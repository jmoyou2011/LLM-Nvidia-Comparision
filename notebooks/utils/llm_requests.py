import requests
import time

# Initalize the url below to avoid undefined error in ngc_request.
fetch_url_format = "https://api.nvcf.nvidia.com/v2/nvcf/pexec/status/" 
 
def ngc_request(url_session, model_url, headers, json_payload, model_name, prompt):

    """
    This function encapsulate the CURL Session in the NGC API.

    Args:
        url_session (request.Session): Session for curl requests.
        model_url (str): Invoke URL for the model.
        headers (dict): Header for the CURL request.
        json_payload (dict): Payload contain model configuration.
        model_name (str): name of the model
        prompt (str): prompt that is used as the input for the LLM.
        
    Output:
        resp_dict (dict): Dictionary containing the relevant fields for analysis.
    """
    # Create a dictionary data structure to hold input | output tokens, message,
    # model name, prompt and output message.  
    resp_dict = {}
    
    # Send a post request to the server.
    response = url_session.post(model_url, headers=headers, json=json_payload)

    # Grab the response from the server serving the 202 response.
    while response.status_code == 202:
      request_id = response.headers.get("NVCF-REQID")
      fetch_url = fetch_url_format + request_id
      response = url_session.get(fetch_url, headers=headers)

    # Extract the json response.
    response.raise_for_status()
    response_body = response.json()
    
    #Extract the relevant fields need for analysis.
    msg = response_body.get('choices')[0].get('message').get('content')
    resp_time = round(response.elapsed.total_seconds(), 3)
    out_tokens = response_body.get('usage').get('completion_tokens')
    in_tokens = response_body.get('usage').get('prompt_tokens')
    resp_dict = {"model_name": model_name, "resp_time": resp_time,
                 "out_tokens": out_tokens, "in_tokens": in_tokens,
                 "prompt": prompt, "message": msg}
    
    return resp_dict

class ModelConfig:
    """
    This call instantiates the configurations for the ngc requests.
    """
    def __init__(self, prompt, api_key, temperature=0.2, top_p=0.7, max_tokens=1024, seed=42, stream=False):
        # Creating the payload configuration.
        self.prompt = prompt
        self.api_key = api_key
        self.temperature = temperature
        self.top_p = top_p
        self.max_tokens = max_tokens
        self.seed = seed
        self.stream = stream

def invoke_one_model(model_name, model_config, model_urls):
    """
    This function will call from any model within the dictionary from Nvidia
    AI foundational models and run the model. This is strictly focused on
    the text-to-text models found on the link below:

    https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-foundation/models

    Models that require context are not included in the dictionary.

    Args:
        model_name (str): name of the model
        model_config (class ModelConfig): prompt to be passed to the model
        model_urls (dict): dictionar

    Outputs:
    Dictionary of the following outputs.
        model_name (str): name of the model
        resp_time (str): time taken to generate the response
        out_tokens (str): Number of tokens returned from the LLM.
        in_tokens (str): Number of tokens that represent the prompt.
        prompt (str): Input string to be ingested by the LLM.
        msg (str): Output response from the LLM.

    """
    # Initialize the headers and payloads for the CURL requests.
    headers = {
        "Authorization": "Bearer " + str(model_config.api_key),
        "Accept": "application/json",
     }

    payload = {
        "messages": [
        {
            "content": str(model_config.prompt),
             "role": "user"
        }
    ],
    "temperature": model_config.temperature,
    "top_p": model_config.top_p,
    "max_tokens": model_config.max_tokens,
    "seed": model_config.seed,
    "stream": model_config.stream
    }
    
    # String formatting for model name to match the model dictionary
    # model_urls dictionary is intialized outside the function.
    model_name = model_name.lower().replace(" ","")
    if model_name not in model_urls.keys():
        print("Model name not found in dictionary, using default model")
        print("Default model is NV-Llama2-70B-RLHF")
        model_name = "nv-llama2-70b-rlhf"
    model_url = model_urls[model_name]
        
    # Create session for curl requests.
    model_session = requests.Session()
    
    return ngc_request(model_session, model_url, headers, payload, model_name, model_config.prompt)
    
def invoke_all_models(model_config, model_urls):
    """
    This function will call from any model within the dictionary from Nvidia
    AI foundational models and run the model. This is strictly focused on
    the text to text models found on the link below:

    https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-foundation/models

    Models that require context or have a different payload
    structure are not included in the dictionary.

    Args:
        model_config (object): Contains all elements for llm config.
        
    Output:
        List of dictionaries:
            lst_resp (list): List of dictionaries for each model.
            
    """
    # Initialize the headers and payloads for the CURL requests.
    headers = {
        "Authorization": "Bearer " + str(model_config.api_key),
        "Accept": "application/json",
    }
    
    payload = {
        "messages": [
        {
            "content": str(model_config.prompt),
             "role": "user"
        }
    ],
    "temperature": model_config.temperature,
    "top_p": model_config.top_p,
    "max_tokens": model_config.max_tokens,
    "seed": model_config.seed,
    "stream": model_config.stream
    }
    
    # Initalize empty list to hold final output.
    lst_resp = []
    
    # Intialize the session for CURL requests.
    model_session = requests.Session()
    
    for key, url in model_urls.items():
        # print(f"Running model {key}")
        # Iterate through each model and store the result in list.
        tmp_resp = ngc_request(model_session, url, headers, payload, key, model_config.prompt)
        lst_resp.append(tmp_resp)
        time.sleep(0.02) # Pause the function so that it is not triggering a rate limit.
    
    return lst_resp
        
        

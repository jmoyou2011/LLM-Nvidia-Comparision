from utils.llm_requests import *

def format_resp_single(model_name: str, model_config, model_urls):
    """
    Formats the output to a human readable style when a model is selected
    get a generated output.

    Args:
        model_name (str): model name that is being invoked
        model_config (Class): class containing model configuration.
        
    Output:
        output (str): formatted output for ease of reading
    """
    # Call the model and format the output by calling the key values.
    llm_out = invoke_one_model(model_name, model_config, model_urls)
    
    output = f"{llm_out['message']}\n\nResponse time: {llm_out['resp_time']} seconds\n\n #Output Tokens:{llm_out['out_tokens']}  #Input Tokens:{llm_out['in_tokens']}  Model Name:{llm_out['model_name']}"
    return output

def format_resp_all(model_config, model_urls):
    """
    Formats the output to human readable style when a prompt is sent
    to all models

    Args:
        model_config (Class): Class containing model configuration.
    
    Output:
        output (str): formatted output for ease of readin
    """
    # Initialze an empty list and sort the output from the call llm models wrt to response time.
    content_lst = []
    llm_out = invoke_all_models(model_config, model_urls)
    llm_out = sorted(llm_out, key=lambda x: x['resp_time'], reverse=False)
    
    # Iterate through results so that we can extract model name, time, in | out tokens.
    for llm_res in llm_out:
        content = f"Model Name: {llm_res['model_name']}  Response Time:{llm_res['resp_time']} seconds  #Input Tokens:{llm_res['in_tokens']}  #Output Tokens:{llm_res['out_tokens']}\n\n"
        content_lst.append(content)
        
    return " ".join(content_lst)
    

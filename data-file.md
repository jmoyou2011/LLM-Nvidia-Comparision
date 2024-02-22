# Data Schema 
This readme will examine how one can modify the data files in notebooks/data directories.

### Questions.csv
The schema for the questions CSV file is listed below:

 - questions (str): The prompt that the LLM model uses to generate text.
 - temperature (float): This value controls the predictability of the LLM, higher is more unpredictable, and lower is more deterministic. Values between 0 and 1.
 - top_p (float): This value controls the size of the vocabulary being considered. Higher is more probabilistic and lower is more deterministic. Values between 0  and 1
 - max_tokens (int): This is the maximum tokens that llm can generate. For the models in this experiment, your limit is 1024.
 - seed (int): Sets the random seed.
 - stream (bool): This tells the model if it is streaming or not.

<p align="center">CSV Screenshot</p>
<p align="center" width="100%">
   <img width="75%" src="https://github.com/jmoyou2011/nvidia-llm-compare/blob/main/screenshots/questions_csv.png">
</p>

### Yaml Model File.
The model YAML files contained the following schema:

 - model_urls (hashmap): This is a key value pair containing the model name with whitespace stripped and lowercase as the key and "invoke_url + model uuid" as the value.
 - model_full_names (hashmap): This is a key value pair containing the model name with whitespace stripped and lowercase as the key and model name as presented on the NVIDIA AI Foundation model catalog as values.
 - invoke-urls (List): This is a list containing the "invoke url" and the "fetch_url_format".

<p align="center">Yaml Screenshot</p>
<p align="center" width="100%">
   <img width="75%" src="https://github.com/jmoyou2011/nvidia-llm-compare/blob/main/screenshots/models_yml.png">
</p>

To have an API key that works with the notebook, you can create a YAML file in the following format:


     NGCKEY:
        API: Your API key 

### JSON Scenario File.

This json file contains the following schema under the name "kv_cache_test.json":

- questions (str): The prompt that the LLM model uses to generate text.
 - temperature (float): This value controls the predictability of the LLM, higher is more unpredictable, and lower is more deterministic. Values between 0 and 1.
 - top_p (float): This value controls the size of the vocabulary being considered. Higher is more probabilistic and lower is more deterministic. Values between 0 and 1
 - max_tokens (int): This is the maximum tokens that llm can generate. For the models in this experiment, your limit is 1024.
 - seed (int): Sets the random seed.
 - stream (bool): This tells the model if it is streaming or not.
 - classification (str): This value is either short-short, short-long, long-short, long-long.

<p align="center">JSON Screenshot</p>
<p align="center" width="100%">
   <img width="75%" src="https://github.com/jmoyou2011/nvidia-llm-compare/blob/main/screenshots/kv_cache_json.png">
</p>

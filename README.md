# Overview
This repo allows you to query multiple NVIDIA AI Foundation LLM models at the same (for FREE 😀) using a single interface. 

https://catalog.ngc.nvidia.com/ai-foundation-models

The goal of the project is to show how you can leverage the AI Foundation Model Endpoints to query many different language models conveniently by sending a single query request to get back the latencies and responses of each of the models of interest

This is most useful and convenient for data scientists and deployment teams who are trying to select the best LLM for their use case based on latency and accuracy. 

The demo is built with Gradio, it shows all the available LLM models (as of 02-16-24) that have the same curl interface. 

### Models
Here is the list of models that were used for this experiment:
   - Mixtral 8x7B Instruct
   - Mistral 7B Instruct
   - NV-Llama2-70B-RLHF
   - NV-Llama2-70B-SteerLM-Chat
   - Code Llama 13B
   - Code Llamm 34B
   - Code Llama 70B
   - Llama 2 13B
   - Llama 2 70B
   - Yi-34B
   - Nemotron-3-8B-QA

### Getting Started




### Screenshots
Below is an image of the gradio interface in which you can select which LLM model and input your prompt to generate text from the LLM.
![Image of choice of LLM](screenshots/single-model-call.png)


Here is another image that shows how the benchmark interface for a singular prompt works when one prompt is run against multiple LLMs.
![Image of metrics from LLMS](screenshots/nvidia-multi-model-llm.png)



### Additional Work

1. Extend this work performance to other types of models on the Nvidia Catalog. This was a strict text-to-text model where the model
   payloads were of the same structure.

2. Rework the async aiohttp notebook to solve for errors in calling the API in an asynchronous fashion i.e. solving for null content when the status_code is 202.

3. Extend the functionality to evaluate the metrics of each LLM under Information Retrieval metrics such as MMR, BLEU Score, ROUGE and, others.  

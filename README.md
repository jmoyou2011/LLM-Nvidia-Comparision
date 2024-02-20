# Overview
This repo allows you to query multiple NVIDIA AI Foundation LLM models at the same (for FREE 😀) using a single interface. 

The goal of the project is to show how you can leverage the AI Foundation Model Endpoints to query many different language models conveniently by sending a single query request to get back the latencies and responses of each of the models of interest

This is most useful and convenient for data scientists and deployment teams trying to select the best LLM for their use case based on latency and accuracy. 

The demo is built with Gradio, it shows all the available LLM models (as of 02-16-24) with the same curl interface. 

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

One must sign up for NGC (https://catalog.ngc.nvidia.com/ai-foundation-models), log in, and head to AI foundational models.
For more information, refer to the "ngc-readme.md" in the file list.

The repo contains two notebooks
   - **nvidia_llm_requests** - This notebook uses the requests module to interact with the Nvidia APIs. This notebook is the completed one 
                               and which performs the benchmarking and illustration through Gradio.

### Screenshots of Outputs
<p align="center">Expected structure of the outputs when the benchmark process is completed</p>
<p align="center" width="100%">
   <img width="75%" src="https://github.com/jmoyou2011/nvidia-llm-compare/blob/main/screenshots/llm-results.png">
</p>

<p align="center" width="100%">
   <img width="75%" src="https://github.com/jmoyou2011/nvidia-llm-compare/blob/main/screenshots/benchmark-llms.png">
</p>

<p align="center">Gradio Interface where a user can select a model and enter a prompt to return a generated message.</p>
<p align="center" width="100%">
   <img width="75%" src="https://github.com/jmoyou2011/nvidia-llm-compare/blob/main/screenshots/single-model-call.png">
</p>

<p align="center">Gradio Interface where a user can enter a prompt to return the models' response time in ascending order.</p>
<p align="center" width="100%">
   <img width="75%" src="https://github.com/jmoyou2011/nvidia-llm-compare/blob/main/screenshots/nvidia-multi-model-llm.png">
</p>

### Additional Work

1. Extend this work performance to other types of models on the Nvidia Catalog. This was a strict text-to-text model where the model
   payloads were of the same structure.

2. Rework the async aiohttp notebook to solve for errors in calling the API in an asynchronous fashion i.e. solving for null content when the status_code is 202.

3. Extend the functionality to evaluate the metrics of each LLM under Information Retrieval metrics such as MMR, BLEU Score, ROUGE and, others.  

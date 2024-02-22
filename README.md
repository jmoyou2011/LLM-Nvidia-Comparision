# Overview
This repo allows you to query multiple NVIDIA AI Foundation LLM models at the same (for FREE 😀) using a single interface. You can leverage this project to see the performance of multiple models across different query types to understand what your production deployment may look like. Keep in mind that the models on the NVIDIA AI Foundation model endpoints are highly optimized and in some cases run across multiple GPUs (using Tensor Parallelism with [TRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) and [NVIDIA Triton](https://github.com/triton-inference-server/server)  

The goal of the project is to show how you can leverage the AI Foundation Model Endpoints to query many different language models conveniently by sending a single query request to get back the latencies and responses of each of the models of interest

This is most useful and convenient for data scientists and deployment teams trying to select the best LLM for their use case based on latency and accuracy. 

There is a demo built with Gradio, it shows all the available LLM models (as of 02-16-24) with the same curl interface to query llms (not code generating ones) 

### Models
Here is the list of models that were used for this experiment:
   - Mixtral 8x7B Instruct
   - Mistral 7B Instruct
   - NV-Llama2-70B-RLHF
   - NV-Llama2-70B-SteerLM-Chat
   - Llama 2 13B
   - Llama 2 70B
   - Yi-34B
   - Nemotron-3-8B-QA

### Getting Started

One must sign up for NGC (https://catalog.ngc.nvidia.com/ai-foundation-models), log in, and head to AI foundational models.
For more information, refer to the "ngc-readme.md" in the file list.

The repo contains one notebook named **nvidia_llm_requests.ipynb**. This notebook uses the requests module to interact with the NVIDIA APIs. The notebook has three sections listed below:

   * Benchmarking against multiple prompts (five in the test case).

   * Benchmarking against multiple query scenarios (short input -> short output, short input -> long output, long input -> short output and, long input -> long output).

   * Interactive Gradio interfaces that allow you to interact with a selected model (single) and user input prompt as well as user input prompt against multiple models. Each interface allows the user to save the response. 

## Screenshots of Outputs
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

<p align="center">Scatter plot showing response time in seconds vs number of input tokens across all the models tested.</p>
<p align="center" width="100%">
   <img width="75%" src="https://github.com/jmoyou2011/nvidia-llm-compare/blob/main/screenshots/response_time-vs-in_tokens-all.png">
</p>

<p align="center">Scatter plot showing response time in seconds vs number of output tokens across all the models tested.</p>
<p align="center" width="100%">
   <img width="75%" src="https://github.com/jmoyou2011/nvidia-llm-compare/blob/main/screenshots/response_time-vs-out_tokens-all.png">
</p>

### Additional Work

1. Extend this work performance to other types of models on the NVIDIA AI Foundation Models catalog. This was a strict text-to-text model comparison where the model payloads were of the same/similar structure.

2. Leverage libraries such as async to send off requests simultaneously. Not sure if multiple concurrent requests from the same key will be denied. TBD.

3. Extend the functionality to evaluate the metrics of each LLM for accuracy to different topics. Each request gives back a text response. Evaluating the speed of an LLM is easy, but accuracy is not and it is very dependent on the use case. Possibly leverage [AlpacaEval](https://github.com/tatsu-lab/alpaca_eval)

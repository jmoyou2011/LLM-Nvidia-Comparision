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


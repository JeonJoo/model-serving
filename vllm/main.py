from vllm import LLM

model = ""  # Name or path of your model
llm = LLM(model=model)  # tensor_parallel_size: int,
result = llm.generate("Hello, my name is")

print(result)

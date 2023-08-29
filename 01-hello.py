from llama_cpp import Llama

llm = Llama(model_path="./models/llama-7b.ggmlv3.q4_0.bin")

response = llm("Who directed The Dark Knight?")

print(response["choices"][0]["text"])

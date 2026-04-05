from transformers import pipeline

print("Loading GPT-2 model...")

generator = pipeline("text-generation", model="gpt2")

prompt = input("Enter your prompt: ")

result = generator(prompt, max_length=80, num_return_sequences=1)

print("\n--- Generated Output ---\n")
print(result[0]['generated_text'])
print("\n------------------------")
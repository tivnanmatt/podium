import openai



# Set your API key

fileObject = open("openai_key.txt", "r")
api_key = fileObject.read()
api_key = api_key.replace("\n","")

openai.api_key = api_key

def generate_response(prompt):
  # Use the GPT-3 API to generate a response to the prompt
  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=2048,
    temperature=0.7,
  )

  # Return the generated response
  return response['choices'][0].text

# Test the function by generating a response to a prompt
# prompt = "What is your favorite color?"
prompt = """
        The following words are selected by a nonverbal autistic child. 
        Please infer what they are trying to say: "jacket", "shoes", "dog", "frisbee"
        """
response = generate_response(prompt)
print(response)

# run another example with a different prompt to check if the model has memory

prompt = """
        Can you give me another example for your response?
        """

response = generate_response(prompt)
print(response)


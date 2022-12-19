import requests

# define text prompt
prompt = "What is your favorite color?"

# Send a POST request to the server
response = requests.post("http://localhost:8000", json={ "userInput": prompt })

# Print the status code and the response text
print("prompt sent to server: \n" + prompt)
print("response from server: \n" + response.text)

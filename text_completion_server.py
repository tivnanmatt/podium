from http.server import HTTPServer, BaseHTTPRequestHandler
import json

import openai

# Set your API key
# we assume the api key is saved in a file "openai_key.txt"
# this file is ignored for the purpose of git check in/out
fileObject = open("openai_key.txt", "r")
api_key = fileObject.read()
api_key = api_key.replace("\n","")
openai.api_key = api_key


def generate_response(userInput,temperature=None):
  # Use the GPT-3 API to generate a response to the prompt
  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=userInput,
    max_tokens=4096-len(userInput),
    temperature=temperature,
  )
  # Return the generated response
  return response['choices'][0].text


class RequestHandler(BaseHTTPRequestHandler):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
  def do_POST(self):
    # Send response
    self.send_response(200)
    self.send_header("Access-Control-Allow-Origin", "*")
    self.end_headers()

    # Get request data
    content_length = int(self.headers["Content-Length"])
    body = self.rfile.read(content_length)

    # Parse the request data as JSON
    request_json = json.loads(body)

    # Set the temperature for AI text generation, if provided
    if request_json.get("temperature", None) is not None:
      temperature = request_json.get("temperature", None)
    else:
      temperature = 0.7
      
    # if textCompletion is provided, use it as the prompt
    if request_json.get("textCompletion", None) is not None:
      prompt = request_json.get("textCompletion", None)
    
      # Generate a response using the generate_response function
      response = generate_response(prompt,temperature)

      # Send the response to the client
      self.wfile.write(response.encode())

# Start the server
httpd = HTTPServer(("0.0.0.0", 8000), RequestHandler)
httpd.serve_forever()

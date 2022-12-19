# Podium Text Completion Server

This project consists of a Python script that uses the OpenAI API to generate responses to user input. The script starts an HTTP server that listens for POST requests on port 8000. When a POST request is received, the script extracts the "userInput" value from the request body, which is in JSON format, and passes it to the `generate_response` function. This function uses the OpenAI API to generate a response to the user input, and the resulting response is sent back to the client.

## Files

- `text_completion_server.py`: the main script for the project
- `test_text_completion_server.py`: a test script for the project
- `.gitignore`: a list of files and directories to ignore when committing to Git
- `html_pages`: a directory containing HTML files for the project
  - `index.html`: the main HTML file for the project
  - `tarot.html`: an HTML file for the project

## Installation

To install the dependencies for this project, run the following command:

pip install openai


## Usage

To start the server, run the following command:

python text_completion_server.py

Copy code

The server will listen for POST requests on port 8000. To send a request to the server, you can use a tool such as `curl`:

curl -X POST -H "Content-Type: application/json" -d '{"userInput": "Hello, world!"}' http://localhost:8000

Copy code

The server will return a response based on the user input.

## Testing

To run the test suite for this project, run the following command:

python test_text_completion_server.py

Copy code

The `test_text_completion_server.py` script contains unit tests for the `text_completion_server.py` script. It tests the `generate_response` function to ensure that it returns the expected output for different inputs.

## Contributing

If you would like to contribute to this project, please follow these guidelines:

- Use descriptive commit messages and pull request titles
- Follow the code style used in the project
- Test your changes thoroughly

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

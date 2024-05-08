# Question Answering API

This repository contains a Question Answering API that generates answers to questions based on webpage content using a pre-trained model.

## Features

- Fetches webpage content given a URL
- Extracts relevant sections from the webpage
- Uses a pre-trained question-answering model to generate answers
- Provides a confidence score for the generated answers
- Supports easy integration with web applications

## Requirements

- Python 3.10 or above
- Required libraries:
  - `requests`
  - `beautifulsoup4`
  - `lxml`
  - `transformers`
  - `gradio`

## Installation

1. Clone the repository:
git clone https://github.com/Cruz455/QA-Model-.git

2. Navigate to the project directory:
cd your-repository

3. Create a virtual environment (optional but recommended):
python -m venv venv

4. Activate the virtual environment:
- For Windows:
  ```
  venv\Scripts\activate
  ```
- For macOS and Linux:
  ```
  source venv/bin/activate
  ```

5. Install the required libraries:
pip install -r requirements.txt

## Usage

1. Run the API:
python api.py

2. Access the API in your web browser at `http://localhost:7860`.

3. Enter a URL and a question in the provided input fields.

4. Click the "Submit" button to generate an answer.

5. The generated answer and its confidence score will be displayed.

## API Endpoint

- **URL:** `/`
- **Method:** `POST`
- **Request Body:**
- `url` (string): The URL of the webpage to fetch content from.
- `question` (string): The question to be answered based on the webpage content.
- **Response:**
- `answer` (string): The generated answer to the provided question.
- `score` (float): The confidence score of the generated answer.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [Apache License 2.0](LICENSE).

## Acknowledgements

- This project utilizes the `deepset/roberta-large-squad2` pre-trained model for question answering.
- The `transformers` library by Hugging Face is used for model integration.
- The `gradio` library is used for creating the user interface.

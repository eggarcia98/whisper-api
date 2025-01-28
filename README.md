# Whisper Transcription Service

This is a Flask application that transcribes audio files using the Whisper model.

## Features

- Upload an audio file and get its transcription.
- Supports Cross-Origin Resource Sharing (CORS) using Flask-CORS.

## Requirements

- Python 3.10 or higher
- Flask 2.3.3
- openai-whisper 20240930
- Flask-Cors 4.0.1

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Set the `MODEL_NAME` environment variable (optional, default is "turbo"):
    ```sh
    export MODEL_NAME="base"
    ```

2. Run the Flask application:
    ```sh
    python app.py
    ```

3. The application will be available at `http://0.0.0.0:8080`.

## API Endpoints

### POST /get-transcript-audio

Upload an audio file to get its transcription.

#### Request

- [file](http://_vscodecontentref_/0): The audio file to be transcribed.

#### Response

- `200 OK`: Returns the transcription of the audio file.
    ```json
    {
        "transcription": "Transcribed text here"
    }
    ```

- `400 Bad Request`: If the file is not provided or the file name is empty.
    ```json
    {
        "error": "No file part in the request"
    }
    ```

    ```json
    {
        "error": "No file selected"
    }
    ```

- `500 Internal Server Error`: If there is an error during transcription.
    ```json
    {
        "error": "Error message here"
    }
    ```

## Docker

You can also run the application using Docker.

1. Build the Docker image:
    ```sh
    docker build -t whisper-transcription-service .
    ```

2. Run the Docker container:
    ```sh
    docker run -p 8080:8080 whisper-transcription-service
    ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
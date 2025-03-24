# GenAI Quickstart

A client for interacting with Azure OpenAI.

## Requirements

- Python 3.13
- [optional] A container engine like Docker, Podman, or Colima

## Environment Variables

Set the required environment variables, e.g. in your `~/.zshrc` file:

```sh
export AZURE_OPENAI_API_KEY=...
export AZURE_OPENAI_ENDPOINT=...
```


## Local Usage Instructions

1. Install Python 3.13 from [python.org](https://www.python.org/downloads/release/python-3130/).

2. Install Poetry (a virtual environment and package manager for Python)
    ```sh
    python3 -m pip install poetry
    ```

4. Clone the repository:

    ```sh
    git clone https://github.com/miles-slalom/genai-quickstart.git
    cd genai_quickstart
    ```

5. Install dependencies using Poetry:

    ```sh
    poetry install
    ```


2. Run the application:

    ```sh
    poetry run python fuzzy_broccoli/azure_openai_client.py
    ```

## Docker Usage Instructions

1. Build the Docker image:

    ```sh
    docker-compose build
    ```

2. Run the Docker container:

    ```sh
    docker-compose up
    ```

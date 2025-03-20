# Fuzzy Broccoli

A client for interacting with Azure OpenAI.

## Requirements

- Git Client
- Python 3.13
- [optional] A container engine like Docker, Podman, or Colima

## Environment Variables

1. Set the required environment variables, e.g. in your `~/.zshrc` file:

    ```sh
    export AZURE_OPENAI_API_KEY=...
    export AZURE_OPENAI_ENDPOINT=...
    ```

Note: if you are using Windows, you may need to set these environment variables in the Control Panel.

2. Close and reopen your shell/Terminal window to ensure that the environment variables take effect.

3. Confirm that the environment variables are present:

    ```sh
    echo $AZURE_OPENAI_API_KEY
    echo $AZURE_OPENAI_ENDPOINT
    ```
    If you do not see the environment variable values.

## Local Usage Instructions
1. Install Git from [git-scm.org](https://www.git-scm.org/)
2. Install Python 3.13 from [python.org](https://www.python.org/downloads/release/python-3130/).

3. Open a Terminal window. If you are using Windows, the preferred terminal is Git Bash, which is installed automatically when you install Git.

4. Install Poetry (a virtual environment and package manager for Python)
    ```sh
    python3 -m pip install poetry
    ```
    
3. Clone the repository:

    ```sh
    git clone https://github.com/miles-slalom/fuzzy-broccoli.git
    cd fuzzy-broccoli
    ```

4. Install dependencies using Poetry:

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

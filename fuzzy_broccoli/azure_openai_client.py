import os
from openai import AzureOpenAI

api_key = os.environ["AZURE_OPENAI_API_KEY"]
azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
deployment_name = "gpt-4o-mini"


class AzureOpenAIClient:
    def __init__(self):
        """Creates an Azure OpenAI client."""
        self.client = AzureOpenAI(
            api_key=api_key,
            api_version="2024-02-01",
            azure_endpoint=azure_endpoint,
        )

    def create_completion(
        self,
        user_prompt: str,
        system_prompt: str = "You are a helpful assistant.",
    ) -> str:
        """Generates a response to a single prompt."""
        response = self.client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        completion = response.choices[0].message.content
        return completion


def main():
    """Tests the API connection and outputs results to the console."""
    client = AzureOpenAIClient()
    completion = client.create_completion(
        "What is the meaning of life? Please express your answer as an integer."
    )
    print(completion)


if __name__ == "__main__":
    main()

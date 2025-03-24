import os
from openai import AzureOpenAI

api_key = os.environ["AZURE_OPENAI_API_KEY"]
azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]


class AzureOpenAIClient:
    def __init__(self, deployment_name: str = "gpt-4o-mini"):
        """Creates an Azure OpenAI client."""
        self.client = AzureOpenAI(
            api_key=api_key,
            api_version="2024-02-01",
            azure_endpoint=azure_endpoint,
        )
        self.deployment_name = deployment_name

    def answer_question(
        self,
        user_prompt: str,
        system_prompt: str = "You are a helpful assistant.",
        temperature: float = 1,
        top_p: float = 1,
    ) -> str | None:
        """Generates a response to a single prompt."""
        response = self.client.chat.completions.create(
            model=self.deployment_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=temperature,
            top_p=top_p,
        )
        completion = response.choices[0].message.content
        return completion


def main():
    """Tests the API connection and outputs results to the console."""
    openai_client = AzureOpenAIClient("gpt-4o-mini")
    completion = openai_client.answer_question(
        "What is the meaning of life? Please express your answer as an integer."
    )
    print(completion)


if __name__ == "__main__":
    main()

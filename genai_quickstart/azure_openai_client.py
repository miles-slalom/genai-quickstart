import os
from openai import AzureOpenAI
from context_gateway import load_context

api_key = os.environ["AZURE_OPENAI_API_KEY"]
azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]


class AzureOpenAIClient:
    """Handles direct interaction with the Azure OpenAI API."""
    def __init__(self, api_key: str, azure_endpoint: str, api_version: str = "2024-02-01"):
        self.client = AzureOpenAI(
            api_key=api_key,
            api_version=api_version,
            azure_endpoint=azure_endpoint,
        )

    def generate_completion(self, deployment_name: str, messages: list, temperature: float = 1, top_p: float = 1) -> str:
        """Generates a completion using the Azure OpenAI API."""
        response = self.client.chat.completions.create(
            model=deployment_name,
            messages=messages,
            temperature=temperature,
            top_p=top_p,
        )
        return response.choices[0].message.content


class Conversation:
    """Manages conversation history and delegates API calls to AzureOpenAIClient."""
    def __init__(self, azure_client: AzureOpenAIClient, deployment_name: str = "gpt-4o-mini",
                 system_prompt: str = "You are a helpful assistant.", additional_context_file: str = None):
        self.azure_client = azure_client
        self.deployment_name = deployment_name
        if additional_context_file is not None:
            additional_context = load_context(additional_context_file)
            system_prompt += f"""
<instructions>
Below is some additional context data that you should use to answer questions.
If the answer is present in this context, ALWAYS use the context to answer the question.
If the answer is NOT present in this context, say "I don't know."
Do not make up an answer if it is not present in the context.
</instructions>
<context>
{additional_context}
</context>"""
        self.conversation_history = [{"role": "system", "content": system_prompt}]
        if additional_context_file is not None:
            additional_context = load_context(additional_context_file)
            self.conversation_history.append({"role": "system", "content": additional_context})

    def interact(self, user_prompt: str, temperature: float = 1, top_p: float = 1) -> str:
        """Adds user input to the conversation and generates a response."""
        self.conversation_history.append({"role": "user", "content": user_prompt})
        completion = self.azure_client.generate_completion(
            deployment_name=self.deployment_name,
            messages=self.conversation_history,
            temperature=temperature,
            top_p=top_p,
        )
        self.conversation_history.append({"role": "assistant", "content": completion})
        return completion


def main():
    """Runs a conversation at the console."""
    azure_client = AzureOpenAIClient(api_key=api_key, azure_endpoint=azure_endpoint)

    # Specify the additional context file
    additional_context_file = "genai_quickstart/context_data.txt"
    conversation = Conversation(
        azure_client, 
        deployment_name="gpt-4o-mini", 
        additional_context_file=additional_context_file
    )

    print("Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input == "exit":
            break
        completion = conversation.interact(user_input, temperature=0)
        print(f"AI: {completion}")


if __name__ == "__main__":
    main()

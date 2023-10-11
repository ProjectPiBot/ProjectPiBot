import openai

class ChatApp:
    def __init__(self):
        # Setting the API key to use the OpenAI API
        openai.api_key = ("")
        self.messages = [
            {"role": "system", "content": "어시스턴트 로봇 파이봇"},
        ]

    def chat(self, message, context=None):
        if context:
            self.messages.append({"role": "assistant", "content": context})

        self.messages.append({"role": "user", "content": message})

        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = self.messages,
            max_tokens = 100,
        )
        self.messages.append({"role": "assistant", "content": response["choices"][0]["message"].content})
        return response["choices"][0]["message"].content.strip()


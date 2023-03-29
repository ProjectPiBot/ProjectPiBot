import openai

openai.api_key = ("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")

def response(text):
    response = openai.Completion.create(
                model = "text-davinci-003", 
                prompt = text,
                temperature = 0,
                max_tokens = 100,
                top_p = 1,
                frequency_penalty = 0.0,
                presence_penalty = 0.0,
                stop=["#n"]
    )
    return str(response.choices[0].text.strip())
    # #print(response)

    # print(response.choices[0].text.strip())
    # #print(str(response))
    # TTS.speak(str(response.choices[0].text.strip()))

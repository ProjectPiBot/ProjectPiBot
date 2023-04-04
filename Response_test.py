import openai

openai.api_key = ("api key")

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
    print(response.choices[0].text.strip())
    return response.choices[0].text.strip()
    # #print(response)

    # print(response.choices[0].text.strip())
    # #print(str(response))
    # TTS.speak(str(response.choices[0].text.strip()))
import openai

openai.api_key = "API_KEY here"

conversation = ""

while True:
    question = input("Usuario: ")
    conversation += f"Usuario: {question}\nAI: "
    prompt = conversation.strip()

    if not question:
        break

    if len(prompt) > 0:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.9,
            max_tokens=1024,
            n=1,
            stop=None,
        )
        answer = response.choices[0].text.strip()
        conversation += answer + "\n"
        print(f"AI: {answer}\n")
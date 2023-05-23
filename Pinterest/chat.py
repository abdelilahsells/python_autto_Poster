def chatgpt(qt):
    import openai
    openai.api_key = ''
    model_engine = "text-davinci-003"
    prompt = qt
    max_tokens = 255

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return completion.choices[0].text
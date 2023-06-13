import openai
openai.api_key = 'my_api_key'
response = openai.Completion.create(
    engine="text_davinci-002",
    prompt="Translate the following English text to French: '{}'",
    max_tokens=60
)

print(response.choices[0].text.strip())

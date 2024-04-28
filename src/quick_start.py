import ollama

CONTENT1 = "まどかマギカで人気のキャラクターは誰でしょうか？"
CONTENT2 = "日本で二番目に高い山はどこでしょうか？"

response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': CONTENT2,
  },
])
print(response['message']['content'])
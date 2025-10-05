import requests
 
def query_ollama(prompt, model="qwen3:4b"):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": False}
    )
    return response.json()["response"]
 
answer = query_ollama("用简单的中文解释量子计算")
print(answer)

"""
curl http://localhost:11434/api/generate -d '{
  "model": "qwen3:4b",
  "prompt": "为什么天空是蓝色的？",
  "stream": false
}'
"""
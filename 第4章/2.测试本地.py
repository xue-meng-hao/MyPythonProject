# openai_style_demo.py
from openai import OpenAI

# 连接到本地的 Ollama 服务
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # 这里的 api_key 是必需的，但可以是任意值
)


def ask_model_via_openai(prompt: str, model: str = " 你deepseek-r1:7b") -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        stream=True
    )
    return response


if __name__ == "__main__":
    question = "为什么天空是蓝色的？请用中文简单解释一下。"
    answer = ask_model_via_openai(question, model="deepseek-r1:7b")
    for chunk in answer:
        print(chunk.choices[0].delta.content, end="", flush=True)
    # print(answer)

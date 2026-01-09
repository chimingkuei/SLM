import ollama

def ollama_chat(prompt):
    response = ollama.chat(model='mistral', messages=[
        {'role': 'user', 'content': prompt}
    ])
    return response['message']['content']

def general_chat():
    print("\n=== Ollama 一般聊天模式，輸入 '0' 離開聊天 ===")
    while True:
        user_input = input("你：").strip()
        if user_input == "0":
            print("退出聊天模式，返回主選單。")
            break
        if not user_input:
            print("請輸入訊息或輸入 0 離開。")
            continue
        try:
            response = ollama_chat(user_input)
            print(f"Ollama：{response}\n")
        except Exception as e:
            print(f"❌ 發生錯誤：{e}\n")

if __name__ == "__main__":
    general_chat()
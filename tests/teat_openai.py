# 1. 導入必要的函式庫
import os
from openai import OpenAI
from dotenv import load_dotenv

# 2. 載入 .env 檔案中的環境變數
#    執行這行後，os.getenv() 就能讀到 .env 裡面的設定了
load_dotenv()

# 3. 從環境變數讀取 API 金鑰，並建立 OpenAI 客戶端
api_key = os.getenv("OPENAI_API_KEY")

# 檢查是否真的有讀到金鑰，如果沒有就報錯停止，這是好習慣
if not api_key:
    raise ValueError("API 金鑰未設定，請檢查你的 .env 檔案。")

client = OpenAI(api_key=api_key)

# --- 以下是 OpenAI 的範例，幾乎沒變 ---

# 4. 準備要發送的訊息
messages_to_send = [
    {"role": "user", "content": "寫一首關於AI的俳句"}
]

# 5. 呼叫 API 並取得回應
print("正在呼叫 OpenAI API，請稍候...")
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=messages_to_send
)

# 6. 解析並印出結果
#    我們多加一個 .content，可以直接取得純文字的內容
ai_haiku = completion.choices[0].message.content
print("\n--- AI 的回答 ---")
print(ai_haiku)
print("--------------------")
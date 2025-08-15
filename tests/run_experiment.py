# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 14:39:31 2025

@author: a2233
"""

# 1. 導入所有必要的函式庫
import os
import time
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
from tqdm import tqdm # 用於顯示進度條

# 2. 載入環境變數並設定 API 金鑰
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API 金鑰未設定，請檢查你的 .env 檔案。")
client = OpenAI(api_key=api_key)


# 3. 定義實驗的固定參數 (Constants)
# ----------------------------------------------------
MODEL_NAME = "gpt-4o"  # 我們使用 gpt-4o，能力更強
NUM_SAMPLES_PER_THEME = 250 # 每個主題的取樣次數
OUTPUT_FILENAME = f"tarot_experiment_results_{time.strftime('%Y%m%d')}.csv" # 加上日期，方便管理

# 這是我們最終定案的提示詞模板
PROMPT_TEMPLATE = """你現在是一個塔羅牌模擬器。
你的牌庫僅包含 22 張大阿爾克那。
請為接下來的問題，隨機抽出一張牌。
你只需要回答那張牌的名稱，不要有任何解釋或多餘的文字。

問題：「{question}」"""

# 這是我們要測試的所有主題和對應的問句
THEMES = {
    "work": "我想要問工作。",
    "love": "我想要問愛情。",
    "control": "請為我抽一張牌。"
}
# ----------------------------------------------------


def run_experiment():
    """執行完整抽牌實驗的主函式"""
    
    # 建立一個空的 list，用來存放所有實驗結果
    all_results = []
    
    print("實驗開始...")
    
    # 4. 外層迴圈：遍歷每一個主題
    for theme_name, question_text in THEMES.items():
        print(f"\n--- 正在處理主題: {theme_name} ---")
        
        # 5. 內層迴圈：在每個主題下，重複抽牌 N 次
        # tqdm 會自動產生一個進度條
        for i in tqdm(range(NUM_SAMPLES_PER_THEME), desc=f"抽牌進度"):
            try:
                # 組合出這次要發送的完整提示詞
                final_prompt = PROMPT_TEMPLATE.format(question=question_text)
                
                # 呼叫 API
                completion = client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=[
                        {"role": "user", "content": final_prompt}
                    ],
                    temperature=1.0 # 確保足夠的「隨機性」
                )
                
                # 取得並清理回覆的牌名
                card_drawn = completion.choices[0].message.content.strip()
                
                # 將這次的結果打包成一個字典
                result_record = {
                    "theme": theme_name,
                    "run_number": i + 1,
                    "card_drawn": card_drawn,
                    "error": None
                }
                
            except Exception as e:
                # 如果 API 呼叫失敗，記錄下錯誤訊息
                print(f"\n在執行 {theme_name} 主題第 {i+1} 次時發生錯誤: {e}")
                result_record = {
                    "theme": theme_name,
                    "run_number": i + 1,
                    "card_drawn": "ERROR",
                    "error": str(e)
                }
                
            # 將這次的結果加入到總列表中
            all_results.append(result_record)
            
            # 禮貌性地停頓1秒，避免過於頻繁地呼叫 API
            time.sleep(1)

    print("\n\n實驗完成！正在將結果儲存至 CSV 檔案...")

    # 6. 將所有結果轉換成 Pandas DataFrame 並儲存
    results_df = pd.DataFrame(all_results)
    results_df.to_csv(OUTPUT_FILENAME, index=False, encoding='utf-8-sig')
    
    print(f"結果已成功儲存至檔案: {OUTPUT_FILENAME}")
    
# 程式執行的進入點
if __name__ == "__main__":
    run_experiment()
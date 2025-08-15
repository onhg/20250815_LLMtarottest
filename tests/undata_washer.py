# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 15:37:48 2025

@author: a2233
"""

import pandas as pd
from config_maps import ALIAS_MAP, STANDARD_NAMES

# --- 設定區 (與前一腳本完全相同) ---
RAW_DATA_FILE = 'tarot_experiment_results_20250722.csv'

# --- 執行區 ---

print(f"正在讀取原始檔案: {RAW_DATA_FILE}")
df = pd.read_csv(RAW_DATA_FILE)

# ... (中間的清理流程不變) ...
df_copy = df.copy()
df_copy['card_cleaned'] = df_copy['card_drawn']
df_copy['card_cleaned'] = df_copy['card_cleaned'].str.strip('「」。 ')
df_copy['card_cleaned'] = df_copy['card_cleaned'].replace(ALIAS_MAP)
is_invalid = ~df_copy['card_cleaned'].isin(STANDARD_NAMES)
invalid_entries = df_copy[is_invalid]
unmapped_cards = invalid_entries['card_drawn'].unique()


print("\n--- 請將以下自動生成的程式碼，複製並貼到主清理腳本的 ALIAS_MAP 中 ---")
if len(unmapped_cards) > 0:
    print("# --- 自動生成 START ---")
    for original_card in unmapped_cards:
        # 智慧猜測：移除常見的贅字和符號，作為建議的標準名稱
        # 你可以根據需要增加更多的 .replace()
        guessed_name = original_card.replace('。', '').replace('「', '').replace('」', '').replace('牌', '').strip()
        
        # **核心更動：產生字典格式的字串**
        # 我們使用 f-string 來組合出 "Key": "Value", 這樣的格式
        print(f'    "{original_card}": "{guessed_name}",')
        
    print("# --- 自動生成 END ---")
else:
    print("太棒了！所有牌名都已成功對應。")
print("--------------------------------------------------------------------------")
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 15:31:51 2025

@author: a2233
"""

import pandas as pd
from config_maps import ALIAS_MAP, STANDARD_NAMES

# --- 設定區 ---
RAW_DATA_FILE = 'tarot_experiment_results_20250722.csv'
CLEANED_DATA_FILE = 'cleaned_tarot_results.csv'

# 定義標準牌名 (使用韋特塔羅的通用中文名稱)
# 這是我們的「白名單」

# --- 執行區 ---

print(f"正在讀取原始檔案: {RAW_DATA_FILE}")
df = pd.read_csv(RAW_DATA_FILE)

# 複製一份新的欄位來進行清理，保留原始數據
df['card_cleaned'] = df['card_drawn']

# 1. 移除前後多餘的符號和空白
#    例如：「戀人」 -> 戀人  或  戀人。 -> 戀人
df['card_cleaned'] = df['card_cleaned'].str.strip('「」。 ')

# 2. 根據對照表，統一別名
df['card_cleaned'] = df['card_cleaned'].replace(ALIAS_MAP)

# 3. 處理非大阿爾克那的牌 (模型失誤)
#    將所有不在我們標準22張牌名單中的牌，都歸類為 "Other/Invalid"
df.loc[~df['card_cleaned'].isin(STANDARD_NAMES), 'card_cleaned'] = 'Other/Invalid'


print("\n--- 資料清理後，各主題牌卡分佈 ---")
for theme in ['love', 'work', 'control']:
    counts = df[df['theme'] == theme]['card_cleaned'].value_counts()
    print(f"\n【{theme}】主題：")
    print(counts)

# 4. 儲存清理乾淨的檔案
df.to_csv(CLEANED_DATA_FILE, index=False, encoding='utf-8-sig')
print(f"\n清理完成的檔案已儲存至: {CLEANED_DATA_FILE}")
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 15:59:08 2025

@author: a2233
"""

import pandas as pd

# --- 設定區 ---
CLEANED_DATA_FILE = '第二次占卜_自動化清洗_手動打磨板.csv'

# --- 執行區 ---

try:
    df = pd.read_csv(CLEANED_DATA_FILE)

    print("--- 各主題內牌卡佔比分析 ---")

    # 取得所有獨一無二的主題名稱
    themes = df['theme'].unique()

    # 遍歷每一個主題
    for theme in themes:
        print(f"\n【{theme.upper()}】主題分析:")
        
        # 1. 篩選出該主題的所有數據
        theme_df = df[df['theme'] == theme]
        
        # 2. 使用 value_counts() 計算每個值的佔比
        #    normalize=True 是關鍵，它會自動將次數轉換為比例 (0.0 ~ 1.0)
        percentage_series = theme_df['card_cleaned'].value_counts(normalize=True) * 100
        
        # 3. 將結果格式化成容易閱讀的百分比字串
        percentage_formatted = percentage_series.map('{:.2f}%'.format)
        
        # 4. 印出結果
        print(percentage_formatted)
        
except FileNotFoundError:
    print(f"錯誤：找不到檔案 '{CLEANED_DATA_FILE}'。請確認清理資料的腳本已成功執行。")
except Exception as e:
    print(f"發生錯誤：{e}")
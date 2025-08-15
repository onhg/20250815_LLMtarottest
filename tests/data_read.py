# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 15:27:09 2025

@author: a2233
"""

import pandas as pd

# 請確認檔案名稱與你的檔案一致
filename = 'tarot_experiment_results_20250722.csv'

# 讀取你的實驗結果
try:
    df = pd.read_csv(filename)

    print("--- 實驗結果頻率統計 ---")

    # 篩選出「愛情」主題並計算次數
    love_counts = df[df['theme'] == 'love']['card_drawn'].value_counts()
    print("\n【愛情】主題牌卡分佈：")
    print(love_counts)

    # 篩選出「工作」主題並計算次數
    work_counts = df[df['theme'] == 'work']['card_drawn'].value_counts()
    print("\n【工作】主題牌卡分佈：")
    print(work_counts)

    # 篩選出「控制組」主題並計算次數
    control_counts = df[df['theme'] == 'control']['card_drawn'].value_counts()
    print("\n【控制組】主題牌卡分佈：")
    print(control_counts)

except FileNotFoundError:
    print(f"錯誤：找不到檔案 '{filename}'。請將此腳本與你的 CSV 檔案放在同一個資料夾中。")
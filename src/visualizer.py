# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 16:06:15 2025

@author: a2233
"""

import pandas as pd
import matplotlib.pyplot as plt

# --- Matplotlib 設定 ---
# 這是關鍵步驟，用來設定字體，確保圖表中的中文能正常顯示
# 如果你的電腦沒有 JhengHei (微軟正黑體)，可以換成其他支援中文的字體，例如 'SimHei'
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
# 用來正常顯示負號
plt.rcParams['axes.unicode_minus'] = False


# --- 數據準備 ---
# 我們直接將你之前產出的百分比數據，建立成 Pandas Series 物件
love_data = {
    "戀人": 99.20, "節制": 0.40, "愚者": 0.40
}
love_series = pd.Series(love_data)

work_data = {
    "命運之輪": 32.00, "隱者": 23.20, "力量": 6.80, "戰車": 6.40, 
    "節制": 4.40, "皇帝": 4.00, "正義": 4.00, "皇后": 2.80, 
    "女祭司": 2.80, "愚者": 2.40, "戀人": 2.40, "倒吊人": 2.40, 
    "教皇": 1.60, "世界": 1.20, "審判": 0.80, "塔": 0.80, 
    "月亮": 0.80, "死神": 0.40, "星星": 0.40, "Other/Invalid": 0.40
}
work_series = pd.Series(work_data)

control_data = {
    "命運之輪": 18.80, "隱者": 17.20, "女祭司": 8.40, "死神": 7.20, 
    "正義": 5.60, "魔術師": 5.20, "戀人": 4.80, "倒吊人": 4.40, 
    "力量": 4.40, "愚者": 4.00, "節制": 3.20, "皇帝": 3.20, 
    "戰車": 2.80, "月亮": 2.40, "世界": 2.40, "皇后": 2.00, 
    "審判": 1.20, "星星": 1.20, "教皇": 1.20, "惡魔": 0.40
}
control_series = pd.Series(control_data)

# --- 繪圖區 ---

# 計算理想中的均勻分佈機率
ideal_prob = (1 / 22) * 100

def create_distribution_plot(series, title):
    """這是一個專門用來畫圖的函式"""
    plt.figure(figsize=(14, 8)) # 設定圖表畫布的大小
    
    # 繪製長條圖
    ax = series.plot(kind='bar', width=0.8, zorder=2, 
                     color='#4285F4', alpha=0.9,
                     edgecolor='black', linewidth=0.5)
    
    # 繪製代表「理想均勻分佈」的紅色虛線
    ax.axhline(y=ideal_prob, color='red', linestyle='--', linewidth=2, 
               label=f'理想均勻分佈 ({ideal_prob:.2f}%)')
    
    # 設定圖表的標題和座標軸標籤
    ax.set_title(f'主題: {title} - 牌卡分佈百分比', fontsize=20, pad=20)
    ax.set_ylabel('出現百分比 (%)', fontsize=14)
    ax.set_xlabel('大阿爾克那牌', fontsize=14)
    
    # 優化圖表外觀
    plt.xticks(rotation=45, ha='right', fontsize=12) # 旋轉X軸的標籤，避免重疊
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.6) # 加入水平格線
    plt.legend(fontsize=14)
    plt.tight_layout() # 自動調整邊距，避免標籤被裁切
    plt.show() # 顯示圖表

# --- 主程式執行 ---
# 依序呼叫函式，繪製三張圖表
create_distribution_plot(love_series, '愛情 (Love)')
create_distribution_plot(work_series, '工作 (Work)')
create_distribution_plot(control_series, '控制組 (Control)')
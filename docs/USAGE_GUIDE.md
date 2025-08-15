# LLM 塔羅牌實驗使用指南

## 🎯 概述

這份指南將詳細說明如何使用本專案進行 LLM 塔羅牌隨機性實驗。

## 📋 前置準備

### 1. 取得 OpenAI API 金鑰

1. 前往 [OpenAI Platform](https://platform.openai.com/)
2. 登入或註冊帳號
3. 前往 [API Keys](https://platform.openai.com/api-keys) 頁面
4. 點擊「Create new secret key」建立新金鑰
5. **重要**：立即複製並妥善保存金鑰（僅顯示一次）

### 2. 環境設定

```bash
# 複製環境變數範本
cp env.example .env

# 使用文字編輯器編輯 .env 檔案
# 將 your_openai_api_key_here 替換為您的實際 API 金鑰
```

## 🚀 執行完整實驗

### 步驟 1：執行抽牌實驗

```bash
python src/experiment.py
```

**注意事項：**
- 完整實驗需要 750 次 API 呼叫（3組 × 250次）
- 預估費用：約 $3-5 USD（依當前 API 費率）
- 執行時間：約 12-15 分鐘（包含 1 秒間隔）

實驗將生成：`tarot_experiment_results_YYYYMMDD.csv`

### 步驟 2：清洗數據

```bash
python src/data_cleaner.py
```

此步驟會：
- 統一不同格式的牌名
- 移除無效回應
- 生成清洗後的數據檔案

### 步驟 3：生成視覺化

```bash
python src/visualizer.py
```

將產生三張分佈圖：
- 愛情組牌卡分佈
- 工作組牌卡分佈  
- 控制組牌卡分佈

## ⚙️ 自定義實驗

### 修改實驗參數

編輯 `src/experiment.py`：

```python
# 調整每組抽牌次數
NUM_SAMPLES_PER_THEME = 100  # 減少至 100 次以節省費用

# 修改測試問題
THEMES = {
    "health": "我想要問健康。",
    "money": "我想要問財運。",
    "control": "請為我抽一張牌。"
}

# 更換 AI 模型
MODEL_NAME = "gpt-4o-mini"  # 使用更便宜的模型
```

### 新增牌名對照規則

如果發現新的牌名變體，編輯 `src/config_maps.py`：

```python
ALIAS_MAP = {
    # 現有對照...
    "新發現的別名": "標準牌名",
    "戀人牌（英文）": "戀人",
}
```

## 📊 結果分析

### 檢視原始數據

```python
import pandas as pd

# 讀取原始結果
df = pd.read_csv('tarot_experiment_results_20250722.csv')
print(df.head())

# 查看各組分佈
for theme in ['love', 'work', 'control']:
    theme_data = df[df['theme'] == theme]
    print(f"\n{theme} 組結果:")
    print(theme_data['card_drawn'].value_counts().head(10))
```

### 檢視清洗後數據

```python
# 讀取清洗後結果
clean_df = pd.read_csv('cleaned_tarot_results.csv')

# 計算各組的分佈百分比
for theme in ['love', 'work', 'control']:
    theme_data = clean_df[clean_df['theme'] == theme]
    percentages = theme_data['card_cleaned'].value_counts(normalize=True) * 100
    print(f"\n{theme} 組百分比分佈:")
    print(percentages.head(10))
```

## 🛠️ 疑難排解

### 常見問題

**Q: API 金鑰錯誤**
```
ValueError: API 金鑰未設定，請檢查你的 .env 檔案。
```
**A:** 確認 `.env` 檔案存在且格式正確：
```
OPENAI_API_KEY=your_actual_api_key_here
```

**Q: 模組導入錯誤**
```
ModuleNotFoundError: No module named 'openai'
```
**A:** 重新安裝依賴：
```bash
pip install -r requirements.txt
```

**Q: 字體錯誤（視覺化）**
```
findfont: Font family ['Microsoft JhengHei'] not found
```
**A:** 修改 `src/visualizer.py` 中的字體設定：
```python
# Windows
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'SimHei'] 
# macOS
plt.rcParams['font.sans-serif'] = ['Helvetica', 'Arial Unicode MS']
# Linux
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'SimHei']
```

### API 使用建議

1. **監控費用**：在 OpenAI 帳戶設定使用限額
2. **測試先行**：先用少量樣本測試（例如每組 10 次）
3. **網路穩定**：確保執行期間網路連線穩定
4. **備份金鑰**：妥善保存 API 金鑰，避免洩漏

## 📈 進階分析

### 統計顯著性檢驗

```python
import scipy.stats as stats

# 卡方檢驗比較各組分佈
love_counts = clean_df[clean_df['theme'] == 'love']['card_cleaned'].value_counts()
control_counts = clean_df[clean_df['theme'] == 'control']['card_cleaned'].value_counts()

# 重新索引確保相同的牌序
all_cards = set(love_counts.index) | set(control_counts.index)
love_aligned = love_counts.reindex(all_cards, fill_value=0)
control_aligned = control_counts.reindex(all_cards, fill_value=0)

chi2, p_value = stats.chisquare(love_aligned, control_aligned)
print(f"卡方統計量: {chi2:.4f}")
print(f"p-value: {p_value:.4f}")
```

### 資訊熵分析

```python
import numpy as np

def calculate_entropy(counts):
    """計算資訊熵"""
    probabilities = counts / counts.sum()
    return -np.sum(probabilities * np.log2(probabilities + 1e-10))

# 計算各組的熵值
for theme in ['love', 'work', 'control']:
    theme_counts = clean_df[clean_df['theme'] == theme]['card_cleaned'].value_counts()
    entropy = calculate_entropy(theme_counts)
    print(f"{theme} 組熵值: {entropy:.4f}")

# 理想均勻分佈的熵值
ideal_entropy = np.log2(22)
print(f"理想均勻分佈熵值: {ideal_entropy:.4f}")
```

## 🤝 貢獻與分享

### 分享您的結果

1. 在 [GitHub Issues](https://github.com/yourusername/repo/issues) 分享有趣發現
2. 提交改進的牌名對照規則
3. 分享不同語言或模型的實驗結果

### 擴展實驗

- 測試不同的 AI 模型（Claude, Gemini 等）
- 嘗試不同語言的提示詞
- 增加更多主題類別
- 測試不同的抽牌數量（單張、三張、十字牌陣等）

---

如有任何問題，歡迎透過 GitHub Issues 聯絡！

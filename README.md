**免責聲明**：
1. 本實驗僅供學術研究使用，不應被視為占卜或預測工具。
2. 原本這專案是用gemini2.5慢慢寫的，出於我已經忘記了我這個專案在做啥，我直接丟給cursor要他幫我整理了
3. 關於主要發現那邊，claude-4-sonnet寫法有誤，實際上「愛情、工作、控制組全部都沒有通過卡方檢定，akaCGPT抽牌不是隨機的」
4. 關於非程式這一類的實驗設計我很願意幫忙，但程式上的技術問題我完全幫不上
5. 聯絡方式：歡迎透過 threads 或 discord聯絡 https://portaly.cc/mercury_txt

# LLM 塔羅牌隨機性實驗

本專案是一個研究大型語言模型（LLM）在模擬塔羅牌抽牌時隨機性表現的實驗。通過讓 ChatGPT (GPT-4o) 在不同問題情境下模擬抽牌，我們發現 AI 的「隨機」行為會受到語意內容的強烈影響。

## 🎯 實驗目的

測試 AI 在以下三種情境下的抽牌行為：
- **愛情組**：「我想要問愛情。」
- **工作組**：「我想要問工作。」  
- **控制組**：「請為我抽一張牌。」

每組進行 250 次抽牌，觀察是否符合隨機分佈。

## 📊 主要發現

### 愛情組：極度偏差 🎭
- **戀人牌**出現 99.20% 的機率（理想值：4.55%）
- AI 幾乎總是選擇與問題語意相關的牌

### 工作組：中度偏差 💼  
- **命運之輪** 32% | **隱者** 23.2%
- 分佈較多樣，但仍有明顯偏向

### 控制組：相對平衡 ⚖️
- 最接近隨機分佈，但仍有輕微偏差
- **命運之輪** 18.8% | **隱者** 17.2%

## 🚀 快速開始

### 環境需求
- Python 3.8+
- OpenAI API 金鑰

### 安裝步驟

1. **複製專案**
```bash
git clone https://github.com/yourusername/llm-tarot-experiment.git
cd llm-tarot-experiment
```

2. **安裝依賴**
```bash
pip install -r requirements.txt
```

3. **設定 API 金鑰**
```bash
# 複製環境變數範本
cp env.example .env

# 編輯 .env 檔案，填入您的 OpenAI API 金鑰
# OPENAI_API_KEY=your_api_key_here
```

### 執行實驗

```bash
# 執行完整實驗（警告：將消耗約 750 次 API 呼叫）
python src/experiment.py

# 清洗數據
python src/data_cleaner.py

# 生成視覺化圖表
python src/visualizer.py
```

## 📁 專案結構

```
llm-tarot-experiment/
├── src/                    # 核心程式碼
│   ├── experiment.py       # 主要實驗程式
│   ├── config_maps.py      # 牌名對照表
│   ├── data_cleaner.py     # 資料清洗工具
│   └── visualizer.py       # 視覺化工具
├── examples/               # 範例結果
│   ├── sample_results.md   # 實驗結果摘要
│   ├── love_distribution.png    # 愛情組分佈圖
│   ├── work_distribution.png    # 工作組分佈圖
│   └── control_distribution.png # 控制組分佈圖
├── docs/                   # 文件
├── requirements.txt        # Python 依賴
├── env.example            # 環境變數範本
├── .gitignore             # Git 忽略檔案
└── README.md              # 本說明文件
```

## 🔧 自定義實驗

### 修改實驗參數

編輯 `src/experiment.py` 中的設定：

```python
# 每組抽牌次數
NUM_SAMPLES_PER_THEME = 250

# 測試主題
THEMES = {
    "work": "我想要問工作。",
    "love": "我想要問愛情。", 
    "control": "請為我抽一張牌。"
}

# AI 模型
MODEL_NAME = "gpt-4o"
```

### 新增牌名對照

在 `src/config_maps.py` 中的 `ALIAS_MAP` 新增對照規則：

```python
ALIAS_MAP = {
    "新的別名": "標準牌名",
    # ...
}
```

## 📈 結果分析

實驗結果將保存為：
- `tarot_experiment_results_YYYYMMDD.csv` - 原始數據
- `cleaned_tarot_results.csv` - 清洗後數據
- 各種視覺化圖表

## ⚠️ 注意事項

1. **API 費用**：完整實驗需要 750 次 API 呼叫，請注意費用
ps.這次的實驗大概花了0.04美元
2. **執行時間**：為避免觸發速率限制，每次呼叫間隔 1 秒
ps.要加速研究時間「好像」可以壓到0.2秒
3. **網路穩定**：實驗期間請確保網路連線穩定

## 🤝 貢獻指南

歡迎提交問題和改進建議！

1. Fork 此專案
2. 建立功能分支：`git checkout -b feature/your-feature`
3. 提交變更：`git commit -am 'Add some feature'`
4. 推送分支：`git push origin feature/your-feature`
5. 提交 Pull Request

## 📄 授權

本專案採用 MIT 授權條款 - 詳見 [LICENSE](LICENSE) 檔案

## 🙏 致謝

感謝 OpenAI 提供的 API 服務，以及所有對此研究感興趣的朋友們。



---


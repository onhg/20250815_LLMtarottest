# 貢獻指南

感謝您對 LLM 塔羅牌實驗專案的興趣！我們歡迎各種形式的貢獻。

## 🤝 如何貢獻

### 回報問題

如果您發現了 bug 或有改進建議：

1. 搜尋現有的 [Issues](https://github.com/yourusername/repo/issues) 確認問題尚未被回報
2. 建立新的 Issue，詳細描述：
   - 問題的重現步驟
   - 預期行為
   - 實際行為
   - 您的環境資訊（Python 版本、作業系統等）

### 提交程式碼

1. **Fork 專案**
   ```bash
   git clone https://github.com/yourusername/llm-tarot-experiment.git
   cd llm-tarot-experiment
   ```

2. **建立功能分支**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **進行變更**
   - 遵循現有的程式碼風格
   - 新增必要的註解
   - 確保程式碼可正常執行

4. **測試變更**
   ```bash
   # 執行基本測試
   python src/experiment.py --test-mode  # 如果有測試模式
   ```

5. **提交變更**
   ```bash
   git add .
   git commit -m "feat: 新增功能描述"
   git push origin feature/your-feature-name
   ```

6. **建立 Pull Request**
   - 詳細描述變更內容
   - 解釋為什麼需要這個變更
   - 如有相關 Issue，請引用

## 📝 程式碼風格

- 使用 Python PEP 8 標準
- 函式和類別需要適當的文檔字串
- 變數名稱使用有意義的英文或中文
- 在 `config_maps.py` 中新增註解說明牌名對照的來源

### 範例

```python
def calculate_distribution(data, theme):
    """
    計算特定主題的牌卡分佈
    
    Args:
        data (pd.DataFrame): 實驗數據
        theme (str): 主題名稱
        
    Returns:
        pd.Series: 牌卡分佈統計
    """
    theme_data = data[data['theme'] == theme]
    return theme_data['card_cleaned'].value_counts()
```

## 🎯 貢獻方向

### 高優先級
- 新增更多牌名對照規則
- 改善錯誤處理機制
- 新增不同語言的支援
- 效能最佳化

### 中優先級
- 新增統計分析功能
- 改善視覺化效果
- 新增更多 AI 模型支援
- 建立單元測試

### 低優先級
- 文件翻譯
- 範例擴充
- 介面美化

## 🧪 新增實驗類型

如果您想新增新的實驗類型：

1. 在 `THEMES` 字典中新增新主題
2. 確保提示詞清晰且一致
3. 考慮文化差異和語言特性
4. 提供預期結果的假設

### 範例：新增健康主題

```python
# 在 src/experiment.py 中
THEMES = {
    # 現有主題...
    "health": "我想要問健康。",
}
```

## 🌍 國際化支援

我們歡迎不同語言版本的貢獻：

- 英文提示詞版本
- 其他語言的塔羅牌名稱對照
- 多語言的 README

## 📊 數據貢獻

歡迎分享您的實驗結果：

1. 在 Issues 中分享有趣的發現
2. 提供不同模型的比較結果
3. 分享跨文化的實驗數據

### 數據格式要求

```csv
theme,run_number,card_drawn,model,language,timestamp
love,1,戀人,gpt-4o,zh-TW,2025-01-01T00:00:00
```

## 🔬 研究貢獻

如果您是研究者，歡迎：

- 提供統計分析方法
- 分享學術見解
- 協助設計更嚴謹的實驗
- 撰寫研究報告

## ❓ 問題解答

### Q: 我可以使用商業模型 API 嗎？
A: 可以，但請確保遵循各平台的使用條款。

### Q: 可以修改提示詞嗎？
A: 當然可以！我們鼓勵測試不同的提示詞策略。

### Q: 如何新增新的塔羅牌系統？
A: 修改 `STANDARD_NAMES` 常數，並相應更新對照表。

## 🙏 致謝

感謝所有貢獻者的付出！您的貢獻將被記錄在專案歷史中。

## 📧 聯絡方式

- GitHub Issues: 技術問題和 bug 回報
- Email: 研究合作和深度討論

---

讓我們一起探索 AI 的隨機性奧秘！ 🎴✨

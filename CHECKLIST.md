# 開源發布檢查清單 ✅

在正式發布此專案前，請確認以下項目：

## 🔒 安全性檢查

- [x] **移除 API 金鑰**: 確認沒有硬編碼的 API 金鑰
- [x] **環境變數設定**: 建立 `.env.example` 範本檔案
- [x] **敏感資訊**: 檢查是否有個人資訊或內部路徑

## 📁 檔案結構

- [x] **主要程式碼**: 移動到 `src/` 資料夾
- [x] **範例結果**: 整理到 `examples/` 資料夾  
- [x] **文件**: 放置在 `docs/` 資料夾
- [x] **測試檔案**: 保留在 `tests/` 資料夾（選擇性清理）

## 📝 文件完整性

- [x] **README.md**: 包含專案描述、安裝步驟、使用方法
- [x] **LICENSE**: MIT 授權條款
- [x] **CONTRIBUTING.md**: 貢獻指南
- [x] **使用指南**: 詳細的使用說明文件
- [x] **requirements.txt**: 完整的依賴清單

## 🛡️ 版本控制

- [x] **.gitignore**: 排除敏感檔案和不必要的檔案
- [ ] **清理歷史**: 確認 git 歷史中沒有敏感資訊
- [ ] **標籤版本**: 建議建立 v1.0.0 標籤

## 🧪 功能測試

建議在發布前進行以下測試：

### 基礎安裝測試
```bash
# 在新環境中測試
git clone <your-repo>
cd llm-tarot-experiment
pip install -r requirements.txt
```

### 設定測試
```bash
# 測試環境變數設定
cp env.example .env
# 編輯 .env 加入測試金鑰
```

### 功能測試
```bash
# 測試小規模實驗（避免大量 API 費用）
# 可以暫時修改 NUM_SAMPLES_PER_THEME = 5
python src/experiment.py
python src/data_cleaner.py  
python src/visualizer.py
```

## 📋 可選清理項目

### 建議保留
- `tests/` 資料夾 - 可供開發者參考
- `result/` 資料夾 - 展示完整實驗數據

### 建議移除
- [ ] `tests/__pycache__/` - Python 編譯快取
- [ ] 重複的 CSV 檔案
- [ ] 暫時性測試檔案

### 清理指令
```bash
# 移除 Python 快取
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -name "*.pyc" -delete

# 移除重複檔案（小心執行）
# rm tests/config_maps.py  # 已複製到 src/
# rm tests/data_washer.py  # 已複製到 src/data_cleaner.py
```

## 🌐 GitHub 發布準備

### Repository 設定
- [ ] **專案名稱**: 使用清楚的英文名稱，如 `llm-tarot-randomness-experiment`
- [ ] **描述**: "Research project analyzing randomness bias in LLM tarot card simulations"
- [ ] **主題標籤**: `llm`, `tarot`, `randomness`, `ai-bias`, `research`
- [ ] **可見性**: Public

### 發布資訊
- [ ] **Release Notes**: 撰寫 v1.0.0 發布說明
- [ ] **GitHub Pages**: 考慮是否啟用 Pages 展示結果
- [ ] **Issues Template**: 建立 Issue 範本

## 📊 範例 Release Notes

```markdown
# LLM Tarot Randomness Experiment v1.0.0

## 🎯 專案簡介
首次發布！本專案研究大型語言模型在模擬塔羅牌抽牌時的隨機性偏差。

## 🔥 主要特色
- 完整的實驗框架支援 GPT-4o
- 自動化數據清洗和視覺化
- 詳細的使用指南和貢獻規範

## 📈 關鍵發現  
- 愛情主題下 AI 偏向選擇「戀人」牌 (99.2%)
- 工作主題呈現中度偏差
- 控制組相對均勻但仍有偏好

## 🚀 快速開始
[詳見 README.md]

## 🐛 已知問題
- 字體設定在某些系統上可能需要調整
- API 費率限制可能影響大規模實驗

## 🤝 參與貢獻
歡迎提交 Issue 和 Pull Request！
```

## ✅ 最終確認

發布前的最後檢查：

- [ ] 所有敏感資訊已移除
- [ ] 文件連結和路徑都正確
- [ ] 在新環境中成功測試
- [ ] 授權條款符合預期
- [ ] GitHub repository 設定完成

---

**準備好了嗎？** 🚀

如果以上項目都已確認，您的專案就可以安全地開源了！

**重要提醒**: 發布後記得：
1. 定期更新依賴包版本
2. 回應社群的 Issues 和 PR
3. 考慮建立 Wiki 或更詳細的文件
4. 分享到相關的研究社群

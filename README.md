# chatGPTにメールの返答文を考えて貰うシステム(プロトタイプ)

## 動作
- [動作イメージ](https://twitter.com/kanhatakeyama/status/1640223616246878213)


## 利用法 
- ブラウザ用extension
  - webextensionをfirefoxやchromeにインストール
  - gpt.js内のURLを変更
- chatGPTの制御ページ(python)
  - key.pyにchatGPTのAPI_KEYを設定
  - ```streamlit run mail.py```

  - (本当はjavascriptだけで実装できるのですが、ちょっと詰まったので断念しました。)
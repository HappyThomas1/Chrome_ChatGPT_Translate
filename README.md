# Web Text Translation Extension
このChromeエクステンションは、ユーザーがウェブページ上のテキストを選択して、それを日本語に翻訳することができます。翻訳にはOpenAIのChatGPTもしくはDeepLを使用します。

## セットアップ
### 前提条件
- Python3がインストールされていること
- Flask, openai, flask_cors, deeplのPythonパッケージがインストールされていること
- Chromeブラウザがインストールされていること
- 環境変数にOpenAIおよびDeepLのAPIキーが設定されていること(`DEEPL_API_KEY`), (`OPENAI_API_KEY`)

### 手順
1. このリポジトリをクローンします。
2. Pythonのローカルサーバーを起動します。
```
   python3 <サーバースクリプトのパス>
```
3. Chromeで `chrome://extensions` にアクセスします。
4. 右上の「デベロッパーモード」を有効にします。
5. 「パッケージ化されていないアイテムを読み込む」をクリックし、エクステンションのディレクトリを選択します。

## 使い方
1. 翻訳したいテキストをウェブページ上で選択します。
2. 右クリックメニューから「Translate by ChatGPT」もしくは「Translate by DeepL」を選択します。
3. 新しいウィンドウが開き、そこに翻訳結果が表示されます。

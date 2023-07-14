# Web Text Translation Extension
このChromeエクステンションは、ユーザーがウェブページ上のテキストを選択して、それを日本語に翻訳することができます。翻訳にはOpenAIのChatGPTもしくはDeepLを使用します。

## セットアップ
### 前提条件
1. **Pythonのインストール**: Python3がまだインストールされていない場合は、[公式ウェブサイト](https://www.python.org/downloads/)からダウンロードしてインストールします。

2. **Pythonパッケージのインストール**: 以下のPythonパッケージが必要です。これらは次のコマンドをターミナルまたはコマンドプロンプトに入力することでインストールできます。ただし、このコマンドを実行する前にPythonがインストールされていることを確認してください。

    ```
    pip install Flask openai flask_cors deepl
    ```

3. **Chromeブラウザ**: もしまだインストールされていない場合は、Googleの[公式ウェブサイト](https://www.google.com/chrome/)からダウンロードしてインストールします。

4. **DeepL APIキーの設定**: DeepLのAPIキーを環境変数に設定する必要があります。これは次の手順で行うことができます。

    - DeepLの[公式ウェブサイト](https://www.deepl.com/pro#developer)でAPIキーを取得します（有料）。
    - 以下のコマンドをターミナルまたはコマンドプロンプトに入力して環境変数にAPIキーを設定します（`YOUR_DEEPL_API_KEY`は取得した実際のAPIキーに置き換えてください）。

        - Windowsの場合：
          ```
          setx DEEPL_API_KEY "YOUR_DEEPL_API_KEY"
          ```

        - macOSまたはLinuxの場合：
          ```
          export DEEPL_API_KEY="YOUR_DEEPL_API_KEY"
          ```

### 手順
1. このリポジトリをクローンします。または、ZIP形式でダウンロードして任意の場所に解凍します。

2. Pythonのローカルサーバーを起動します。ターミナルまたはコマンドプロンプトを開き、サーバースクリプトの存在するディレクトリに移動した上で次のコマンドを実行します。

   ```
   python3 ChatGPT_translation.py
   ```

3. Chromeで `chrome://extensions` にアクセスします。

4. 右上の「デベロッパーモード」を有効にします。

5. 「パッケージ化されていないアイテムを読み込む」をクリックし、エクステンションのディレクトリを選択します。

## 使い方
1. 翻訳したいテキストをウェブページ上で選択します。

2. 右クリックメニューから「Translate by ChatGPT」もしくは「Translate by DeepL」を選択します。

3. 新しいウィンドウが開き、そこに翻訳結果が表示されます。

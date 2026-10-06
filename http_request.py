# Python 標準ライブラリの HTTP 通信機能と例外を使用します。
import urllib.request
import urllib.error

# リクエストの送信先です。アクセスしたい URL に変更してください。
url = "https://github.com"

try:
    # GET は、指定した URL のページやデータを取得するメソッドです。
    # User-Agent ヘッダーで、リクエストを送信するクライアントを示します。
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Python HTTP Client"},
        method="GET",
    )

    # リクエストを送信します。タイムアウトは 30 秒です。
    # with を使うと、処理が終わったときにレスポンスが自動で閉じられます。
    with urllib.request.urlopen(request, timeout=30) as response:
        # 応答で指定された文字コードを使い、未指定の場合は UTF-8 を使います。
        charset = response.headers.get_content_charset() or "utf-8"
        # 本文をバイト列から文字列に変換します。
        # 変換できない文字は置換文字に置き換えます。
        body = response.read().decode(charset, errors="replace")

        # HTTP ステータス（例: 成功なら 200）と取得した本文を表示します。
        print("HTTP ステータス:", response.status)
        print("レスポンス本文:", body)

except urllib.error.HTTPError as error:
    # サーバーが 404 や 500 などの HTTP エラーを返した場合です。
    print("HTTP エラー:", error.code)
except urllib.error.URLError as error:
    # 接続失敗や名前解決の失敗など、通信に問題があった場合です。
    print("通信エラー:", error.reason)

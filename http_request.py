import urllib.request
import urllib.error

url = "https://github.com"

try:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Python HTTP Client"},
        method="GET",
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        body = response.read().decode(charset, errors="replace")

        print("HTTP ステータス:", response.status)
        print("レスポンス本文:", body)

except urllib.error.HTTPError as error:
    print("HTTP エラー:", error.code)
except urllib.error.URLError as error:
    print("通信エラー:", error.reason)

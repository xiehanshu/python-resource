import requests


def tryOrdos():
    url = 'https://ncthapi.ordostanpuhui.com:1443/security/login'
    data = {
        'loginName': 'admin',
        'password': 'b378ba69fb7bbaee64cfdf3fb55dd5ec',
        'type': 1
    }
    res = requests.post(url=url, json=data)
    print(res.json())
    token = res.json()['data']['token']

    headers = {
        'Token': token
    }

    url = 'https://ncthapi.ordostanpuhui.com:1443/statistics/getStatisticsInfo'

    res = requests.get(url=url, headers=headers)
    print(res.json())


if __name__ == '__main__':
    tryOrdos()

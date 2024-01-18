import requests


def req01():
    url = 'http://localhost:3000/sample/api05'
    params = {
        'a': 1,
        'b': 2,
        'key01': 'value01'
    }
    res = requests.get(url=url, params=params)
    print(res.json())
    print(res.status_code)
    res01 = requests.get(url=url, data=params)
    print(res01.json())
    print(res.status_code)


def req02():
    url = 'http://localhost:3000/sample/api03'
    data = {
        'a': 1,
        'b': 2
    }
    res = requests.post(url=url, data=data)
    print(res.text)
    print(res.status_code)


if __name__ == '__main__':
    req01()
    # req02()

import requests


def req01():
    url = 'http://localhost:3000/sample/api02'
    params = {
        'a': 1,
        'b': 2
    }
    res = requests.get(url=url, params=params)
    print(res.text)
    res01 = requests.get(url=url, data=params)
    print(res.text)


if __name__ == '__main__':
    req01()

import requests


def getParam(url, data):
    res = requests.get(url=url, params=data)
    print(res.text)
    print(res.status_code)


def getData(url, data):
    res = requests.get(url=url, data=data)
    print(res.text)
    print(res.status_code)


def postData(url, data):
    res = requests.post(url=url, data=data)
    print(res.text)
    print(res.status_code)


def getRoute(url, *args):
    url = url.format(args[0], args[1])
    res = requests.get(url=url)
    print(res.text)
    print(res.status_code)


if __name__ == '__main__':
    url = 'http://localhost:3000/user/get01'
    data = {
        "name": "xiehanshu",
        "age": "111"
    }
    getData(url, data)

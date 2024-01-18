import requests


def upload_file(api_url, app_id, access_token, file_path):
    request_url = f"{api_url}/tenant/upload/{app_id}"
    headers = {"access_token": access_token}
    with open(file_path, 'rb') as f:
        files = {"file": ('baiduMap.20240115-bike.csv', f)}
        response = requests.post(request_url, headers=headers, files=files)
        return response


if __name__ == '__main__':
    api_url = "https://accepter.lvpuhui.com"
    app_id = "8"
    access_token = "XwtvfDsp+xkGfuo49eAPGC+hzEpRN0pHHxHYorW6NoQbynuBeTFxEiGDLTT/KopuRi5C8Dg631kVSNTKPUcwgFb/ISWpYSekZD3ob6xtS6g15UQ3KbOMcB+alILElHLiI2Au5A/8MQzf6R1zVPaZ6W05963GYkUbYTYPxT3cfhRbz2dDGnzf+goGxpa3uy8Pzl9c6XtXCul8kNNpXkqn1bBv4Ggh6FgULC6flcHMVypLLNjXHMZ8YtEHzv6nodBdvjgOMLxLNSzLWrmrJa7JtWlQK5HIkHeN7sdKxhJdLkC5EyOaoyl8Rzac31/14Z8k7ksALjbUqv0="
    file_path = 'C:\\Users\\admin\\Desktop\\baiduMap.20240115-bike.csv'
    response = upload_file(api_url, app_id, access_token, file_path)
    print(response.content.decode())

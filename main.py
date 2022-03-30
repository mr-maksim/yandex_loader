import os
import config
import requests


class Uploader:
    def __init__(self, token: str):
        self.token = token

    def _get_link(self, file_path, name):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': self.token
        }
        params = {
            'path': f'{file_path}/{name}',
            'overwrite': 'true'
        }
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path, name):
        dict = self._get_link(file_path='uploader', name=name)
        href = dict['href']
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Uploaded')


if __name__ == '__main__':
    path_to_file = config.uploads_list()
    token = config.TOKEN
    uploader = Uploader(token)
    for item in path_to_file:
        name = os.path.basename(item)
        uploader.upload(item, name)

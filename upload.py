import requests
import OAuth_Key

def up_file(path_file):
    URL = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'

    params = {
        'path': f'netology/{path_file[13:]}'
    }
    headers = {'Authorization': f'OAuth {OAuth_Key.getOAuth()}',
               'Accept': 'application/json'}
    res = requests.get(URL, params=params, headers=headers)
    URL = res.json()['href']
    with open(path_file, 'rb') as d_file:
        data = d_file.read()
        res = requests.put(URL, data=data)
        print(f'Файл: {path_file} скопирован на Яндекс.Диск {res}\n')


if __name__ == '__main__':
    path = 'result_files/translate_de_ru.txt'
    up_file(path)

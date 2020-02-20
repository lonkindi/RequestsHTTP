import requests
import os
import upload

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(path_source, path_result, from_lang, to_lang='ru'):
    with open(path_source, encoding='utf-8') as file_s:
        text_s = file_s.read()
    params = {
        'key': API_KEY,
        'text': text_s,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }
    response = requests.get(URL, params=params)
    json_ = response.json()
    text_r = ''.join(json_['text'])

    with open(path_result, 'w', encoding='utf-8') as file_r:
        file_r.write(text_r)
        print(f'Файл : {path_source} переведён.\nРезультат перевода записан в : {path_result}\n')
        # upload.up_file(path_result)


if __name__ == '__main__':
    trnsl_to = 'ru'
    file_list = os.listdir('source_files')
    for file in file_list:
        s_file_name = file
        s_full_path = os.path.join('source_files', s_file_name)
        trnsl_from = file[0:2].lower()
        r_file_name = f'translate_{trnsl_from}_{trnsl_to}.txt'
        r_full_path = os.path.join('result_files', r_file_name)
        translate_it(s_full_path, r_full_path, trnsl_from, trnsl_to)

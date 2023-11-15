import requests

url_list = [
    'https://www.myauto.ge/ka/pr/97040958/iyideba-manqanebi-sedani-bmw-540-2017-benzini-batumi?offerType=superVip',
    'https://www.myauto.ge/ka/pr/97623410/iyideba-manqanebi-jipi-lexus-rx-450-2022-hibridi-tbilisi?offerType=superVip',
    'https://www.myauto.ge/ka/pr/97904774/iyideba-manqanebi-jipi-mercedes-benz-glb-35-amg-2023-benzini-tbilisi?offerType=superVip',
    'https://www.myauto.ge/ka/pr/98623538/iyideba-jipi-hyundai-santa-fe-2019-benzini-rustavis-avtobazroba?offerType=basic',
    'https://www.myauto.ge/ka/pr/98623530/iyideba-sedani-ford-escape-2019-benzini-gzashi-sak.-sken?offerType=basic'
]

for links in url_list:
    print('start')
    requests.post(f'http://127.0.0.1:5000/api/product/{links}')
    print('done')
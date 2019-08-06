import requests
import json
import codecs
from pathlib import Path

path = Path.cwd()
absolute = (str(path))
data = requests.get('https://pokeapi.co/api/v2/pokemon')
print(data.json())
j_data = data.json()


with open(absolute + '/python-api/data.json', 'w', encoding='utf-8') as f:
    json.dump(j_data, f, ensure_ascii=False, indent=4)
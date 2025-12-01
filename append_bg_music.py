# adds the list of sounds from story_variables.json to config.toml to selectively download only relevant sounds
from pathlib import Path
import json,time,requests,re
import toml

def remove_redundant(text: str) -> str:
    redundant_list = ['.mp3', '_intro', '_loop']
    for pattern in redundant_list:
        if pattern in text:
            text = text.replace(pattern, '')
    return text

with requests.get('https://raw.githubusercontent.com/KakkoiiSaber/arknights_story_data/main/assets/zh_CN/audio_table.json') as r:
    audio_table = r.json()

music_list = []
for key, value in audio_table.items():
    if value['intro'] is not None:
        music_list.append(remove_redundant(value['intro']))
    if value['loop'] is not None:
        music_list.append(remove_redundant(value['loop']))


with open('config.toml', 'r') as file:
    data = toml.load(file)
data['path_whitelist'] += [path for path in music_list]
data['path_whitelist'] = list(set(data['path_whitelist']))
with open('config.toml', 'w') as file:
    toml.dump(data, file)

# adds the list of sounds from story_variables.json to config.toml to selectively download only relevant sounds
from pathlib import Path
import json,time,requests,re
import toml

with requests.get('https://raw.githubusercontent.com/KakkoiiSaber/arknights_story_data/main/assets/cn/audio_table.json') as r:
    audio_table = r.json()

music_list = []
for key, value in audio_table.items():
    if value['intro'] is not None:
        music_list.append(value['intro'].replace('.mp3', ''))
    if value['loop'] is not None:
        music_list.append(value['loop'].replace('.mp3', ''))


with open('config.toml', 'r') as file:
    data = toml.load(file)
data['path_whitelist'] += [path for path in music_list]
data['path_whitelist'] = list(set(data['path_whitelist']))
with open('config.toml', 'w') as file:
    toml.dump(data, file)

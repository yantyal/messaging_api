# english.jsonにdataを入力

import json

data = dict()
with open('english.json', mode='rt', encoding='utf-8') as file:
  data = json.load(file)

word = input('word:')
sentence = input('sentence:')

data['items'].append(dict(word=word, sentence=sentence))

with open('english.json', mode='wt', encoding='utf-8') as file:
  json.dump(data, file, ensure_ascii=False, indent=2)
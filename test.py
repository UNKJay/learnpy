import json

obj = dict(name='pkj', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
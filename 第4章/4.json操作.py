import json

s = {
    "name": "二货",
    "age": 11,
    "gender": "female",
    "hobby": [
        "drawing",
        "swimming",
        "reading"
    ]
}

with open("json.json", "w", encoding="utf-8") as f:
    # 序列化
    json.dump(s, f, ensure_ascii=False, indent=2)

with open("json.json", "r", encoding="utf-8") as f:
    # 反序列化
    obj = json.load(f)
    print(f"类型：{type(s)}")
    print(obj)
    print(type(obj))
    parsed = json.dumps(obj, ensure_ascii=False, indent=2)
    print(parsed)
    print(type(parsed))

import csv

with open("test.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, ["name", "age", "gender"])
    writer.writeheader()
    writer.writerow({"name": "二货", "age": 11, "gender": "female"})
    writer.writerow({"name": "二货2", "age": 12, "gender": "male"})

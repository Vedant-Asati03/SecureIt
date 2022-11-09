import json

json_dump = json.dumps({"hi":"bye"}, indent=4)

with open("sample.json", "w", encoding="UTF-8") as outfile:
    outfile.write(json_dump)

with open("sample.json", "r", encoding="UTF-8") as outfile:
    print(json.load(outfile["hi"]))

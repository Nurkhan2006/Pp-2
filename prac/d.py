import json

sample_data = {"message": "Hello, JSON!"}

with open("sample-data.json", "w") as openfile:
    json.dump(sample_data, openfile)

print("Файл sample-data.json создан.")

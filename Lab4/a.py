import json  # <-- Добавь это

file_path = r"C:\Users\Hp\OneDrive\Рабочий стол\Pp-2\Lab4\sample-data.json"

with open(file_path, "r") as openfile:
    data = json.load(openfile)  # Теперь json импортирован, и всё должно работать

print(data)

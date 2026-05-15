import json

with open('tasks.json', 'r', encoding='utf-8') as f:
    tasks = json.load(f)

# Преобразуем строки в словари
new_tasks = []
for task in tasks:
    if isinstance(task, str):
        new_tasks.append({'text': task, 'date': '2026-05-15'})
    else:
        new_tasks.append(task)

with open('tasks.json', 'w', encoding='utf-8') as f:
    json.dump(new_tasks, f, ensure_ascii=False, indent=2)

print("Миграция завершена!")
from flask import Flask, render_template, request, redirect
import json
import os
from datetime import datetime # Для задания №3

app = Flask(__name__)
FILE_NAME = 'tasks.json'

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

tasks = load_tasks()

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_text = request.form['task']
    if task_text:
        # Задание №3: Добавляем дату создания
        new_task = {
            'text': task_text,
            'date': datetime.now().strftime("%d.%m.%Y %H:%M")
        }
        tasks.append(new_task)
        save_tasks(tasks)
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
    return redirect('/')

# Задание №1: Кнопка "Очистить всё"
@app.route('/clear')
def clear_all():
    tasks.clear()
    save_tasks(tasks)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, jsonify
from datetime import datetime
import pandas as pd

app = Flask(__name__)

def read_schedule(file_path):
    # Считываем данные из файла Excel
    df = pd.read_excel(file_path, engine='openpyxl')

    # Определение текущего дня недели
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    today = days[datetime.now().weekday()]
    
    # Подготовка данных для текущего дня
    day_column = today
    time_column = "Время" if today == "Понедельник" else f"Время.{days.index(today)}"
    schedule_today = df[[day_column, time_column]]
    
    # Переименовываем столбцы для унификации
    schedule_today.columns = ['Предмет', 'Время']
    
    # Возвращаем данные за текущий день
    return schedule_today

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule')
def schedule():
    data = read_schedule('C:\\Users\\d.ivanov\\Documents\\shedule.xlsx')
    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)

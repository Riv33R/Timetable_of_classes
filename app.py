from flask import Flask, render_template, jsonify
import pandas as pd
import threading
import time

app = Flask(__name__)

# Путь к файлу Excel
EXCEL_FILE_PATH = "C:\\Users\\d.ivanov\\Documents\\shedule.xlsx"

# Глобальная переменная для хранения данных о расписании
schedule_data = None


def read_schedule(file_path):
    # Считываем данные из файла Excel
    df = pd.read_excel(file_path, engine="openpyxl")

    # Подготовка данных для каждого дня недели
    days = [
        "Понедельник",
        "Вторник",
        "Среда",
        "Четверг",
        "Пятница",
        "Суббота",
    ]
    week_schedule = {}
    for index, day in enumerate(days):
        day_column = day
        time_column = "Время" if index == 0 else f"Время.{index}"
        day_schedule = df[[day_column, time_column]].dropna()
        day_schedule.columns = ["Предмет", "Время"]
        week_schedule[day] = day_schedule.to_dict(
            orient="records"
        )  # Преобразуем DataFrame в список словарей

    return week_schedule


def update_schedule():
    """Обновляет глобальную переменную с данными расписания."""
    global schedule_data
    schedule_data = read_schedule(EXCEL_FILE_PATH)
    print("Schedule updated at", time.ctime())  # Логгирование времени обновления


def schedule_reader():
    """Функция, которая вызывает update_schedule() каждую минуту."""
    update_schedule()
    threading.Timer(60, schedule_reader).start()  # Запускает себя каждую минуту


@app.route("/")
def index():
    """Отображает главную страницу."""
    return render_template("index.html")


@app.route("/schedule")
def schedule():
    """Возвращает текущее расписание в формате JSON."""
    global schedule_data
    if schedule_data is None:
        update_schedule()  # Первоначальное чтение при запуске приложения
    return jsonify(schedule_data)


if __name__ == "__main__":
    schedule_reader()  # Запуск фонового процесса обновления данных
    app.run(host='0.0.0.0', port=5001, debug=False)

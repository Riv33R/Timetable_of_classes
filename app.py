from flask import Flask, render_template, jsonify
from datetime import datetime
import pandas as pd

app = Flask(__name__)


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
        "Воскресенье",
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


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/schedule")
def schedule():
    data = read_schedule("C:\\Users\\d.ivanov\\Documents\\shedule.xlsx")
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, jsonify
from datetime import date
import pandas as pd

app = Flask(__name__)

def read_schedule(file_path):
    # Считываем данные из файла Excel
    df = pd.read_excel(file_path, engine='openpyxl')
    # Преобразуем даты в строковый формат для удобства сравнения
    df['Дата'] = pd.to_datetime(df['Дата']).dt.date
    # Возвращаем данные за текущий день
    return df[df['Дата'] == date.today()]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule')
def schedule():
    data = read_schedule('path_to_your_excel_file.xlsx')
    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)

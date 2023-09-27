from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = '79B834609EB62400'

@app.route('/')
def index():
    table_1_data = {
        'A1': 41,
        'A2': 18,
        'A3': 21,
        'A4': 63,
        'A5': 2,
        'A6': 53,
        'A7': 5,
        'A8': 57,
        'A9': 60,
        'A10': 93,
        'A11': 28,
        'A12': 3,
        'A13': 90,
        'A14': 39,
        'A15': 80,
        'A16': 88,
        'A17': 49,
        'A18': 60,
        'A19': 26,
        'A20': 28,
    }

    # Calculations for Table 2
    alpha_value = table_1_data['A5'] + table_1_data['A20']
    beta_value = table_1_data['A15'] / table_1_data['A7']
    charlie_value = table_1_data['A13'] * table_1_data['A12']

    table_2_data = {
        'Alpha': alpha_value,
        'Beta': beta_value,
        'Charlie': charlie_value,
    }

    return render_template('index.html', table_1=table_1_data, table_2=table_2_data)

if __name__ == '__main__':
    app.run()

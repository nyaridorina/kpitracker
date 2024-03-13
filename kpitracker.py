from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_difference():
    difference = ''
    if request.method == 'POST':
        date_str = request.form.get('date')
        date_format = "%Y-%m-%d %H:%M:%S"
        provided_date = datetime.strptime(date_str, date_format)
        now = datetime.now()
        difference = now - provided_date
        difference = str(difference)

    return render_template('index.html', difference=difference)

if __name__ == '__main__':
    app.run(debug=True)

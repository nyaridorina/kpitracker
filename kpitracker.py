from flask import Flask, request, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_remaining_time():
    remaining_time_str = ''
    if request.method == 'POST':
        arrival_time_str = request.form.get('date')
        date_format = "%Y-%m-%d %H:%M:%S"
        arrival_time = datetime.strptime(arrival_time_str, date_format)
        response_limit = timedelta(hours=8)
        current_time = datetime.now()
        time_passed = current_time - arrival_time
        remaining_time = response_limit - time_passed
        remaining_hours = remaining_time.seconds // 3600
        remaining_minutes = (remaining_time.seconds // 60) % 60
        remaining_time_str = f"You have {remaining_hours} hours and {remaining_minutes} minutes remaining to respond."

    return render_template('index.html', remaining_time=remaining_time_str)

if __name__ == '__main__':
    app.run(debug=False)
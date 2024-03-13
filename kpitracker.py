from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

def calculate_countback_counter(input_date):
    # Define working hours
    start_time = datetime.strptime("2024-03-13 08:00:00", "%Y-%m-%d %H:%M:%S").time()
    end_time = datetime.strptime("2024-03-13 16:30:00", "%Y-%m-%d %H:%M:%S").time()

    # Convert input date to datetime object
    input_datetime = datetime.strptime(input_date, "%Y-%m-%d %H:%M:%S")

    # Initialize counter
    counter = 0

    while datetime.now() > input_datetime:
        # Check if it's a weekday and within working hours
        if input_datetime.weekday() < 5 and start_time <= input_datetime.time() <= end_time:
            counter += 1
        
        # Increase one day to the input date
        input_datetime += timedelta(days=1)

        # Set the time to the start of the working day if it falls outside working hours
        if input_datetime.time() < start_time:
            input_datetime = input_datetime.replace(hour=start_time.hour, minute=start_time.minute, second=start_time.second)

    return counter

@app.route("/calculate_countback_counter", methods=["POST"])
def calculate_countback_counter_route():
    input_date = request.json["input_date"]
    counter = calculate_countback_counter(input_date)
    return jsonify({"counter": counter})  # Return JSON response

if __name__ == "__main__":
    app.run(debug=False)  # Debug mode disabled

from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/calculate_countback_counter", methods=["POST"])
def calculate_countback_counter_route():
    input_date = request.json["input_date"]
    counter = calculate_countback_counter(input_date)
    return jsonify({"counter": counter})

def calculate_countback_counter(input_date):
    # Define working hours
start_time = datetime.strptime("2024-03-07 08:00:00", "%Y-%m-%d %H:%M:%S").time()
end_time = datetime.strptime("2024-03-07 16:30:00", "%Y-%m-%d %H:%M:%S").time()

    # Convert input date to datetime object
    input_datetime = datetime.strptime(input_date, "%Y-%m-%d %H:%M:%S")

    # Initialize counter
    counter = 0

    while input_datetime > datetime.now():
        # Check if it's a weekday and within working hours
        if input_datetime.weekday() < 5 and start_time <= input_datetime.time() <= end_time:
            counter += 1
        
        # Decrease one day from the input date
        input_datetime -= timedelta(days=1)

        # Set the time to the end of the working day if it falls outside working hours
        if input_datetime.time() > end_time:
            input_datetime = input_datetime.replace(hour=end_time.hour, minute=end_time.minute, second=end_time.second)

    return counter

if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode for development
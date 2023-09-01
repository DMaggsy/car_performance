import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('car_performance')

performance = SHEET.worksheet('cars')

data = performance.get_all_values()


print(data)

from flask import Flask, jsonify, request
import gspread
from google.oauth2.service_account import Credentials

app = Flask(__name__)

# Setup gspread
SCOPE = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('car_performance')
performance = SHEET.worksheet('cars')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search', methods=['POST'])
def search():
    criteria = request.json.get('criteria')
    value = request.json.get('value').upper()
    all_data = performance.get_all_records()

    results = [row for row in all_data if str(row[criteria]).upper() == value]
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)




SEARCH_PROMPT = "Searching for "


def search_by_make():
    print("Please enter the car make you wish to search for: ")
    car_make = input()
    car_make = car_make.upper()
    print(SEARCH_PROMPT + car_make + "...")
    for row in data:
        if row[0] == car_make:
            print(row)

def search_by_model():
    print("Please enter the car model you wish to search for: ")
    car_model = input()
    car_model = car_model.upper()
    print(SEARCH_PROMPT + car_model + "...")
    for row in data:
        if row[1] == car_model:
            print(row)

def search_by_year():
    print("Please enter the car year you wish to search for: ")
    car_year = input()
    car_year = car_year.upper()
    print(SEARCH_PROMPT + car_year + "...")
    for row in data:
        if row[2] == car_year:
            print(row)

def search_by_engine_size():
    print("Please enter the engine size you wish to search for: ")
    engine_size = input()
    engine_size = engine_size.upper()
    print(SEARCH_PROMPT + engine_size + "...")
    for row in data:
        if row[3] == engine_size:
            print(row)

def search_by_horsepower():
    print("Please enter the horsepower you wish to search for: ")
    horsepower = input()
    horsepower = horsepower.upper()
    print(SEARCH_PROMPT + horsepower + "...")
    for row in data:
        if row[4] == horsepower:
            print(row)

def search_by_torque():
    print("Please enter the torque you wish to search for: ")
    torque = input()
    torque = torque.upper()
    print(SEARCH_PROMPT + torque + "...")
    for row in data:
        if row[5] == torque:
            print(row)

def search_by_0_60_mph_time():
    print("Please enter the 0-60 MPH time you wish to search for: ")
    time = input()
    time = time.upper()
    print(SEARCH_PROMPT + time + "...")
    for row in data:
        if row[6] == time:
            print(row)

def search_by_price_range():
    print("Please enter the price range you wish to search for: ")
    price = input()
    price = price.upper()
    print(SEARCH_PROMPT + price + "...")
    for row in data:
        if row[7] == price:
            print(row)

def search_by_all_data():
    print("Here's all the data we have on file: ")
    for row in data:
        print(row)

def get_data_by_criteria(criteria, value):
    all_data = performance.get_all_records()
    return [row for row in all_data if str(row[criteria]) == value]

def main_menu():
    while True: 
        print("\nCar Performance Data Tool\n")
        print("Please select an option from the menu below:\n")
        print("A: Search by Car Make")
        print("B: Search by Car Model")
        print("C: Search by Car Year")
        print("D: Search by Car Engine Size")
        print("E: Search by Car Horsepower")
        print("F: Search by Car Torque")
        print("G: Search by 0-60 MPH Time")
        print("H: Search by Price Range")
        print("I: View All Data")
        print("Q: Quit")

choice = input("Enter your choice: ").upper()

if choice == 'A':
    search_by_make()
elif choice == 'B':
    search_by_model()
elif choice == 'C':
    search_by_year()
elif choice == 'D':
    search_by_engine_size()
elif choice == 'E':
    search_by_horsepower()
elif choice == 'F':
    search_by_torque()
elif choice == 'G':
    search_by_0_60_mph_time()
elif choice == 'H':
    search_by_price_range()
elif choice == 'I':
    search_by_all_data()
elif choice =='Q':
    print("Thank you for using the Car Performance Data Tool. Goodbye.")
else:
    print("Invalid choice. Please try again.")
    
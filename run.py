from flask import Flask, jsonify, request, render_template
import gspread
from google.oauth2.service_account import Credentials
from flask_cors import CORS  # Importing CORS

# Setting up the app
app = Flask(__name__)
CORS(app)  # Allowing all origins

# Initialize gspread
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




SEARCH_PROMPT = "Searching for "


def search_by_make(data):
    print("Please enter the car make you wish to search for: ")
    car_make = input()
    car_make = car_make.upper()
    print(SEARCH_PROMPT + car_make + "...")
    for row in data:
        if row[0] == car_make:
            print(row)

def search_by_model(data):
    print("Please enter the car model you wish to search for: ")
    car_model = input()
    car_model = car_model.upper()
    print(SEARCH_PROMPT + car_model + "...")
    for row in data:
        if row[1] == car_model:
            print(row)

def search_by_year(data):
    print("Please enter the car year you wish to search for: ")
    car_year = input()
    car_year = car_year.upper()
    print(SEARCH_PROMPT + car_year + "...")
    for row in data:
        if row[2] == car_year:
            print(row)

def search_by_engine_size(data):
    print("Please enter the engine size you wish to search for: ")
    engine_size = input()
    engine_size = engine_size.upper()
    print(SEARCH_PROMPT + engine_size + "...")
    for row in data:
        if row[3] == engine_size:
            print(row)

def search_by_horsepower(data):
    print("Please enter the horsepower you wish to search for: ")
    horsepower = input()
    horsepower = horsepower.upper()
    print(SEARCH_PROMPT + horsepower + "...")
    for row in data:
        if row[4] == horsepower:
            print(row)

def search_by_torque(data):
    print("Please enter the torque you wish to search for: ")
    torque = input()
    torque = torque.upper()
    print(SEARCH_PROMPT + torque + "...")
    for row in data:
        if row[5] == torque:
            print(row)

def search_by_0_60_mph_time(data):
    print("Please enter the 0-60 MPH time you wish to search for: ")
    time = input()
    time = time.upper()
    print(SEARCH_PROMPT + time + "...")
    for row in data:
        if row[6] == time:
            print(row)

def search_by_price_range(data):
    print("Please enter the price range you wish to search for: ")
    price = input()
    price = price.upper()
    print(SEARCH_PROMPT + price + "...")
    for row in data:
        if row[7] == price:
            print(row)

def search_by_all_data(data):
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

        all_data = performance.get_all_values()  # Fetch the data from Google Sheet

        if choice == "A":
            search_by_make(all_data)
        elif choice == "B":
            search_by_model(all_data)
        elif choice == "C":
            search_by_year(all_data)
        elif choice == "D":
            search_by_engine_size(all_data)
        elif choice == "E":
            search_by_horsepower(all_data)
        elif choice == "F":
            search_by_torque(all_data)
        elif choice == "G":
            search_by_0_60_mph_time(all_data)
        elif choice == "H":
            search_by_price_range(all_data)
        elif choice == "I":
            search_by_all_data(all_data)
        elif choice == "Q":
            print("Thank you for using the Car Performance Data Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

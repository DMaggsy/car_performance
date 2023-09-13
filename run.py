import gspread
from google.oauth2.service_account import Credentials

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


class Car:
    def __init__(self, data):
        self.make = data["Make"]
        self.model = data["Model"]
        self.year = data["Year"]
        self.engine_size = data["EngineSize"]
        self.horsepower = data["Horsepower"]
        self.torque = data["Torque"]
        self.time_0_60 = data["0-60MphTime"]
        self.price_range = data["PriceRange"]

    def __str__(self):
        return (f"Make: {self.make}, Model: {self.model}, Year: {self.year}, "
                f"Engine Size: {self.engine_size}, Horsepower: {self.horsepower}, "
                f"Torque: {self.torque}, 0-60 MPH Time: {self.time_0_60}, "
                f"Price Range: {self.price_range}")


def fetch_cars():
    all_data = performance.get_all_records()
    return [Car(data) for data in all_data]


def search(criteria, value, cars):
    matches = [car for car in cars if getattr(car, criteria).upper() == value.upper()]
    if matches:
        for match in matches:
            print(match)
    else:
        print(f"No records found for {criteria}: {value}")


def main_menu():
    cars = fetch_cars()
    
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

        criteria_map = {
            "A": "make",
            "B": "model",
            "C": "year",
            "D": "engine_size",
            "E": "horsepower",
            "F": "torque",
            "G": "time_0_60",
            "H": "price_range"
        }

        if choice in criteria_map:
            value = input(f"Enter {criteria_map[choice]}: ").upper()
            print(f"Searching for {criteria_map[choice]}: {value}...")
            search(criteria_map[choice], value, cars)
        elif choice == "I":
            for car in cars:
                print(car)
        elif choice == "Q":
            print("Thank you for using the Car Performance Data Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()

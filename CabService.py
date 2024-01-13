# Vehicle categories
vehicles = {
    "AC Cars": ["ACC1-HONDA", "ACC2-AUDI", "ACC3-HYUNDAI", "ACC4-BMW"],
    "Non-AC Cars": ["NACC1-SUZUKI", "NACC2-SUZUKI", "NACC3-TATA"],
    "AC Vans": ["ACV1-TOYOTA", "ACV2-TOYOTA", "ACV3-BENZ"],
    "Non-AC Vans": ["NACV1-TOYOTA", "NACV2-LANCER"],
    "Three Wheels": ["TW1-BAJAJ", "TW2-BAJAJ", "TW3-BAJAJ", "TW4-BAJAJ"],
    "Trucks": ["TRK1-TATA", "TRK2-MITSUBISHI"],
    "Lorries": ["LRY1-TATA", "LRY2-MITSUBISHI"],
    "Hired Vehicles": ["LRY3-TATA", "NACC4-BMW"]
}

# Global Functions
def print_message(message):
    print(">>>>" + message + "<<<<")

def back():
    x = input('''====================================
Enter (x) to Back : ''')
    if x == "x":
        main_menu()
    else:
        print("Invalid Input!!!")

def display_list(vehicle_list, category_name):
    print(f"====================================\nAvailable {category_name} List")
    for vehicle in vehicle_list:
        print(vehicle)
    print(back())

def release_vehicle(vehicle_name, category_list, hired_list):
    category_list.append(vehicle_name)
    hired_list.remove(vehicle_name)
    print_message("Vehicle Released Successfully")
    back()

def hire_vehicle(category_list, hired_list, category_name):
    for vehicle in category_list:
        print(vehicle)
    selected_vehicle = input(f"Enter {category_name} Name from List to Hire: ")
    category_list.remove(selected_vehicle)
    hired_list.append(selected_vehicle)
    print_message("Vehicle Hired Successfully")
    back()

def remove_vehicle(category_list, category_name):
    for vehicle in category_list:
        print(vehicle)
    selected_vehicle = input(f"Enter {category_name} Name from List to Remove: ")
    category_list.remove(selected_vehicle)
    print_message("Vehicle Removed Successfully")
    for vehicle in category_list:
        print(vehicle)
    back()

def add_vehicle(category_list, category_name):
    new_vehicle = input(f"Enter New {category_name} Name: ")
    category_list.append(new_vehicle)
    print_message("Vehicle Added Successfully")
    for vehicle in category_list:
        print(vehicle)
    back()

# Option 7: Hired Vehicles List
def see_hired_vehicles():
    display_list(vehicles["Hired Vehicles"], "Hired Vehicles")

# Option 6: Release Hired Vehicles
def release_hired_vehicles():
    display_list(vehicles["Hired Vehicles"], "Hired Vehicles")
    print("Enter (x) 2 Times to Back Menu")
    vehicle_name = input('Enter Vehicle Name from List to Release: ')
    
    print("Select a category to release the vehicle:")
    for i, category in enumerate(vehicles.keys()):
        print(f"({i + 1}) Release {vehicle_name} to {category}")
    
    selected_category = input('Enter a Choice: ')
    
    if selected_category in vehicles.keys():
        release_vehicle(vehicle_name, vehicles[selected_category], vehicles["Hired Vehicles"])
    elif selected_category == "x":
        main_menu()
    else:
        print("Invalid Input!!!")
        release_hired_vehicles()

# Option 5: Hire Vehicles
def hire_vehicles():
    print("===========================")
    print("       Hire a Vehicle      ")
    print("===========================")
    for i, category in enumerate(vehicles.keys()):
        print(f"({i + 1}) {category}")

    print("===========================")
    print("(x) Back to Menu")

    selected_category_index = input('Enter a Choice: ')

    if selected_category_index.isdigit():
        selected_category_index = int(selected_category_index)
        categories = list(vehicles.keys())
        
        if 1 <= selected_category_index <= len(categories):
            selected_category = categories[selected_category_index - 1]
            hire_vehicle(vehicles[selected_category], vehicles["Hired Vehicles"], selected_category)
        else:
            print("Invalid Input!!!")
            hire_vehicles()
    elif selected_category_index == "x":
        main_menu()
    else:
        print("Invalid Input!!!")
        hire_vehicles()

# Option 4: Remove Vehicles
def remove_vehicles():
    print("===========================")
    print("      Remove Vehicles      ")
    print("===========================")
    for i, category in enumerate(vehicles.keys()):
        print(f"({i + 1}) {category}")

    print("===========================")
    print("(x) Back to Menu")

    selected_category_index = input('Enter a Choice: ')

    if selected_category_index.isdigit():
        selected_category_index = int(selected_category_index)
        categories = list(vehicles.keys())
        
        if 1 <= selected_category_index <= len(categories):
            selected_category = categories[selected_category_index - 1]
            remove_vehicle(vehicles[selected_category], selected_category)
        else:
            print("Invalid Input!!!")
            remove_vehicles()
    elif selected_category_index == "x":
        main_menu()
    else:
        print("Invalid Input!!!")
        remove_vehicles()

# Option 3: Add Vehicles
def add_vehicles():
    print("===========================")
    print("      Add New Vehicles     ")
    print("===========================")
    for i, category in enumerate(vehicles.keys()):
        print(f"({i + 1}) {category}")

    print("===========================")
    print("(x) Back to Menu")

    selected_category_index = input('Enter a Choice: ')

    if selected_category_index.isdigit():
        selected_category_index = int(selected_category_index)
        categories = list(vehicles.keys())
        
        if 1 <= selected_category_index <= len(categories):
            selected_category = categories[selected_category_index - 1]
            add_vehicle(vehicles[selected_category], selected_category)
        else:
            print("Invalid Input!!!")
            add_vehicles()
    elif selected_category_index == "x":
        main_menu()
    else:
        print("Invalid Input!!!")
        add_vehicles()

# Option 2: See Available Vehicles
def available_vehicles():
    print("===========================")
    print("     Available Vehicles    ")
    print("===========================")
    for i, category in enumerate(vehicles.keys()):
        print(f"({i + 1}) {category}")

    print("===========================")
    print("(x) Back to Menu")

    selected_category_index = input('Enter a Choice: ')

    if selected_category_index.isdigit():
        selected_category_index = int(selected_category_index)
        categories = list(vehicles.keys())
        
        if 1 <= selected_category_index <= len(categories):
            selected_category = categories[selected_category_index - 1]
            display_list(vehicles[selected_category], f"Available {selected_category}")
        else:
            print("Invalid Input!!!")
            available_vehicles()
    elif selected_category_index == "x":
        main_menu()
    else:
        print("Invalid Input!!!")
        available_vehicles()

# Option 1: Vehicles Details
def details_of_vehicles():
    print("==================================================")
    print("                Vehicles Details                  ")
    print("==================================================")
    print("✔ Car | Passengers: 3 and 4 | Type: AC/ Non AC")
    print("✔ Van | Passengers: 6 and 8 | Type: AC/ Non AC")
    print("✔ Three Wheel | Passengers: 3")
    print("✔ Trucks | Size: 7 ft and 12 ft")
    print("✔ Lorry | Max Load - 2500kg and 3500kg")
    print("==================================================")
    input("Enter (x) to Go to Main Page:")

# Main Page
def main_menu():
    print("************************************")
    print("       Welcome to Cab Service       ")
    print("         BY Rensith Udara           ")
    print("************************************")
    print("Choice 1 - Vehicles Details")
    print("Choice 2 - See Available Vehicles")
    print("Choice 3 - Add Vehicles")
    print("Choice 4 - Remove Vehicles")
    print("Choice 5 - Hire a Vehicle")
    print("Choice 6 - Release Hired Vehicles")
    print("Choice 7 - See Hired Vehicles List")
    print("************************************")
    user_input = input('Enter a Choice Number: ')
    print("************************************")
    
    if user_input == "1":
        details_of_vehicles()
    elif user_input == "2":
        available_vehicles()
    elif user_input == "3":
        add_vehicles()
    elif user_input == "4":
        remove_vehicles()
    elif user_input == "5":
        hire_vehicles()
    elif user_input == "6":
        release_hired_vehicles()
    elif user_input == "7":
        see_hired_vehicles()
    else:
        print("Invalid Choice.... Please Try Again")

main_menu()

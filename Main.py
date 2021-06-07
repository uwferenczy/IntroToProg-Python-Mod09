# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# DFerenczy,6.6.2021,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules
import IOClasses as IO
import ProcessingClasses as PC

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts
listEmployee = PC.FileProcessor.read_data_from_file('EmployeeData.txt')

while True:
    # Show user a menu of options
    IO.EmployeeIO.print_menu_items()

    # Get user's menu option choice
    strChoice = IO.EmployeeIO.input_menu_options()

    # Show user current data in the list of employee objects
    if strChoice == '1':
        IO.EmployeeIO.print_current_list_items(listEmployee)
        IO.EmployeeIO.input_press_to_continue()

    # Let user add data to the list of employee objects
    elif strChoice == '2':
        try:
            listEmployee.append(IO.EmployeeIO.input_employee_data())
        except Exception as e:
            print('Employee data was not added.\n')
            print(e)

        IO.EmployeeIO.input_press_to_continue()

    # let user save current data to file
    elif strChoice == '3':
        try:
            PC.FileProcessor.save_data_to_file('EmployeeData.txt', listEmployee)
            print("Employee data was successfully saved to the file.")
        except Exception as e:
            print('File not saved.\n')
            print(e)

        IO.EmployeeIO.input_press_to_continue()

    # Let user exit program
    elif strChoice == '4':
        print("Goodbye!")
        break

    else:
        print("Please enter a valid number between 1 and 4")
    # Main Body of Script  ---------------------------------------------------- #

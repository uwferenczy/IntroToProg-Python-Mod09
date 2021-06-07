import DataClasses as DC
import ProcessingClasses as PC
import IOClasses as IO

listEmployee = PC.FileProcessor.read_data_from_file('EmployeeData.txt')
IO.EmployeeIO.print_current_list_items(listEmployee)
listEmployee.append(IO.EmployeeIO.input_employee_data())
IO.EmployeeIO.print_current_list_items(listEmployee)
listEmployee.append(IO.EmployeeIO.input_employee_data())
IO.EmployeeIO.print_current_list_items(listEmployee)
PC.FileProcessor.save_data_to_file('EmployeeData.txt', listEmployee)
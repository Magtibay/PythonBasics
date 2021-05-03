employee_file = open("writingToFiles\\employees.txt", "a")

# print(employee_file.readable())
# print(employee_file.read())

# print(employee_file.readline())
# for employee in employee_file.readlines():
    # print(employee)

employee_file.write("Toby - Human Resources")
employee_file.write("\nKelly - Customer Service")
employee_file.close()

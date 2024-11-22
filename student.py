import csv

# Function to add a student
def add_student(first_name, last_name, reg_no):
    with open('students.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([first_name, last_name, reg_no])

# Function to search for a student using reg_no
def search_student(reg_no):
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[2] == reg_no:  
                print(f"First_Name: {row[0]}, Last_Name: {row[1]}, Reg_No: {row[2]}")
                return
        print("Student not found!")

# Function to delete a student by first_name
def delete_student(first_name):
    rows = []
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    # Filter rows that do not match the first_name
    data = [row for row in rows if row and row[0] != first_name]

    # Write updated data back to the file
    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Main function to handle user input
def main():
    while True:
        print("\n1. Add Student")
        print("2. Search for a Student by Reg_No")
        print("3. Delete a Student by First_Name")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            first_name = input("Enter Student First Name: ").capitalize()
            last_name = input("Enter Student Last Name: ").capitalize()
            reg_no = input("Enter Student Reg No: ").capitalize()
            add_student(first_name, last_name, reg_no)
            print("Student added successfully!")

        elif choice == '2':
            reg_no = input("Enter Reg_No: ").capitalize()
            search_student(reg_no)

        elif choice == '3':
            first_name = input("Enter Student First Name to delete: ").capitalize()
            delete_student(first_name)
            print(f"Student with first name '{first_name}' deleted successfully!")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()

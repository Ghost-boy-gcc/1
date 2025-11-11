#Student Record System (Linked List) Implementation

class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None

class StudentSystem:
    def __init__(self):
        self.head = None

    def insert(self, roll, name, marks):
        new_node = Student(roll, name, marks)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print("Student record added.")

    def display(self):
        if self.head is None:
            print("No student records.")
            return
        current = self.head
        while current:
            print(f"Roll: {current.roll}, Name: {current.name}, Marks: {current.marks}")
            current = current.next

    def update(self, roll, new_name, new_marks):
        current = self.head
        while current:
            if current.roll == roll:
                current.name = new_name
                current.marks = new_marks
                print(f"Student record for roll no {roll} updated.")
                return
            current = current.next
        print("Student not found.")

    def search(self, roll):
        current = self.head
        while current:
            if current.roll == roll:
                print(f"Student Found -> Roll: {current.roll}, Name: {current.name}, Marks: {current.marks}")
                return current
            current = current.next
        print("Student record not found.")
        return None

    def sort_by_roll_number(self, ascending=True):
        if self.head is None:
            return
        
        # Simple bubble sort on linked list for demonstration
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current and current.next:
                # Compare and swap data if needed
                if (ascending and current.roll > current.next.roll) or \
                   (not ascending and current.roll < current.next.roll):
                    current.roll, current.next.roll = current.next.roll, current.roll
                    current.name, current.next.name = current.next.name, current.name
                    current.marks, current.next.marks = current.next.marks, current.marks
                    swapped = True
                current = current.next
        print("Student record sorted by roll number.")

# Menu for Student System
if __name__ == "__main__":
    system = StudentSystem()
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student")
        print("4. Search Student")
        print("5. Sort by Roll No")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            roll = int(input("Enter roll no: "))
            name = input("Enter name: ")
            marks = float(input("Enter marks: "))
            system.insert(roll, name, marks)
        elif choice == '2':
            system.display()
        elif choice == '3':
            roll = int(input("Enter roll no to be updated: "))
            name = input("Enter new name: ")
            marks = float(input("Enter new marks: "))
            system.update(roll, name, marks)
        elif choice == '4':
            roll = int(input("Enter roll no to search: "))
            system.search(roll)
        elif choice == '5':
            order = input("Sort in 'asc' or 'desc' order? ").lower()
            ascending = True if order == 'asc' else False
            system.sort_by_roll_number(ascending)
            system.display()
        elif choice == '6':
            print("Exiting Student Record Management System.")
            break
        else:
            print("Invalid choice. Try again.")
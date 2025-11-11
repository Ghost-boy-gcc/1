#Text Editor with Undo/Redo Implementation

class TextEditor:
    def __init__(self):
        self.document = ""
        self.undo_stack = []
        self.redo_stack = []
    
    def make_change(self, change):
        # When a new change is made, clear the redo stack
        self.undo_stack.append(self.document)
        self.document += change
        self.redo_stack.clear()
        print("Change made.")

    def undo_action(self):
        if not self.undo_stack:
            print("No more actions to undo.")
            return
        
        # Move current state to redo stack
        self.redo_stack.append(self.document)
        # Revert to previous state from undo stack
        self.document = self.undo_stack.pop()
        print("Undo performed.")

    def redo_action(self):
        if not self.redo_stack:
            print("No more actions to redo.")
            return

        # Move current state back to undo stack
        self.undo_stack.append(self.document)
        # Apply the redone state
        self.document = self.redo_stack.pop()
        print("Redo performed.")
        
    def display_state(self):
        print(f'Current Document State: "{self.document}"')

# Menu for the editor
if __name__ == "__main__":
    editor = TextEditor()
    while True:
        print("\n--- Text Editor ---")
        print("1. Make a change (add text)")
        print("2. Undo")
        print("3. Redo")
        print("4. Display Document State")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            text_to_add = input("Enter text to add: ")
            editor.make_change(text_to_add)
        elif choice == '2':
            editor.undo_action()
        elif choice == '3':
            editor.redo_action()
        elif choice == '4':
            editor.display_state()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
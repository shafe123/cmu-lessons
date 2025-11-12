import datetime
from io_utils import get_integer_input, get_date_input
import os

# from todo_list import TodoList
from ai_ppp_python_review_solutions import (
    TodoList,
)  # remove this when using code in todo_list.py


def display_loaded_lists(loaded_lists):
    list_names = list(loaded_lists.keys())
    print("\n--- Loaded To-Do Lists ---")
    if not list_names:
        print("No lists currently loaded.")
    else:
        for i, name in enumerate(list_names):
            print(f"[{i+1}] {name} ({len(loaded_lists[name].get_items())} items)")
    print("--------------------------")
    return list_names


def list_menu(todo_list, file_path):
    """Menu for interacting with a specific TodoList."""
    while True:
        print(todo_list)
        print("\n--- List Options ---")
        print("1. Add item")
        print("2. Remove item (by number)")
        print("3. Set item status (by number)")
        print("4. Save list to file")
        print("5. Go back to Main Menu")
        print("--------------------")

        choice = get_integer_input("Enter choice (1-5): ", 1, 5)
        if choice is None:
            continue

        if choice == 1:  # Add item
            task_name = input("Enter new task name: ").strip()
            # TODO: Do you want to check anything here?

            due_date = get_date_input("Enter due date (YYYY-MM-DD, default today): ")
            if due_date is None:
                due_date = datetime.date.today()

            todo_list.add_task(task_name, due_date)
            print(f"Task '{task_name}' added.")

        elif choice == 2:  # Remove item
            # TODO: What if the list is empty?

            max_index = len(todo_list.get_items())
            item_num = get_integer_input(
                f"Enter item number to remove (1-{max_index}): ", 1, max_index
            )
            todo_list.remove_task(item_num - 1)

        elif choice == 3:  # Set item status
            # TODO: What if the list is empty?

            max_index = len(todo_list.get_items())
            item_num = get_integer_input(
                f"Enter item number to update status (1-{max_index}): ", 1, max_index
            )

            print("Status options: [1] Complete, [2] Incomplete, [3] Toggle")
            status_choice = get_integer_input("Enter status choice (1-3): ", 1, 3)

            todo_list.mark_complete(item_num - 1, status_choice == 1)

        elif choice == 4:  # Save list
            save_path = (
                input(f"Enter filename to save (default: {file_path}): ") or file_path
            )
            todo_list.save_to_file(save_path)

        elif choice == 5:  # Go back
            break


def main_menu():
    """Main application loop."""
    # Dictionary to hold loaded lists, keyed by their unique name
    loaded_lists = {}

    # Simple default path for saving/loading lists
    DEFAULT_FILE_PATH = "todo_list.txt"

    print("--- Welcome to the To-Do List CLI ---")

    while True:
        list_names = display_loaded_lists(loaded_lists)
        num_lists = len(list_names)

        print("\n--- Main Menu ---")
        print("1. Select a list")
        print("2. Create a new list")
        print("3. Load a list from file")
        print("4. Remove a list from memory")
        print("5. Quit")
        print("-----------------")

        choice = get_integer_input("Enter choice (1-5): ", 1, 5)
        if choice is None:
            continue

        if choice == 1:  # Select a list
            if num_lists == 0:
                print("No lists available to select.")
                continue

            list_choice = get_integer_input(
                f"Enter the list number to select (1-{num_lists}): ", 1, num_lists
            )
            if list_choice is not None:
                selected_name = list_names[list_choice - 1]
                list_menu(loaded_lists[selected_name], DEFAULT_FILE_PATH)

        elif choice == 2:  # Create a new list
            new_name = input("Enter a unique name for the new list: ").strip()
            if not new_name:
                print("List name cannot be empty.")
                continue
            if new_name in loaded_lists:
                print(f"Error: List with name '{new_name}' already exists in memory.")
                continue

            loaded_lists[new_name] = TodoList(new_name)
            print(f"New list '{new_name}' created.")

        elif choice == 3:  # Load a list
            file_path = (
                input(
                    f"Enter the path/filename to load (default: {DEFAULT_FILE_PATH}): "
                )
                or DEFAULT_FILE_PATH
            )
            if not os.path.exists(file_path):
                print(f"Error: File '{file_path}' not found.")
                continue

            list_name = input(
                f"Enter a name for the loaded list (default: {os.path.basename(file_path).split('.')[0]}): "
            )
            if not list_name:
                list_name = os.path.basename(file_path).split(".")[0]

            if list_name in loaded_lists:
                print(
                    f"Error: List with name '{list_name}' already loaded. Remove it first."
                )
                continue

            try:
                new_list = TodoList(list_name)
                new_list.load_from_file(file_path)
                loaded_lists[list_name] = new_list
                print(f"List '{list_name}' loaded successfully.")
            except Exception as e:
                print(f"Error loading list from file: {e}")

        elif choice == 4:  # Remove a list
            if num_lists == 0:
                print("No lists loaded to remove.")
                continue

            remove_choice = get_integer_input(
                f"Enter the list number to remove from memory (1-{num_lists}): ",
                1,
                num_lists,
            )
            if remove_choice is not None:
                removed_name = list_names[remove_choice - 1]
                del loaded_lists[removed_name]
                print(f"List '{removed_name}' removed from memory.")

        elif choice == 5:  # Quit
            print("Exiting To-Do List CLI. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()

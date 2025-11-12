import datetime

from ai_ppp_python_review_solutions import write_todo_list, read_todo_list

# --- CODE TO COMPLETE: Todo Class ---
# The Todo class represents a single task.
# It should have a task name, a due date, and a completion status (all as private variables).
# You need to fill in the methods to manage these attributes.
# HINT: The main_cli.py file expects a `to_dict` method that returns a dictionary like:
# {'task': 'task name', 'date': datetime.date(2025, 1, 1), 'completed': False}
# Also, the __str__ method should format the output nicely.


class Todo:
    """
    Represents a single To-Do item. Stores task name, date, and completion status.
    """

    def __init__(
        self, task, date, completed=False
    ):  # what should the default value be?
        self.set_task(task)
        self.set_date(date)
        self.set_completed(completed)

    @classmethod
    def from_dict(cls, dictionary):
        return Todo(dictionary["task"], dictionary["data"], dictionary["completed"])

    def get_task(self):
        return self.__task

    def get_date(self):
        return self.__date

    def is_completed(self):
        return self.__completed

    def set_task(self, new_task):
        self.__task = new_task

    def set_date(self, new_date):
        self.__date = new_date

    def set_completed(self, status):
        self.__completed = status

    def toggle_completion(self):
        self.__completed = not self.__completed

    def to_dict(self):
        """
        Converts the Todo object to dictionary format with keys like:
        {'task': 'task name', 'date': datetime.date(2025, 1, 1), 'completed': False}
        """
        return {
            "task": self.get_task(),
            "date": self.get_date(),
            "completed": self.is_completed(),
        }

    def __str__(self):
        return f"{'x' if self.is_completed() else 'o'} {self.get_date().strftime('%Y-%m-%d')}: {self.get_task()}"


# --- CODE TO COMPLETE: TodoList Class ---
# The TodoList class manages a collection of Todo objects.
# This is the central hub for adding, removing, and updating tasks.
# It should store a list of Todo objects (private variable).


class TodoList:
    """
    Manages a collection of Todo objects for a specific list.
    """

    def __init__(self, name):
        self.set_name(name)
        self.set_items([])

    def get_name(self):
        return self.__name

    def get_items(self):
        return self.__items

    def set_name(self, new_name):
        self.__name = new_name

    def set_items(self, new_items):
        self.__items = new_items[:]

    def add_task(self, task_name, date):
        self.get_items().append(Todo(task_name, date))

    def remove_task(self, index):
        del self.get_items()[index]

    def mark_complete(
        self, index, status=True
    ):  # what might the default status be for mark complete?
        """Sets the completion status of a task by its 0-based index."""
        self.get_items()[index].set_completed(status)

    def save_to_file(self, file_path):
        """
        Use the functions implemented by another group (io_utils.py).
        """
        dicts = [item.to_dict() for item in self.get_items()]
        write_todo_list(file_path, dicts)

    def load_from_file(self, file_path):
        """
        Use the functions implemented by another group (io_utils.py).
        """
        dicts = read_todo_list(file_path)
        self.set_items([Todo.from_dict(item) for item in dicts])

    def __str__(self):
        """
        Returns a formatted string representing the list.
        """
        return f"{self.get_name()}:\n" + "\n".join(
            [f"{index} - {str(item)}" for index, item in enumerate(self.get_items())]
        )


# --- Example Use (for testing) ---
# Students should run this file directly to check their class implementations.
if __name__ == "__main__":
    print("--- Group 1: Testing Todo and TodoList classes ---")

    # The group should use this section to test their code.
    # For example:
    my_list = TodoList("My Test List")
    today = datetime.date.today()

    # Check if add_task works
    print("\nAdding tasks...")
    my_list.add_task("Test task 1", today)
    my_list.add_task("Test task 2", today)
    print(my_list)

    # Check if mark_complete works
    print("\nMarking task 1 as complete...")
    my_list.mark_complete(0)
    print(my_list)

    # Check to_dict method
    print("\nChecking to_dict output for the first item...")
    print(my_list.get_items()[0].to_dict())

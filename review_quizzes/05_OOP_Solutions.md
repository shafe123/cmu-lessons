# Python OOP Review Quiz: Comprehensive Asses

# Answer Key

## 1\. Multiple Choice Answers

| \# | Type | Answer |
| :---: | :---: | :---: |
| 1 | Concept | **B** |
| 2 | Concept | **B** |
| 3 | Concept | **C** |
| 4 | Concept | **C** |
| 5 | Concept | **C** |
| 6 | Concept | **C** |
| 7 | Concept | **A** |
| 8 | Concept | **B** |
| 9 | Concept | **D** |
| 10 | Concept | **C** |
| 11 | Error ID | **D** |
| 12 | Error ID | **C** |
| 13 | Error ID | **D** |
| 14 | Error ID | **B** |
| 15 | Error ID | **B** |
| 16 | Error ID | **A** |
| 17 | Error ID | **C** |
| 18 | Error ID | **C** |
| 19 | Error ID | **C** |
| 20 | Error ID | **B** |

-----

## 2\. Short Answer Conceptual Answers

1.  **Class vs. Object:** A **Class** is a blueprint/template defining structure and behavior. An **Object** is a specific, concrete instance of a class with its own state/data.
2.  **Attributes and Methods:** **Attributes** are the data (characteristics) of an object. **Methods** are the functions (behaviors) the object can perform. *Analogy:* A **Phone Class** has attributes like $\text{color}$ and $\text{screen\_size}$ and methods like $\text{call()}$ and $\text{text()}$.
3.  **Purpose of $\text{super()}$:** To allow a subclass to call a method or access an attribute defined in its parent class, usually within the subclass's own overriding method or $\text{\_\_init\_\_}$.
4.  **Method Overriding:** A child class redefining a method that is already defined in its parent class. Used to provide specialized, class-specific behavior for a common action.
5.  **Private Mechanism:** **Name mangling**. The attribute is named with a leading **double underscore ($\text{\_\_}$)**. Python internally renames the attribute to include the class name (e.g., $\text{\_\_attribute}$ becomes $\text{\_ClassName\_\_attribute}$), making external access difficult.
6.  **Liskov Substitution Principle (LSP):** Objects of a superclass should be replaceable with objects of its subclasses without breaking the application.
7.  **Dunder Methods:** Special methods with double underscores (e.g., $\text{\_\_init\_\_}$) that allow Python classes to interface with built-in language features and operators. Example for human-readable string: **$\text{\_\_str\_\_}$**.
8.  **Abstract Class:** A class that cannot be instantiated and typically requires subclasses to implement specific methods. The **$\text{abc}$** (Abstract Base Class) module is used to formally enforce this.
9.  **Advantages of OOP:** 1. **Modularity/Reusability** (classes can be reused easily). 2. **Maintainability** (encapsulation helps prevent unrelated code from being broken by changes).
10. **Multiple Inheritance:** A class inherits from **more than one** parent class. The potential issue is the **Diamond Problem**, where a method inherited from two different paths has an ambiguous implementation.

### Error Identification Explanations

11. **Error:** $\text{Example.method()}$: **$\text{TypeError}$**. An instance method is called directly on the *class* without an instance object. Instance methods require an object to be bound to the $\text{self}$ parameter.
12. **Error:** $\text{super().\_\_init\_\_(5)}$: **$\text{TypeError}$**. The parent class $\text{Base}$ does not define an explicit $\text{\_\_init\_\_}$, so it implicitly uses the default $\text{object.\_\_init\_\_}$, which takes no arguments (besides $\text{self}$). Calling it with $\text{5}$ is an error.
13. **Error/Unexpected Behavior:** When $\text{A.x}$ is changed to $\text{20}$, the single class attribute is updated. Since $\text{a.x}$ still references the class attribute, the calculation is $\text{20} + \text{20} = \text{40}$. The unexpected part is that changing the class attribute affected the instance's value.
14. **Error:** $\text{print(Item.new\_attr)}$: **$\text{AttributeError}$**. The code attempts to access a class attribute ($\text{new\_attr}$) that has not been defined on the $\text{Item}$ class.
15. **Error:** $\text{v.move}$: No error, but an **unexecuted method call**. The programmer intended to execute the method but forgot the parentheses ($\text{v.move()}$). This line prints the *method object* itself.
16. **Error:** $\text{c.get\_id()}$: **$\text{TypeError}$**. The child class $\text{C}$ **overrode** $\text{get\_id}$ but changed the signature to require an argument ($\text{arg}$). Calling it without the required argument causes a $\text{TypeError}$.
17. **Error:** $\text{b.size = b.size + "cm"}$: **$\text{TypeError}$**. The code attempts to mix types ($\text{int}$ and $\text{str}$) using the addition operator. You cannot add the integer value of $\text{b.size}$ ($\text{10}$) to the string $\text{"cm"}$.
18. **No Error (Conceptual):** $\text{print(c)}$ searches for $\text{\_\_str\_\_}$ first. Since $\text{Child}$ doesn't have $\text{\_\_str\_\_}$, it inherits it from $\text{Parent}$, resulting in the output $\text{'P'}$. The $\text{\_\_repr\_\_}$ method is only used if $\text{\_\_str\_\_}$ is absent.
19. **Error:** $\text{B(y=5)}$: **$\text{TypeError}$**. Class $\text{B}$ inherits $\text{\_\_init\_\_(self, x)}$ from $\text{A}$. The constructor call passes the keyword argument $\text{y=5}$, but $\text{\_\_init\_\_}$ expects a positional or keyword argument named $\text{x}$, causing a $\text{TypeError}$ for an unexpected argument.
20. **Error/Conceptual Issue:** **Ambiguity**. The $\text{Final}$ class inherits the $\text{feature()}$ method from *both* $\text{Mixin1}$ and $\text{Mixin2}$. Python resolves this using the **MRO** (Method Resolution Order), which in this case calls the method from the class listed first ($\text{Mixin1}$), potentially masking the intent or function of $\text{Mixin2}$.

-----

## 3\. Fill-in-the-Blank Answers

| \# | Question Type | Correct Answer |
| :---: | :---: | :---: |
| 1 | Conceptual | **Polymorphism** |
| 2 | Conceptual | **instances** |
| 3 | Code Completion | $\text{\_\_init\_\_}$ |
| 4 | Conceptual | **instantiate** (or *call*) |
| 5 | Conceptual | **underscore ($\text{\_}$)** |
| 6 | Conceptual | **Overriding** |
| 7 | Conceptual | **Encapsulation** |
| 8 | Conceptual | **Method Resolution Order** |
| 9 | Conceptual | **Object** |
| 10 | Conceptual | **getter/setter** (or *accessor/mutator*) |
| 11 | Code Completion | $\text{print(Data.value)}$ OR $\text{print(d.value)}$ |
| 12 | Code Completion | $\text{super().\_\_init\_\_(x)}$ |
| 13 | Code Completion | $\text{return self.\_secret}$ |
| 14 | Code Completion | $\text{print(i)}$ |
| 15 | Code Completion | $\text{self.name = name}$ |

-----

## 4\. Building Code Prompts Answer

```python
# Part 1: The Book Classes (Encapsulation and Inheritance)

class Book:
    # Prompt 1: Constructor with private attributes (double underscore)
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn

    # --- Getters (Prompt 2) ---
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    # --- Setters (Prompt 3) ---
    def set_title(self, new_title):
        self.__title = new_title

    def set_author(self, new_author):
        self.__author = new_author

    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn

    # Prompt 5 (Instance Method for Book)
    def get_details(self):
        # Access attributes using their getter methods
        return f"Title: {self.get_title()} by {self.get_author()}"


class Ebook(Book):
    # Prompt 4: Ebook Inheritance
    def __init__(self, title, author, isbn, file_size):
        # Call the parent's constructor
        super().__init__(title, author, isbn)
        self.__file_size = file_size  # Private attribute

    # --- Getter/Setter for file_size (Prompt 4) ---
    def get_file_size(self):
        return self.__file_size

    def set_file_size(self, size):
        self.__file_size = size

    # Prompt 5 (Polymorphism - Method Overriding)
    def get_details(self):
        # Use super() and access file_size via its getter method
        base_details = super().get_details()
        return f"{base_details} | File Size: {self.get_file_size()}MB"


# Part 2: The LibraryCatalog Class (Composition)

class LibraryCatalog:
    # Prompt 6: Constructor with private list
    def __init__(self):
        self.__books = []  # Private list instance attribute

    # Prompt 7: Getter for books list
    def get_books(self):
        return self.__books

    # Prompt 7: Composition method
    def add_item(self, item):
        # Expects a Book or Ebook object
        self.__books.append(item)

    # Prompt 8: Iteration Method
    def list_all_titles(self):
        print("--- Library Titles ---")
        # Iterate over the books using the getter method
        for book in self.get_books():
            # Access the book's title using its getter method
            print(book.get_title())
        print("----------------------")


# Part 3: Demonstration

# Prompt 9 (Object Creation & Mutators)
book_one = Book(
    title='Old Title',
    author='Original Author',
    isbn='999'
)

# Use the setter method (mutator) to change the title
book_one.set_title('New Title')

ebook_one = Ebook(
    title='Python Crash Course',
    author='Eric Matthes',
    isbn='978-1593279288',
    file_size=25
)
catalog = LibraryCatalog()

catalog.add_item(book_one)
catalog.add_item(ebook_one)

# Prompt 10 (Accessors & Method Call)
# Access author and isbn using their getter methods (accessors)
print(f"Book1 Author: {book_one.get_author()}")
print(f"Book1 ISBN: {book_one.get_isbn()}")

# Call list_all_titles()
catalog.list_all_titles()

print("\n--- Ebook Details (Polymorphism Demo) ---")
print(ebook_one.get_details())
```
# Python OOP Review Quiz: Coding Exercise Solutions

## 4. Building Code Prompts Answer

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

    # Prompt 7: Property for books list (getter/setter)
    @property
    def books(self):
        """Return the private list of books."""
        return self.__books

    @books.setter
    def books(self, new_books):
        """Replace the internal books list. Expects an iterable of Book/Ebook objects."""
        # Optionally validate type/contents here; keep minimal for the exercise
        self.__books = list(new_books)

    # Prompt 7: Composition method
    def add_item(self, item):
        # Expects a Book or Ebook object
        self.__books.append(item)

    # Prompt 8: Iteration Method
    def list_all_titles(self):
        print("--- Library Titles ---")
        # Iterate over the books using the property
        for book in self.books:
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

## Bonus: Music Catalog Example

```python
# Music catalog bonus implementation

class Song:
    """Represents a song with simple encapsulated attributes."""

    def __init__(self, artist, title, album, year):
        self.__artist = artist
        self.__title = title
        self.__album = album
        self.__year = year

    # Accessors (explicit getters as in the exercise)
    def get_artist(self):
        return self.__artist

    def get_title(self):
        return self.__title

    def get_album(self):
        return self.__album

    def get_year(self):
        return self.__year

    # Mutators (explicit setters)
    def set_artist(self, new_artist):
        self.__artist = new_artist

    def set_title(self, new_title):
        self.__title = new_title

    def set_album(self, new_album):
        self.__album = new_album

    def set_year(self, new_year):
        self.__year = new_year

    def get_details(self):
        return f"{self.get_title()} by {self.get_artist()} ({self.get_album()}, {self.get_year()})"


class MusicCatalog:
    """Collection of Song objects using a property-based API for the internal list."""

    def __init__(self):
        self.__songs = []

    @property
    def songs(self):
        return self.__songs

    @songs.setter
    def songs(self, new_songs):
        self.__songs = list(new_songs)

    def add_item(self, item):
        # Expect a Song object; keep it simple for the exercise
        self.__songs.append(item)

    def list_all_titles(self):
        print("--- Music Catalog Titles ---")
        for s in self.songs:
            print(s.get_title())
        print("----------------------------")

    def list_all_details(self):
        print("--- Music Catalog Details ---")
        for s in self.songs:
            print(s.get_details())
        print("------------------------------")


# Demo
song1 = Song("The Beatles", "Hey Jude", "Hey Jude", 1968)
song2 = Song("Nirvana", "Smells Like Teen Spirit", "Nevermind", 1991)
song3 = Song("Beyoncé", "Halo", "I Am... Sasha Fierce", 2008)

catalog = MusicCatalog()
catalog.add_item(song1)
catalog.add_item(song2)

# mutate a song title using the setter
song1.set_title("Hey Jude (Remastered)")

catalog.add_item(song3)

# Print outputs
catalog.list_all_titles()
print()
catalog.list_all_details()
```

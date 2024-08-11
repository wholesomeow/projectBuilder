# Table Of Contents
- [Python Reference](#python-reference)
  - [Common Items and Notes](#common-items-and-notes)
    - [Classes](#classes)
    - [Data Classes](#data-classes)
    - [List Comprehension](#list-comprehension)
    - [Decorators](#decorators)
  - [Basic File Structure](#basic-file-structure)
    - [Breakdown](#breakdown)
  - [Advanced File Structure](#advanced-file-structure)
    - [Breakdown](#breakdown-1)
  - [Google Style Guide](#google-style-guide)
    - [Module Comments](#module-comments)
    - [Test Module Comments](#test-module-comments)
    - [Class Comments](#class-comments)
    - [Function Comments](#function-comments)
  - [Writing and Running Tests](#writing-and-running-tests)
  - [Python Links](#links)


# Python Reference
This reference document contains a living list of items I find useful to have on hand, either because I don't know them off the top of my head or because they are complicated.

## Common Items and Notes
Running python in a seperate terminal requires the following syntax
```
python3 location/filename.py
```

### Classes
```
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)
```

### Data Classes
Similar to C-like structs, Python has Data Classes

```
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0


p = Point(1.5, 2.5)

print(p)  # Point(x=1.5, y=2.5, z=0.0)
```

### List Comprehension
The standard way of creating a list of items, in this case a list of squares vs creating that same list of squares with list comprehension.
A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.

Standard List implementation:
```
squares = []
for x in range(10):
  squares.append(x**2)

print(squares)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

List Comprehension:
```
squares = [x**2 for x in range(10)]

print(squares)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Decorators
Functions are just like any other object in Python and can be nested inside another function as an "Inner Function" or passed as a parameter as a "First-Class Object".
With this, a simple wrapper - or decorator - can be constructed.

See [Links](#links) for a list of built in python decorators

Simple Decorator
```
def decorator(func):
  def wrapper():
    print("Something is happening before the function is called.")
    func()
    print("Something is happening after the function is called.")
  return wrapper

def say_whee():
  print("Whee!")

say_whee = decorator(say_whee)

say_whee()

OUTPUT:
Something is happening before the function is called.
Whee!
Something is happening after the function is called.
```

By using the @ symbol, also called pie syntax, we can replace the last line above with something a little nicer looking.
The @ replaces the need to assign the decorator function to the function we want to wrap.

Decorator with Pie Syntax
```
def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator
def say_whee():
    print("Whee!")

say_whee()

OUTPUT:
Something is happening before the function is called.
Whee!
Something is happening after the function is called.
```

## Basic File Structure
```
ROOT/
├─ setup.py
├─ requirements.txt
├─ PROJECT_Name/
│  ├─ stubLib.py
│  ├─ stubClass.py
│  ├─ stubExecutable.py
├─ data/
├─ docs/
│  ├─ reference.md
├─ tests/
│  ├─ stubTest.py
├─ README.md
```

### Breakdown
- ROOT
  - This is the ROOT directory of the project, more than likely sharing the PROJECT_NAME
- setup.py
  - This is used for package and distribution management
  - Expand on this when package management becomes the subject of focus
- requirements.txt
  - A pip requirements file should be placed at the root of the repository that specifies the dependencies required to contribute to the project:
    - Testing
    - Building
    - Generating Documentation
  - This file may not be needed if there are no dependencies
- PROJECT_NAME
  - This is the module package sits and should be named appropriatly so there is no confusion as to it's purpose
  - stubLib.py
    - A stubbed out python library file, primed for building out a library for the rest of the module
  - stubClass.py
    - A stubbed out python class file, ready for a class or dataclass
  - stubExecutable.py
    - A stubbed out python exe file, ready to ingest the class, library, and/or other logic
- data
  - A directory to hold any data to be referenced in the rest of the module
  - Keeping it seperate from the logic ensures proper decoupling/modularity
- docs
  - Any documentation goes here. Theres no better place for it
- tests
  - The place where all your tests are ran from
  - Expand on this when testing becomings the subject of focus

## Advanced File Structure
Placeholder

### Breakdown
Placeholder

## Google Style Guide
Placeholder

### Module Comments
```
"""A one-line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""
```

### Test Module Comments
```
"""This blaze test uses golden files.

You can update those files by running
`blaze run //foo/bar:foo_test -- --update_golden_files` from the `google3`
directory.
"""
```

### Class Comments
This shows more than just the Class Comments, to give context to what is required and not required.
```
class SampleClass:
    """Summary of class here.

    Longer class information...
    Longer class information...

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam: bool = False):
        """Initializes the instance based on spam preference.

        Args:
          likes_spam: Defines if instance exhibits this preference.
        """
        self.likes_spam = likes_spam
        self.eggs = 0

    @property
    def butter_sticks(self) -> int:
        """The number of butter sticks we have."""
```

### Function Comments
Key take-away is to provide the following:
- Description
- Args
- Returns
- Raises

```
def fetch_smalltable_rows(
    table_handle: smalltable.Table,
    keys: Sequence[bytes | str],
    require_all_keys: bool = False,
) -> Mapping[bytes, tuple[str, ...]]:
    """Fetches rows from a Smalltable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by table_handle.  String keys will be UTF-8 encoded.

    Args:
        table_handle: An open smalltable.Table instance.
        keys: A sequence of strings representing the key of each table
          row to fetch.  String keys will be UTF-8 encoded.
        require_all_keys: If True only rows with values set for all keys will be
          returned.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {b'Serak': ('Rigel VII', 'Preparer'),
         b'Zim': ('Irk', 'Invader'),
         b'Lrrr': ('Omicron Persei 8', 'Emperor')}

        Returned keys are always bytes.  If a key from the keys argument is
        missing from the dictionary, then that row was not found in the
        table (and require_all_keys must have been False).

    Raises:
        IOError: An error occurred accessing the smalltable.
    """
```

## Writing and Running Tests
See [Links](#links) for documentation on testing with python

## Links
[Structuring Your Project](https://docs.python-guide.org/writing/structure/)
[Python Data Structures - More on Lists](https://docs.python.org/2/tutorial/datastructures.html)
[Primer on Python Decorators](https://realpython.com/primer-on-python-decorators)
[Built-In Python Decorators](https://wiki.python.org/moin/Decorators)
[Testing in Python](https://realpython.com/python-testing/)
[Google Python Style Guide](https://google.github.io/styleguide/pyguide.htm)
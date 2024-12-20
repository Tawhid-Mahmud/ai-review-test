# Basic variable assignments
name = "Alice"
age = 25
is_student = True
height = 1.75

# Basic data structures
# List
fruits = ["apple", "banana", "orange"]
fruits.append("mango")

# Dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Set
unique_numbers = {1, 2, 3, 3, 4, 4, 5}  # Duplicates are automatically removed

# Tuple (immutable)
coordinates = (10, 20)

# Basic function
def greet(name, greeting="Hello"):
    """
    A simple greeting function with a default parameter.
    """
    return f"{greeting}, {name}!"

# Function with type hints
def calculate_rectangle_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle."""
    return length * width

# List comprehension
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
even_numbers = [n for n in numbers if n % 2 == 0]

# Class definitionA
class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age 
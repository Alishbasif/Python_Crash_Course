# ============================================================
# Python Functions - Lecture
# Default Parameters and List Functions
# ============================================================


# ------------------------------------------------------------
# Default Parameters
# ------------------------------------------------------------

# A default parameter has a default value.
# If we do not provide a value during function call,
# Python uses the default value.

def cal_prod(b, a=6):
    product = a * b
    print("Product =", product)


# Function Call
cal_prod(4)


# ============================================================
# Practice Question - 1
# ============================================================

# Function to print the length of a list

cities = ["Karachi", "Lahore", "Islamabad", "Multan", "Faisalabad"]
numbers = [1, 4, 2, 9, 7, 3, 5]


def print_len(my_list):
    print("Length of list =", len(my_list))


# Function Call
print_len(numbers)


# ============================================================
# Practice Question - 2
# ============================================================

# Function to print all elements of a list

cities = ["Karachi", "Lahore", "Islamabad", "Multan", "Faisalabad"]
numbers = [1, 4, 2, 9, 7, 3, 5]


def print_elements(my_list):
    for item in my_list:
        print(item, end=" ")


# Function Call
print_elements(cities)
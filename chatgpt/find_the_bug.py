

# More use of "last letter"
def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    return sorted(strings, key=last_letter)

# Less use of "last letter"
def sort_by_last_letter(strings):
    return sorted(strings, key=lambda s: s[0])


# Playing with the scope
a = [2]
def f(a):
    a = [1]
f(a)
assert a == [2]

# documentation mismatches the code

# Take the square root of a number
def sqrt(x):
    """Return the square root of x."""
    return x ** 2

# Slow function that could be sped up
def get_first_letter(s):
    for i, c in reversed(s):
        if i == 0:
            return c


# No zero of gradients in function
output = model(input)
optimizer.zero_grad()
loss_fn.backward()
optimizer.step()


# What is the best string concatenation method?
first_name = "Foo"
last_name = "Bar"

# Method 1
full_name = first_name + " " + last_name

# Method 2
full_name = "{} {}".format(first_name, last_name)

# Method 3
full_name = f"{first_name} {last_name}"

# Method 4
full_name = " ".join([first_name, last_name])


# List fuckery
def add_to_list(x, l=[]):
    l.append(x)
    return l

# Sam Bankman Fraud
from dataclasses import dataclass

@dataclass
class FTXAccounts:
    customer: float = 0.0
    business: float = 0.0

    def deposit_into_customer(self, amount):
        self.customer += amount

    def withdraw_from_business(self, amount):
        self.customer -= amount


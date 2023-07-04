# Implicit Type Conversion
num_int = 10
num_float = 3.14

result = num_int + num_float  # int + float -> Python converts num_int to float
print(result)  # Output: 13.14


# Explicit Type Conversion
num_str = "42"
num_int = int(num_str)  # Convert string to integer
num_float = float(num_str)  # Convert string to float

print(num_int)  # Output: 42
print(num_float)  # Output: 42.0


# Explicit Type Conversion to Boolean
num = 10
is_greater_than_zero = bool(num)  # Convert integer to boolean

print(is_greater_than_zero)  # Output: True


# Type Conversion with str.format()
age = 25
name = "Alice"

message = "My name is {} and I am {} years old.".format(name, age)
print(message)  # Output: "My name is Alice and I am 25 years old."

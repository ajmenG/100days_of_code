len("12345") # ta fukncja działa tylko na stringi itp, jest to w dokumentacjach
print(type("12345"))
print(type(12345))
print(type(True))
print(type(1.5))

# type conversion

int("123") # it will convert 123 string into 123 number
float("12.5")
str(123)
print(bool(0))


name_of_the_user = input("Enter your name: ")
lenght_of_name = str(len(name_of_the_user))
print("Number of letters in your name: " + lenght_of_name)
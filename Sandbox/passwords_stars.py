MIN_LENGTH = 5

password = input("Enter password: ")
while len(password) < MIN_LENGTH:
    print(f"The password does not meet the minimum length of {MIN_LENGTH}")
    password = input("Enter password: ")
for i in range(1, len(password) + 1, 1):
    print("*", end="")
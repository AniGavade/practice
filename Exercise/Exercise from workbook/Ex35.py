# Dog year.

h_age = int(input("Enter a dog age in human years: "))
if h_age < 0:
    print("age must be positive number.")
    exit()
elif h_age <= 2:
    d_age = h_age * 10.5
else:
    d_age = 21 + (h_age - 2)*4
print("The dog's age in dog's years is", d_age)


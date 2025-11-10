number = int(input("Enter a number to see its multiplication table: "))
for nums in range(1, 11):
    Z = nums * number
    print(f"{number} * {nums} = {Z}")
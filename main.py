# if __name__ == '__main__':
def add_num(a, b):
    return a+b


def sub_num(a, b):
    return a-b


def mul_num(a, b):
    return a*b


def div_num(a, b):
    return a/b


print("Enter two numbers")


a1 = int(input())
a2 = int(input())

choice = input("1 - addition \n2 - subtraction \n3 - multiplication \n4 - division \n")
result = ""


if choice == "1":
    result = add_num(a1, a2)
elif choice == "2":
    result = sub_num(a1, a2)
elif choice == "3":
    result = mul_num(a1, a2)
elif choice == "4":
    result = div_num(a1, a2)
else:
    print("Enter valid option")

print(result)

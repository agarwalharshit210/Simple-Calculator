def add(a,b):
    return a+b

def Multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

def subtraction(a,b):
    return a-b

def main():
    print("----------------CALCULATOR-------------------------------")
    print()
    while True:
            print("1.ADD\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
            choice = int(input("Enter your Choice : "))

            sum = None
            
            if choice == 1:
                num1 = int(input("Enter the First Number : "))
                num2 = int(input("Enter the Second Number : "))
                sum = add(num1,num2)
                print()
                print(f"Addition of Two Number is {sum}")
                print()
            elif choice == 2:
                num1 = int(input("Enter the First Number : "))
                num2 = int(input("Enter the Second Number : "))
                sum = subtraction(num1, num2)
                print()
                print(f"Subtraction of Two Number is {sum}")
                print()
            elif choice == 3:
                num1 = int(input("Enter the First Number : "))
                num2 = int(input("Enter the Second Number : "))
                sum = Multiplication(num1,num2)
                print()
                print(f"Multiplication of Two Number is {sum}")
                print()
            elif choice == 4:
                num1 = int(input("Enter the First Number : "))
                num2 = int(input("Enter the Second Number : "))
                sum = division(num1,num2)
                print()
                print(f"Division of Two Number is {sum}")
                print()
            elif choice == 5:
                print("Thank you")
                break
            else:
                print("Invalid Choice?Please! enter the valid choice")

if __name__ == '__main__':
    main()
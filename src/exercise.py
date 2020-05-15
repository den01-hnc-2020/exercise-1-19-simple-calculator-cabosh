def main():
    #write your code below this line
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))

    add = num1 + num2
    subtract = num1 - num2
    multiply = num1 * num2
    divide = num1 / num2

    print(str(num1) + " + " + str(num2) + " = " + str(add))
    print(str(num1) + " - " + str(num2) + " = " + str(subtract))
    print(str(num1) + " * " + str(num2) + " = " + str(multiply))
    print(str(num1) + " / " + str(num2) + " = " + str(divide))

if __name__ == '__main__':
    main()

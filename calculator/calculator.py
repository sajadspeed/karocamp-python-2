
number1 = float(input("Number1: "))

oprator = input("Oprator (+ - / *): ")

number2 = float(input("Number2: "))

result = 0

if oprator == "+":
    result = number1 + number2
elif oprator == "-":
    result = number1 - number2
elif oprator == "*":
    result = number1 * number2
elif oprator == "/":
    if number2 != 0:
        result = number1 / number2
    else:
        print("NIMISHED")
else:
    print("Wrong command.")


print(f"{number1} {oprator} {number2} = {result}")
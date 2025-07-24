import math

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return "Error: Divide by zero" if b == 0 else a / b
def modulus(a, b): return a % b
def power(a, b): return a ** b
def square_root(a): return math.sqrt(a)

def area_circle(radius): return math.pi * radius ** 2
def area_rectangle(length, width): return length * width
def simple_interest(p, r, t): return (p * r * t) / 100
def bmi(weight, height): return weight / (height ** 2)
def c_to_f(c): return (c * 9/5) + 32
def f_to_c(f): return (f - 32) * 5/9

while True:
    print("\n📊 --- Smart Python Calculator ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (x^y)")
    print("7. Square Root (√x)")
    print("8. Area of Circle")
    print("9. Area of Rectangle")
    print("10. Simple Interest")
    print("11. BMI Calculator")
    print("12. Celsius to Fahrenheit")
    print("13. Fahrenheit to Celsius")
    print("14. Exit")

    choice = input("👉 Enter your choice (1-14): ")

    if choice == '14':
        print("Exiting... Thank you! ✨")
        break

    elif choice in ['1','2','3','4','5','6']:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if choice == '1': print("Result:", add(a, b))
        elif choice == '2': print("Result:", subtract(a, b))
        elif choice == '3': print("Result:", multiply(a, b))
        elif choice == '4': print("Result:", divide(a, b))
        elif choice == '5': print("Result:", modulus(a, b))
        elif choice == '6': print("Result:", power(a, b))

    elif choice == '7':
        a = float(input("Enter number: "))
        print("Square root:", square_root(a))

    elif choice == '8':
        r = float(input("Enter radius: "))
        print("Area of Circle:", area_circle(r))

    elif choice == '9':
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print("Area of Rectangle:", area_rectangle(l, w))

    elif choice == '10':
        p = float(input("Enter principal amount: "))
        r = float(input("Enter rate of interest: "))
        t = float(input("Enter time (years): "))
        print("Simple Interest:", simple_interest(p, r, t))

    elif choice == '11':
        w = float(input("Enter weight (kg): "))
        h = float(input("Enter height (m): "))
        print("BMI:", round(bmi(w, h), 2))

    elif choice == '12':
        c = float(input("Enter temperature in Celsius: "))
        print("Fahrenheit:", c_to_f(c))

    elif choice == '13':
        f = float(input("Enter temperature in Fahrenheit: "))
        print("Celsius:", f_to_c(f))

    else:
        print("❌ Invalid choice. Try again.")

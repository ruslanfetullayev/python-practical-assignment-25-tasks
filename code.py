#Task 1

a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
if a>b:
    print(f"{a} is greater than {b}")
elif a<b:
    print(f"{b} is greater than {a}")
else:
    print(f"{a} is equal to {b}")

#Task 2

number=int(input("Enter a number: "))
if number > 0:
    print(f"{number} is a positive number") 
elif number < 0:
    print(f"{number} is a negative number")
else:
    print(f"{number} is zero")

#Task 3
number=int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number")
else:   
    print(f"{number} is an odd number")

#Task 4

score=int(input("Enter your score: "))
if score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.") 
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
elif score >= 50:
    print("Grade: E") 
else:
    print("Grade: F")

#Task 5

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a >= b and a >= c:
    print(f"{a} is the greatest number")
elif b >= a and b >= c:
    print(f"{b} is the greatest number")
else:
    print(f"{c} is the greatest number")

#Task 6

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == "+":
    result = a + b
    print(f"The result of {a} + {b} is: {result}")
elif operation == "-":
    result = a - b
    print(f"The result of {a} - {b} is: {result}")
elif operation == "*":
    result = a * b
    print(f"The result of {a} * {b} is: {result}")
elif operation == "/":
    if b != 0:
        result = a / b
        print(f"The result of {a} / {b} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")

#Task 7

age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age. Please enter a valid age.")
elif age <= 12:
    print("You are a child.")
elif age <= 17:
    print("You are a teenager.")
elif age <= 64:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

#Task 8

amount = float(input("Enter the amount: "))
if amount < 0:
    print("Invalid amount. Please enter a valid amount.")
elif amount < 100:
    discount = 0
elif amount < 300:
    discount = 0.10 * amount
elif amount < 500:
    discount = 0.15 * amount
else:
    discount = 0.20 * amount
if discount >= 0:
    final_amount = amount - discount
    print(f"Original amount: {amount}")
    print(f"Discount: {discount}")
    print(f"Final amount after discount: {final_amount}")

#Task 9
a = int(input("Enter a number: "))
b = int(input("Enter second number: "))
c = int(input("Enter a third number: "))
if a > b and a > c:
    if b > c:
        print(f"{a} is the greatest number, {b} is the second greatest number, and {c} is the smallest number.")
    else:
        print(f"{a} is the greatest number, {c} is the second greatest number, and {b} is the smallest number.")
if b > a and b > c:
    if a > c:
        print(f"{b} is the greatest number, {a} is the second greatest number, and {c} is the smallest number.")
    else:
        print(f"{b} is the greatest number, {c} is the second greatest number, and {a} is the smallest number.")
if c > a and c > b:
    if a > b:
        print(f"{c} is the greatest number, {a} is the second greatest number, and {b} is the smallest number.")
    else:
        print(f"{c} is the greatest number, {b} is the second greatest number, and {a} is the smallest number.")
else:
    print("There are equal numbers among the inputs.")

#Task 10

balance = 1000
amount = float(input("Enter the amount to withdraw: "))
if amount <= 0:
    print("Invalid amount. Please enter a positive amount.")
elif amount > balance:
    print("Insufficient balance. Please enter an amount less than or equal to your balance.")
else:
    balance -= amount
    print(f"Withdrawal successful. Your new balance is: {balance}")

#Task 11

usage = float(input("Enter the electricity usage in kWh: "))
if usage < 0:
    print("Invalid usage. Please enter a valid electricity usage.")
elif usage <= 100:
    rate = 0.08
    bill = usage * rate
    print("Usage is within the first 100 kWh. Rate: $0.08 per kWh." \")
elif usage <= 300:
    rate = 0.12
    bill = usage * rate
    print("Usage is between 101 and 300 kWh. Rate: $0.10 per kWh.")
else:
    rate = 0.15
    bill = usage * rate
    print("Usage is above 300 kWh. Rate: $0.15 per kWh.")

#Task 12

start_fee = 2
distance = float(input("Distance (km): "))
if distance < 0:
    print("Invalid distance")
else:
    if distance <= 5:
        distance_fee = distance * 0.70
    elif distance <= 15:
        distance_fee = 5 * 0.70 + (distance - 5) * 0.60
    else:
        distance_fee = 5 * 0.70 + 10 * 0.60 + (distance - 15) * 0.50
    total_fare = start_fee + distance_fee
    print("Starting fee:", start_fee, "AZN")
    print("Distance fee:", distance_fee, "AZN")
    print("Total amount:", total_fare, "AZN")

#Task 13

age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
loan_amount = float(input("Enter the loan amount: "))
if age < 18:
    print("You are not eligible for a loan due to age restrictions.")   
else:
    if salary < 500:
        print("You are not eligible for a loan due to insufficient salary.")
    else:
        if loan_amount > salary * 10:
            print("You are not eligible for a loan as the requested amount exceeds the maximum limit based on your salary.")
        else:
            print("You are eligible for a loan.")

#Task 14

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter a third number: "))
if a + b > c:
    if a + c > b:
        if b + c > a:
            if a == b:
                if b == c:
                    print("Equilateral")
                else:
                    print("Isosceles")
            else:
                if a == c:
                    print("Isosceles")
                elif b == c:
                    print("Isosceles")
                else:
                    print("Scalene")
        else:
            print("Triangle cannot be created")
    else:
        print("Triangle cannot be created")
else:
    print("Triangle cannot be created")

#Task 15

exam_score = float(input("Enter your exam score: "))
school_score = float(input("Enter your school score: "))
age = int(input("Enter your age: "))
if age < 16:
    print("Rejected: Age is below 16")
else:
    if exam_score < 0 or exam_score >700:
        print("Invalid exam score. Please enter a score between 0 and 700.")
    elif school_score < 0 or school_score > 100:
        print("Invalid school score. Please enter a score between 0 and 100.")
    elif exam_score >=600:
        print("Scholarship granted: Full scholarship")
    elif exam_score >=450:
        print("Accepted: Partial scholarship")
    elif exam_score >=300:
        if school_score >= 80:
            print("Accepted: Partial scholarship")
        else:
            print("Rejected: School score is below 80")
    else:
        print("Rejected: Exam score is below 300")

#Task 16

score = int(input("Enter your score: "))
result = "Pass" if score >= 50 else "Fail"
print(f"Result: {result}")

#Task 17

total = float(input("Enter the total amount: "))
membership = input("Are you a member? (yes/no): ")
if total < 0 or (membership != "yes" and membership != "no"):
    print("Invalid input")
else:
    delivery_fee = 0 if (total >= 50 or membership == "yes") else 5
    final_total = total + delivery_fee
    print(f"Delivery fee: {delivery_fee}")
    print(f"Final total: {final_total}")

#Task 18

day = input("Enter the day of the week: ")
match day:
    case 1:
        print("Monday - Study day")
    case 2:
        print("Tuesday - Study day")
    case 3:
        print("Wednesday - Study day")
    case 4:
        print("Thursday - Study day")
    case 5:
        print("Friday - Study day")
    case 6:
        print("Saturday - Weekend")
    case 7:
        print("Sunday - Weekend")
    case _:
        print("Invalid day")

#Task 19
code = input("Enter a code: ")
quantity = int(input("Enter the quantity: "))
if quantity < 1 or quantity > 10:
    print("Invalid quantity")
else:
    match code:
        case "T":
            drink, price = "Tea", 2
        case "C":
            drink, price = "Coffee", 4
        case "J":
            drink, price = "Juice", 3
        case _:
            drink, price = None, None
    if drink is not None:
        print("Unknown code")
    else:
        total = price * quantity
        order_type = "Large order" if total >=20 else "Regular order"
        print(f"Drink: {drink}, Quantity: {quantity}, Total: {total} AZN, Order type: {order_type}")

#Task 20

id = input("Enter your ID: ")
if len(id) != 8:
    print("rejection: student ID must contain 8 characters")
elif not id.isascii():
    print ("Rejection: Non-ASCII characters detected")
elif not id.isdecimal():
    print("Rejection: Student ID must contain only digits")
else:
    print("Student ID accepted")

#Task 21

stored_pin = "0427"
pin = input("Enter your PIN: ")
if len(pin) == 0:
    print("PIN is required")
elif len(pin) != 4:
    print("PIN must be 4 digits")
elif not (pin.isascii() and pin.isdecimal()):
    print("PIN must contain only digits")
elif pin = stored_pin:
    print("Access granted")
else:
    print("Incorrect PIN")

#Task 22

phone = input("Telefon nömrəsini daxil edin: ")

if len(phone) != 10:
    print(f"'{phone}' is invalid for this format (Incorrect length)")
elif not (phone.isascii() and phone.isdecimal()):
    print(f"'{phone}' is invalid for this format (Contains non-digits)")
elif phone[0] != "0":
    print(f"'{phone}' is invalid for this format (Must start with 0)")
else:
    prefix = phone[:3]
    match prefix:
        case "050" | "051" | "055" | "070" | "077" | "099":
            print(f"'{phone}' is valid")
        case _:
            print(f"'{phone}' is invalid for this format (Unsupported prefix)")

#Task 23

balance = 1000.0
stored_pin = "0427"

pin_input = input("PIN daxil edin: ")
amount_input = input("Məbləğ daxil edin: ")

if len(pin_input) != 4 or not (pin_input.isascii() and pin_input.isdecimal()):
    print("Error: Invalid PIN format")
elif pin_input != stored_pin:
    print("Error: Incorrect PIN")
elif not (amount_input.isascii() and amount_input.isdecimal()):
    print("Error: Invalid amount format (Digits only)")
else:
    amount = int(amount_input)
    if amount < 10 or amount > 500 or amount % 10 != 0:
        print("Error: Amount must be between 10 and 500 AZN and divisible by 10")
    else:
        fee = 0 if amount <= 200 else 2
        total_deduction = amount + fee
        if total_deduction > balance:
            print("Error: Insufficient balance for withdrawal + fee")
        else:
            balance -= total_deduction
            print(f"Withdrawal: {amount} AZN, Fee: {fee} AZN, New Balance: {balance:.2f} AZN")

#Task 24

product_code = input("Məhsul kodu (K/M/H): ")
quantity_str = input("Miqdar (1-5): ")
coupon_code = input("Kupon kodu (NONE/SAVE10): ")
delivery_code = input("Çatdırılma kodu (P/S): ")

match product_code:
    case "K":
        product, price = "Keyboard", 40
    case "M":
        product, price = "Mouse", 20
    case "H":
        product, price = "Headphones", 60
    case _:
        product, price = None, 0

if product is None:
    print("Error: Invalid product code")
elif not (quantity_str.isascii() and quantity_str.isdecimal()):
    print("Error: Quantity must contain digits only")
else:
    quantity = int(quantity_str)
    if quantity < 1 or quantity > 5:
        print("Error: Quantity must be between 1 and 5")
    elif coupon_code != "NONE" and coupon_code != "SAVE10":
        print("Error: Invalid coupon code")
    elif delivery_code != "P" and delivery_code != "S":
        print("Error: Invalid delivery code")
    else:
        subtotal = price * quantity
        if coupon_code == "SAVE10":
            if subtotal >= 100:
                discount = subtotal * 0.10
            else:
                discount = 0.0
                print("Warning: Kupon yalnız 100 AZN və üzəri üçün keçərlidir.")
        else:
            discount = 0.0

        discounted_subtotal = subtotal - discount

        if delivery_code == "P":
            delivery_fee = 0
        else:
            delivery_fee = 0 if discounted_subtotal >= 80 else 5

        final_total = discounted_subtotal + delivery_fee

        print(f"Product: {product}, Qty: {quantity}")
        print(f"Subtotal: {subtotal:.2f} AZN")
        print(f"Discount: {discount:.2f} AZN")
        print(f"Delivery Fee: {delivery_fee:.2f} AZN")
        print(f"Final Total: {final_total:.2f} AZN")

#Task 25

student_id = input("Student ID: ")
age_str = input("Age: ")
workshop_code = input("Workshop code (PY/WEB/CY): ")
payment_str = input("Payment amount: ")

if len(student_id) != 8 or not (student_id.isascii() and student_id.isdecimal()):
    print("Error: Invalid Student ID format")
elif not (age_str.isascii() and age_str.isdecimal()):
    print("Error: Invalid Age format")
else:
    age = int(age_str)
    if age < 16 or age > 65:
        print("Error: Age must be between 16 and 65")
    else:
        match workshop_code:
            case "PY":
                ws_name, base_fee, min_age = "Python Basics", 30, 16
            case "WEB":
                ws_name, base_fee, min_age = "Web Development", 40, 16
            case "CY":
                ws_name, base_fee, min_age = "Cybersecurity", 50, 18
            case _:
                ws_name, base_fee, min_age = None, 0, 0

        if ws_name is None:
            print("Error: Invalid workshop code")
        elif age < min_age:
            print(f"Error: Minimum age for {ws_name} is {min_age}")
        elif not (payment_str.isascii() and payment_str.isdecimal()):
            print("Error: Invalid Payment format")
        else:
            payment = int(payment_str)
            discount_rate = 0.20 if (16 <= age <= 18) else 0.0
            discount = base_fee * discount_rate
            final_fee = base_fee - discount

            if payment < final_fee:
                missing = final_fee - payment
                print(f"Insufficient payment. Missing amount: {missing:.2f} AZN")
            else:
                change = payment - final_fee
                print("Registration confirmed")
                print(f"Student ID: {student_id}, Workshop: {ws_name}")
                print(f"Discount: {discount:.2f} AZN, Final Fee: {final_fee:.2f} AZN, Change: {change:.2f} AZN")
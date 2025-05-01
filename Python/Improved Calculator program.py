# define arithmetic functions
def add(num1,num2):
    print(num1+num2)
def sub(num1,num2):
    print(num1-num2)
def mul(num1,num2):
    print(num1*num2)
def div(num1,num2):
    if num2 == 0:
        print("Division by zero is not allowed")
    print(num1/num2)

# Function to handle evaluating expressions
def evaluate_expression(expression):
    try:
        # Evaluate the expression and return the result
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"   #f-string for error message

#Improved calculator using control functions and BODMAS
def calculator():
    while True:
        print("\nEnter a maths expression as input for calculation in the format like: (2 + 3 * (4 - 1))")
        print("or type 'Exit' to quit the calculator")

        user_input = input("Enter your input: ")

        if user_input.lower == 'Exit':            #to check case sensitive letter for exit
            print("Exit calculator,Thank you!")
            break

        # Evaluate the user input expression and display the result
        result = evaluate_expression(user_input)
        print(f"Result:{result}")     #f-string to display result

# call the calculator
if __name__ == "__main__":
    calculator()
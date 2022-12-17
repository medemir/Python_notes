# calculator


# add
def add(n1,n2):
    return n1+n2

# subtract
def subtract(n1,n2):
    return n1-n2 

#division
def divide(n1,n2):
    return n1/n2

#multiply
def multiply(n1,n2):
    return n1*n2




operations = {
    '+': add, 
    '-': subtract, 
    '/': divide, 
    '*': multiply
}




def calculator():
    num1 = int(input('Your first number:'))

    for symbol in operations:
        print(symbol)
    should_continue=True

    while should_continue:
        operations_symbol = input('Pick operation from the line above:')
        num2 = int(input('Your second number:'))
        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operations_symbol} {num2} = {answer}")
    
        if input(f'Type 'y' to continue cal. with {answer}, or type 'n' to start new cal.') == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


    
    

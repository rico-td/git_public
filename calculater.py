def calculater(x,y,input_operater):
    
    add = lambda x,y: x+y
    sub = lambda x,y: x-y
    mul = lambda x,y: x*y
    div = lambda x,y: x/y if y != 0 else "UNDEFIEND DIVISION!"

    operators = {"+": add, "-": sub, "*": mul, "/": div}
    result = (operators[input_operater](x,y))

    # ENTER THE CALCULATION IN TERMINAL
    # x = pyinputplus.inputFloat("enter the 1st float number")
    # y = pyinputplus.inputFloat("enter the 2nd float number")
    # input_operater = pyinputplus.inputStr("enter the operator")
    
    print(f"result of {x} {input_operater} {y}: {result}")

def simpleCalculator(a,b):
    firstNum = a;
    secondNum = b;
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
    print ("The sum of " + str(firstNum) + "," + str(secondNum) + " is: "
        + str(add))
    print ("The subtraction of " + str(firstNum) + "," + str(secondNum) + " is: "
        + str(sub))
    print ("The multiplication of " + str(firstNum) + "," + str(secondNum) +
        " is: " + str(mul))
    print ("The division of " + str(firstNum) + "," + str(secondNum) + " is: "
        + str(div))

simpleCalculator(4,2)

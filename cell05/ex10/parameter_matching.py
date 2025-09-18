import sys 
if len(sys.argv) ==2:
    parameter = sys.argv[1]
    user_imput = imput("what was the parameter? ")

    if user_imput == parameter:
        print("good job!")
    else:
        print("nope, sorry...")
else:
    print("none")
while(True):
    oper = input("tf u wanna do + - / *")
    if(oper in ['+', '-', '*,', '/']):
        break  # - out of while loop
    else:
        print("Write + - * or /")


if(oper in ['*', '/']):
    total = int(input("starting number :"))
else:
    total = 0


while(True):
    try:
        x = input("Number :")
        if(x == ''):
            break
        if(oper == '+'):  # plus
            total += int(x)

        elif(oper == '-'):  # minus
            total -= int(x)

        elif(oper == '*'):  # mult
            total *= int(x)

        elif(oper == '/'):  # div
            total = total / int(x)
    except:
        print("write a number cunt")

print("total is : ", total)

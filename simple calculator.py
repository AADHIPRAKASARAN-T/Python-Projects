def show_menu():
    print("==Main Menu==")
    print("1.Addition")
    print("2.Subraction:")
    print("3.Multiplication")
    print("4.Division")
    print("5.Floor Division")
    print("6.Exponential")
while True:
    show_menu()
    choice=input("Enetr a choice(1-5):")
    a=float(input("Enter a number1:"))
    b=float(input("Enter a number2:"))
    if choice=='1':
        print("Result:", a+b)
    elif choice=='2':
        print("Result:",a-b)
    elif choice=='3':
        print("Result:",a*b)
    elif choice=='4':
        if b==0:
            print("Division By zero error")
        else:
            print("Result:",a/b)
    elif choice=='5':
        if b==0:
            print("Division By zero error")
        else:
            print("Result:",a//b)
    elif choice=='6':
        if b==0:
            print(1)
        else:
            print("Result:",a**b)
    else:
        print("Invalid Choice")


tasks=[]
def show_menu():
    print("==Main Menu==")
    print("1. Add")
    print("2. View")
    print("3. Remove")
    print("4. Quit")
        
while True:
    show_menu()
    choice=input("Enter an task number(1-4):")
    if choice=='1':
        task=input("enter a task:")
        tasks.append(task)
        print("task added:",task)
    elif choice=='2':
        if tasks:
            for i,task in enumerate(tasks,start=1):
                print(f"{i}.{task}")
        else:
            print("No tasks yet")
    elif choice=='3':
        if tasks:
            for i,task in enumerate(tasks,start=1):
                print(f"{i}.{task}")
            serial=int(input("enter task number:"))
            if 1<=serial<=len(tasks):
                removed=tasks.pop(serial-1)
                print("Removed Task:",removed)
            else:
                print("Invalid Number")
        else:
            print("NO tasks to remove")
    elif choice=='4':
        print("quit")
        break
    else:
        print("Invalid choice")
    
        
        
        
    
            
        
        

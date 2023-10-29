while True:
    print("Menue numbes:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Quit","\n")

    try:
       menu_num=int(input("Enter the menu number : "))

       if menu_num == 1:
           print("1 selected")

       elif menu_num == 2:
           print("2 selected")
       elif menu_num == 3:
           print("3 selected")
       elif menu_num == 4:
           print("You Quit the program")
           break
       else:
           print("Option not recognised")
    
    
    except ValueError:
        print("Requires a valid integer! Please try again.",end='')
        
           
   

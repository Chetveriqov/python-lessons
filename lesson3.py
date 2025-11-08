while True:
    
    operation = input("Введи что делае + - * / или exit: ")
    if operation == "exit":
        print("Вы вышли!")
        break
    
    num1 = int(input("Первое число: "))
    num2 = int(input("Второе число: "))
    
    if operation == "+":
        result = num1 + num2
        
    elif operation == "-":
        result = num1 - num2
        
    elif operation == "*":
        result = num1 * num2
        
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Нельзя делить на 0!"
                         
    else:
        result = "Неизвестный"
        
        
    print(f"Результат {result}")
tasks = [] #пустой список задач

while True:
    command = input("\nЧто делаем? (add, show, delete, exit): ").lower()
        
    if command == "add":
        task = input("Введите задачу: ")
        tasks.append(task)
        print(f"✅ Задача {task} добавлена!")
    
    elif command == "show":
        if len(tasks)  == 0:
            print("Список пуст!")
        else:
            print("\n Текущие задачи:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}: {t}")
                
    elif command == "delete":
        if len(tasks) == 0:
            print("\n Удолять нечего.")
        else:
            num = int(input("\n Введите номер задачи: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"\n Задача {removed} удолена!")
            else:
                print("\n Неверный номер задачи!")
                    
    elif command == "exit":
        print("\n До встречи")
        break
        
    else:
        print("Неизвестная команда. Попробуйте: add/show/delete/exit")
        print("Github config edit!!!")
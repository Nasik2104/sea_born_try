while True:
    try:
        user_input = int(input("Введіть ціле число:\n"))
        break
    except(ValueError):
        print("Я сказав ціле!!>:(")
        
print(f"Молодець! Ви ввели:\n{user_input}")
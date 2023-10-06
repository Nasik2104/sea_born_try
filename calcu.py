
while True:
    user_input = input('Привіт введіть свій вираз(для виходу введіть "c"):\n')
    
    if user_input.lower() == 'c':
        print("Дякую за використання!!!")
        break
    else:
        try:
            
            if '+' in user_input:
                values = user_input.split('+')
                print(int(values[0])+int(values[1]))    
                
            elif '-' in user_input:
                values = user_input.split('-')
                print(int(values[0])-int(values[1]))
            
            elif '*' in user_input:
                values = user_input.split('*')
                print(int(values[0])*int(values[1]))
            
            elif '/' in user_input:
                values = user_input.split('/')
                print(int(values[0])/int(values[1]))
                                
            else:   
                print(int(values))
            values.clear()
                     
        
        except(NameError, TypeError) as err:
            print("Цифри, а не букви і знаки")
        
        else:
            print("Все гуд")
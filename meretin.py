a=1 
 
    
while a==1: 
    print("Какую задачу вы хотите решить?") 
    print("1)Кодирование звука") 
    print("2)Кодирование изображения") 
    print("3)Кодирование текста")
    type=int(input()) 
    if type == 1:
        print("Выбрано: Кодирование звука") 
        a=2 
        print("введите неизвестную переменную")
        print("Нажмите 1 если неизвестна - A")
        print("Нажмите 2 если неизвестна - D")
        print("Нажмите 3 если неизвестна - T")
        print("Нажмите 4 если неизвестна - I")
        meow =int(input())
        if meow == 1:
            print("Введите D")
            d =int(input())
            print("Введите I")
            i =int(input())
            print("Введите T")
            t =int(input())
            print("если вы хотите посчитать размер моноаудиофайла нажмите 1")
            print("если вы хотите посчитать размер стереоаудиофайла нажмите 2")
            z = int(input())
            if z == 1:
                otvet = d*t*i/8
            if z == 2:
                otvet = 2*d*t*i/8
            print(otvet)
        elif meow == 2:
            print("Введите A")
            a =int(input())
            print("Введите I")
            i =int(input())
            print("Введите T")
            t =int(input())
            print("если вы хотите посчитать размер моноаудиофайла нажмите 1")
            print("если вы хотите посчитать размер стереоаудиофайла нажмите 2")
            z = int(input())
            if z == 1:
                otvet = a*8/t/i
            if z == 2:
                otvet = 2*a*8/t/i
            print(otvet)
        elif meow == 3:
            print("Введите D")
            d =int(input())
            print("Введите A")
            i =int(input())
            print("Введите I")
            t =int(input())
            print("если вы хотите посчитать размер моноаудиофайла нажмите 1")
            print("если вы хотите посчитать размер стереоаудиофайла нажмите 2")
            z = int(input())
            if z == 1:
                otvet = a*8/d/i
            if z == 2:
                otvet = 2*a*8/d/i
            print(otvet)
        elif meow == 4:
            print("Введите D")
            d =int(input())
            print("Введите A")
            i =int(input())
            print("Введите T")
            t =int(input())
            print("если вы хотите посчитать размер моноаудиофайла нажмите 1")
            print("если вы хотите посчитать размер стереоаудиофайла нажмите 2")
            z = int(input())
            if z == 1:
                otvet = a*8/d/t
            if z == 2:
                otvet = 2*a*8/d/t
            print(otvet)
        else:
            print("ошибка")
            
            
            
    elif type == 2: 
        print("Выбрано: Кодирование изображения")
        a=2 
    elif type == 3: 
        print("Выбрано: Кодирование текста") 
        a=2 
    else: 
        print("Ошибка404:тип задачи не обнаружен")


def f():
    vopros = [
        ("в армянском 39 букв?", "да"),
        ("у калимбы есть струны?", "нет"),
        ("ты выспался?", "нет"),
        ("в сникерсе всего 16 орешек?", "да"),
        ("любишь маму?", "да")    
    ]
     
    for q, 16a in vopros:
        print(q, '[да/нет]')
        answer = input().strip().lower()
        if answer == a:
            print("правильный ответ!")
        else:
            print("неправильный ответ...")

f()
    
z=1

while z==1:
    z=input('заново?')
    f()
    

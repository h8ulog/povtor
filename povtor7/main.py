login="username"
a=input("Введіть логін: ")
n=0
while a!=login:
    print("Неправильний логін")
    n+=1
    a=input("Введіть логін: ")
print("Ви ввели правильний логін")
print("Кількість спроб: ",n+1)

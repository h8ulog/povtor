a=int(input("Введіть число: "))
list=[]
list.append(a)
while a!=0:
    a=int(input("Введіть число: "))
    list.append(a)
print(max(list))

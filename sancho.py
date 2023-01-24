print("DO'stlaringiz ro'yhatini tuzamiz")
ismlar=[]
n=1
while True:
    savol=f"{n}-do'stingiz ismini kiriting"
    ism=input(savol)
    ismlar.append(ism)
    takrorlash = input("Yana ism kiritasizmi? (ha/yo'q')")
    n+=1
    if takrorlash != 'ha':
        break
    print(ismlar)
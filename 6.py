a=input("enter the month: ")
b=int(input("enter the date: "))
if a in ("december","january","february","march"):
    season = "winter"
elif a in ("march","april","may","june"):
    season = "summer"
elif a in ("july","august","september"):
    season = "spring"
else:
    season = "fall"
if(a=="march") and (b>=20):
    print("summer")
elif(a=="june") and (b>=21):
    print("spring")
elif(a=="september") and (b>=22):
    print("fall")
elif(a=="december") and (b>=21):
    print("winter")

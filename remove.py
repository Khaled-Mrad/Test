test=True
while test:
    ch = input("Enter your string  :")
    print(ch)
    x = input("what do you want to remove :")
    p = len(x)
    try:
        ch.index(x) != -1
        ch1=ch[:ch.index(x)]+ch[ch.index(x)+p:]
        print("done","\n","Result :",ch1)
    except:
        print("doesn\'t exist !!!!")
    verif=input("Do you want to try again (yes/no): ")
    if verif=="yes":
        test=True
    else :
        test=False
        print("Thank you !!!!")

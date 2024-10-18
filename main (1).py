# hometask 1
def funksiya(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma


print(funksiya(22, 6, 3))


#hometask2

def talaba_info(ism, familiya, **kwargs):
    kwargs["ism"] = ism
    kwargs["familiya"] = familiya
    return kwargs


talaba = talaba_info("Arslon", "Niyozmetov", tyil=1995

#hometask3

def kv(a,b,c,*sonlar):
    
    
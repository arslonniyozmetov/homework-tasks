# Hometask 1

def mijoz_haqida(ism, familiya, t_yil, t_joy, email="", tel=None):
    mijoz = {
        "ism": ism,
        "familiya": familiya,
        "t_yil": t_yil,
        "yoshi": 2020 - t_yil,
        "t_joy": t_joy,
        "email": email,
        "telefon": tel,
    }
    return mijoz


print("Mijozning ma'lumotlarini kiriting.")
mijozlar = []
while True:
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    t_yil = int(input("Tug'ilgan yili: "))
    t_joy = input("Tug'ilgan joyi: ")
    email = input("Email: ")
    telefon = input("Telefon raqami: ")
    mijozlar.append(mijoz_haqida(ism, familiya, t_yil, t_joy, email, telefon))
    javob = input("Davom etasizmi? (ha/yo'q)")
    if javob != "ha":
        break

print("Mijozlar: ")
for mijoz in mijozlar:
    print(
        f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
        f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}"
    )


#hometask 2

def son_max(x, y, z):
    max = x
    if y >= max:
        max = y
    if z >= max:
        max = z
    return max

#hometask 3
def aylana_info(radius, pi=3.14):
    aylana = {
        "radius": radius,
        "diametr": 2 * radius,
        "perimetr": 2 * radius * pi,
        "yuza": pi * radius ** 2,
    }
    return aylana
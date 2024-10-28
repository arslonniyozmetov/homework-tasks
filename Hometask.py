class Shaxs:
    def init(self, ism, familiya):
        self.ism = ism
        self.familiya = familiya

    def get_info(self):
        return f"Ism: {self.ism}, Familiya: {self.familiya}"

class Professor(Shaxs):
    def init(self, ism, familiya, mutaxassislik):
        super().init(ism, familiya)
        self.mutaxassislik = mutaxassislik

    def get_info(self):
        return f"Professor: {super().get_info()}, Mutaxassislik: {self.mutaxassislik}"

class Foydalanuvchi(Shaxs):
    def init(self, ism, familiya, email):
        super().init(ism, familiya)
        self.email = email

    def get_info(self):
        return f"Foydalanuvchi: {super().get_info()}, Email: {self.email}"

class Sotuvchi(Shaxs):
    def init(self, ism, familiya, mahsulot):
        super().init(ism, familiya)
        self.mahsulot = mahsulot

    def get_info(self):
        return f"Sotuvchi: {super().get_info()}, Mahsulot: {self.mahsulot}"

class Mijoz(Shaxs):
    def init(self, ism, familiya, telefon):
        super().init(ism, familiya)
        self.telefon = telefon

    def get_info(self):
        return f"Mijoz: {super().get_info()}, Telefon: {self.telefon}"

class Admin(Foydalanuvchi):
    def ban_user(self):
        print("Foydalanuvchi bloklandi")

professor = Professor("Ali", "Karimov", "Matematika")
foydalanuvchi = Foydalanuvchi("Oyguloy", "Davlatova", "oyna@example.com")
sotuvchi = Sotuvchi("Bobur", "Xolov", "Elektronika")
mijoz = Mijoz("Jamila", "Saidova", "+9989283747474")
admin = Admin("Jasur", "Rasulov", "jasur@gmail.com")

print(professor.get_info())
print(foydalanuvchi.get_info())
print(sotuvchi.get_info())
print(mijoz.get_info())
admin.ban_user()
print(admin.get_info())
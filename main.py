

# 6-m
class Talaba:
    def __init__(self, a, b, c):
        self.ism = a
        self.yosh = b
        self.kurs = c

t1 = Talaba("Ali", 20, 2)
print(t1.ism)
print(t1.yosh)
print(t1.kurs)

t2 = Talaba("Vali", 22, 3)
print(t2.ism)
print(t2.yosh)
print(t2.kurs)


# 7-m
class Kitob:
    def __init__(self, a, b, c):
        self.nomi = a
        self.muallif = b
        self.sahifa_nomi = c

k1 = Kitob("O'tkan kunlar", "Abdulla Qodiriy", 300)
print(k1.nomi)
print(k1.muallif)
print(k1.sahifa_nomi)

k2 = Kitob("Alkimyogar", "Paulo Coelho", 200)
print(k2.nomi)
print(k2.muallif)
print(k2.sahifa_nomi)


# 8-m
class Telefon:
    def __init__(self, madel, rang, narx):
        self.madel = madel
        self.rang = rang
        self.narx = narx

t1 = Telefon("iPhone 13", "qora", 1200)
print(t1.madel)
print(t1.rang)
print(t1.narx)

t2 = Telefon("Samsung S21", "oq", 900)
print(t2.madel)
print(t2.rang)
print(t2.narx)


# 9-m
class Mashina:
    def __init__(self, marka, rang, yili):
        self.marka = marka
        self.rang = rang
        self.yili = yili


m1 = Mashina("Cobalt", "oq", 2022)
print(m1.marka)
print(m1.rang)
print(m1.yili)

m2 = Mashina("Malibu", "qora", 2023)
print(m2.marka)
print(m2.rang)
print(m2.yili)


# 10-m
class Xodim:
    def __init__(self, ism, lavozim,  maosh):
        self.ism = ism
        self.lavozim = lavozim
        self.maosh = maosh

x1 = Xodim("Ali", "Dasturchi", 1000)
print(x1.ism)
print(x1.lavozim)
print(x1.maosh)


x2 = Xodim("Vali", "Manager", 1500)
print(x2.ism)
print(x2.lavozim)
print(x2.maosh)

x3 = Xodim("Hasan", "Dizayner", 1200)
print(x3.ism)
print(x3.lavozim)
print(x3.maosh)



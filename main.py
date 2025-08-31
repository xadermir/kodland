import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("Parola uzunlugunu girin: "))

sifre = ""

for i in range(uzunluk):
    sifre += random.choice(karakterler)

print("Olusturulan parola: ", sifre)
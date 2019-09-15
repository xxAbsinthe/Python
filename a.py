giriş = """
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
|                                                               |
|              S A Y I  T A H M İ N  O Y U N U N A              |
|                    H O Ş  G E L D İ N İ Z                     |
|                                                               |
|                                                    xxAbsinthe |
|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
"""
çıkış = """
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
|                                                               |
|              S A Y I  T A H M İ N  O Y U N U N U              |
|                O Y N A D I Ğ I N I Z  İ Ç İ N                 |
|                 T E Ş E K K Ü R  E D E R İ Z                  |
|                                                    xxAbsinthe |
|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
"""
print(giriş)
from random import randint
 
rand=randint(1, 100)
sayac=0

while True:
    sayac+=1
    try:
        sayi=int(input("1 ile 100 arasında değer girin (0 Çıkış):"))
    except ValueError:
        print("Lütfen sadece sayı girişi yapınız")
        continue
    if sayi==0:
        print("Çıkış yapılıyor...")
        break
    elif sayi < rand - 10:
        print("\nÇok düşük!\n\nDaha yüksek söyle.\n")
    elif sayi < rand:
        print("\nYaklaştın!\n\nYüksek söyle.\n")
    elif sayi > rand + 10:
        print("\nÇok büyük!\n\nDaha düşük söyle.\n")
    elif sayi > rand:
        print("\nYaklaştın!\n\nDüşük söyle.\n")
    else:
        print("Tebrikler :)\nTuttuğum sayı {0}!".format(rand))
        print("Tam {0} kerede tahmin ettin.".format(sayac))
        print(çıkış)
        break

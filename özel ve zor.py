# import math


# boy = float(input('Boyunuzu m cinsinden giriniz!'))
# kilo = int(input('Kilonuzu kg cinsinden giriniz!'))

# idealKilo = math.floor(22*boy*boy)
# fark = abs(idealKilo-kilo)
# if idealKilo > kilo:
#     print(f'{fark} kilo almalısınız')
# else:
#     print(f'{fark} kilo vermelisiniz')
# sayi1 = int(input('1nci Sayıyı Giriniz'))
# sayi2 = int(input('2nci Sayıyı Giriniz'))
# sayi3 = int(input('3nci Sayıyı Giriniz'))
# sayi4 = int(input('4nci Sayıyı Giriniz'))
# sayi5 = int(input('5nci Sayıyı Giriniz'))
# enBuyuk = sayi1

# if enBuyuk < sayi2:
#     enBuyuk = sayi2
# if enBuyuk < sayi3:
#     enBuyuk = sayi3
# if enBuyuk < sayi4:
#     enBuyuk = sayi4
# if enBuyuk < sayi5:
#     enBuyuk = sayi5


# print(f'Girilen Sayıların En Büyüğü = {enBuyuk}')
# import random

# randomSayi = random.randint,(1,3)
# cevap = int(input('Taş (1), Kağıt (2) Makas (3) Seçiniz'))
# sehirler  = [
# "Adana","Adıyaman","Afyonkarahisar","Ağrı","Aksaray","Amasya","Ankara","Antalya","Ardahan","Artvin","Aydın","Balıkesir","Bartın","Batman",
# "Bayburt","Bilecik","Bingöl","Bitlis","Bolu","Burdur","Bursa","Çanakkale","Çankırı","Çorum","Denizli","Diyarbakır","Düzce","Edirne","Elazığ",
# "Erzincan","Erzurum","Eskişehir","Gaziantep","Giresun","Gümüşhane","Hakkari","Hatay","Iğdır","Isparta","İstanbul","İzmir","Kahramanmaraş","Karabük",
# "Karaman","Kars","Kastamonu","Kayseri","Kilis","Kırıkkale","Kırklareli","Kırşehir","Kocaeli","Konya","Kütahya",
# "Malatya","Manisa","Mardin","Mersin","Muğla","Muş","Nevşehir","Niğde","Ordu","Osmaniye","Rize","Sakarya","Samsun","Şanlıurfa",
# "Siirt","Sinop","Şırnak","Sivas","Tekirdağ","Tokat","Trabzon","Tunceli","Uşak","Van","Yalova","Yozgat","Zonguldak"
# ]
# print(sehirler[0])
# print(sehirler.index("Aksaray"))
# print(sehirler[12])
# print(sehirler[80]) 
# print(sehirler[-1]) 
# print(sehirler[-2]) 
# print(sehirler[33])  
# sehirler[33] = "İçel"
# print(sehirler[33])  

# print(sehirler[80])
# sehirler.append("Tarsus")
# print(sehirler[81])
# sehirler.remove("Tarsus")
# print(len(sehirler))
# print(sehirler[-1])
# sehirler.pop()
# print(sehirler[-1])
# row1 = ['⬜️', '⬜️', '⬜️']
# row2 = ['⬜️', '⬜️', '⬜️']
# row3 = ['⬜️', '⬜️', '⬜️']
# harita = [row1, row2, row3]
# print(f'{row1}\n{row2}\n{row3}\n')

# pozisyon = input('Hazineyiğ nereye koymak istersin?\n')

# yatay = int(pozisyon[0]) -1
# dikey = int(pozisyon[1]) - 1 
# harita[dikey][yatay] = 'X'
# print(f'{row1}\n{row2}\n{row3}\n')
# import random
# taş = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# kağıt = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# makas = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# while True:
#     kullaniciSecimi = int(input('Taş(0), Kağıt(1), Makas(2) seç!'))
#     bilgisayarSecimi = random.randint(0,2)

#     print('Senin Seçimin')
#     if kullaniciSecimi == 0:
#         print(taş)
#     elif kullaniciSecimi ==1:
#         print(kağıt)
#     elif kullaniciSecimi ==2:
#         print(makas)

#         print('Bilgisayarın Seçimi')
#     if bilgisayarSecimi == 0:
#         print(taş)
#     elif bilgisayarSecimi ==1:
#         print(kağıt)
#     elif bilgisayarSecimi ==2:
#         print(makas)



#     if kullaniciSecimi >=3 or kullaniciSecimi < 0:
#         print('0 , 1 ,veya 2 giriniz')
#     elif kullaniciSecimi == 0 and bilgisayarSecimi == 2:
#         print('Yendin!')
#     elif bilgisayarSecimi == 0 and kullaniciSecimi == 2:
#         print('Kaybettin!')
#     elif kullaniciSecimi > bilgisayarSecimi:
#         print('Yendin!')
#     elif bilgisayarSecimi > kullaniciSecimi:
#         print('Kaybettin!')
#     else:
#         print('Berabere!')
# for sayi in range(0,1000):
#     if (sayi%3) == 0 and  (sayi%5) ==0:
#         print(sayi)



































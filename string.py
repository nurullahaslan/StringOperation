soz="Beni bu şehir boğuyor bilmem bana ne oluyor çöken karanlığın içinde umutlarım tükeniyor."
uzunluk=len(soz)
sesliHarfler = 'AEIİOÖUÜaeıioöuü'
sesliSayisi=0

for i in range(0,uzunluk):
    if soz[i] in sesliHarfler:
        sesliSayisi += 1
print("1.Adım:")
print("Sesli Harf Sayısı= %d"% sesliSayisi)
print('')
print('########################################################')
########################################################
uzunluk=len(soz)
for i in range(0, uzunluk):
    if(i==19):
        print("2.Adım:")
        for j in range(0,3):          
            print(soz[i])
print('')
print('########################################################')
########################################################
dilimlenmis=''
for i in range(4,33):
    dilimlenmis+=soz[i]
print("3.Adım:")
print(dilimlenmis)
print('')
print('########################################################')
#######################################################
sozSahibi=' Arap Şükrü'
soz+=sozSahibi
print("4.Adım:")
print(soz)
print('')
print('########################################################')
#######################################################
uzunluk=len(soz)
for i in range(0,uzunluk):
    if(soz[i] =='e'):
           list1 = list(soz)
           list1[i] = 'E'
           soz = ''.join(list1)
print("5.Adım:")           
print(soz)
print('')
print('########################################################')
#######################################################
import string

soz = string.capwords(soz)
print("6.Adım:")
print(soz)
print('')
print('########################################################')
#######################################################
uzunluk=len(soz)
sayac=0
for i in range(0,uzunluk):
    if(soz[i] =='n'):
           sayac+=1
print("7.Adım:")          
print("İsim Baş Harf Sayısı= %d"%sayac)
print('')
print('########################################################')
#######################################################
uzunluk=len(soz)
for i in range(0,uzunluk):
    if(soz[i] =='n'):
           print("8.Adım:") 
           i+=1
           print("Bulunan Konum= %d"%i )
           break
print('')
print('########################################################')
#######################################################
import re

sozListesi = re.sub("[^\w]", " ",  soz).split()
print("9.Adım:")           
print(sozListesi)
print('')
print('########################################################')
#######################################################
tcNo='12345678910'          
sozListesi+=list(tcNo) 
print("10.Adım:")
print(sozListesi)
print('')
print('########################################################')
#######################################################       
liste=['a','u','36','45']
elemanListe=''
for kelime in liste:  
        elemanListe += kelime
elemanListe=re.sub("[^\w]", " ",  elemanListe).split()
sozListesi+=elemanListe
print("11.Adım:")
print(sozListesi)
print('')
print('########################################################')
####################################################### 
sozListesi[12]='Soyad'
print("12.Adım:")
print(sozListesi)
print('')
print('########################################################')
#######################################################
sahip=re.sub("[^\w]", " ",  sozSahibi).split()
sozListesi=list(filter(lambda x: x not in sahip, sozListesi))    
print("13.Adım:")           
print(sozListesi)
print('')
print('########################################################')
#######################################################
sozListesi.reverse()
print("14.Adım:")           
print(sozListesi)
print('')
print('########################################################')
#######################################################         
print("15.Adım:") 
print("Liste Uzunluğu= %d"% len(sozListesi))
print('')
print('########################################################')
#######################################################
temp=[]
print("16.Adım:")
for i in range(4,15):
    temp.append(sozListesi[i])
sozListesi=temp   
print(sozListesi)
print('')
print('########################################################')
#######################################################
uzunluk=len(sozListesi)
birlestirilmis=sozListesi[0]
for i in range(1,uzunluk): 
    birlestirilmis+=('***'+sozListesi[i])
print("17.Adım:") 
print(birlestirilmis)
print('')
print('########################################################')

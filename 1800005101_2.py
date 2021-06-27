#Salon Bilet Sistemi Proje Ödevi 2
#1800005101 Muhammed Hüseyin ÖZDEMİR

import time

"""Salon Tanımla"""
salon=[]

for x in range(20):
    salon.append(['-' for i in range(20)])

secim=True

"""Toplam Ciro Tanımla"""
toplamCiro = 0
ciro1 = 0
ciro2 = 0
ciro3 = 0
ciro4 = 0

"""Toplam Satılan Bilet Adet Tanımla"""
satis1 = 0
satis2 = 0
satis3 = 0
satis4 = 0

def print_ana_menu():
    print('''************************
******  ANA MENÜ  ******
************************
1) Rezervasyon
2) Salonu Yazdır
3) Yeni Etkinlik
4) Hesap Dökümü
0) Çıkış
************************''')

def ciro_yaz():
    toplamBilet = satis1+satis2+satis3+satis4
    print("1. kategori için toplam satılan bilet adedi: {} / toplam ciro: {} TL".format(satis1,ciro1))
    print("2. kategori için toplam satılan bilet adedi: {} / toplam ciro: {} TL".format(satis2,ciro2))
    print("3. kategori için toplam satılan bilet adedi: {} / toplam ciro: {} TL".format(satis3,ciro3))
    print("4. kategori için toplam satılan bilet adedi: {} / toplam ciro: {} TL".format(satis4,ciro4))
    print("Toplam Ciro: ",toplamCiro," TL / Toplam Satılan Bilet Adedi: ",toplamBilet," / Salonda Müsait Koltuk Sayısı: ",400-toplamBilet)


def hesapDokumu(kategori,bilet_adedi,netTutar):
    global ciro1
    global ciro2
    global ciro3
    global ciro4
    global satis1
    global satis2
    global satis3
    global satis4
    global toplamCiro

    if kategori == 1:
        toplamCiro = toplamCiro + netTutar
        ciro1 = ciro1 + netTutar
        satis1 = satis1 + bilet_adedi
    elif kategori == 2:
        toplamCiro = toplamCiro + netTutar
        ciro2 = ciro2 + netTutar
        satis2 = satis2 + bilet_adedi
    elif kategori == 3:
        toplamCiro = toplamCiro + netTutar
        ciro3 = ciro3 + netTutar
        satis3 = satis3 + bilet_adedi
    elif kategori == 4:
        toplamCiro = toplamCiro + netTutar
        ciro4 = ciro4 + netTutar
        satis4 = satis4 + bilet_adedi
     
def fiyatlistesi():
    global secim
    with open("indirim.txt","r") as file:
        for satir in file:
            file.seek(6)
            fiyat = file.read(22)
            print("Bilet Fiyat Listesi\n*******************\n{}\n*******************".format(fiyat))
            onay = input("Kategori seçimi yapmak istiyor musunuz ? E/H: ")
            if onay == "E" or onay == "e":
                bilet_yaz()
            elif onay == "H" or onay == "h":
                return secim == False
            else:
                print("Hatalı Giriş Yaptınız !")
                return fiyatlistesi()
                
def UcretHesapla(kategori,bilet_adedi):
    with open("indirim.txt","r") as file:
        if kategori == 1:
            if bilet_adedi >= 2 and bilet_adedi <= 4:
                file.seek(33)
                indirimoran = file.read(11)
                print("Seçmiş olduğunuz {}. kategorideki {} adet bilet için uygulanan indirim oranı(Kategori-Min/Max Bilet Adedi-İndirim Oranı): {}".format(kategori,bilet_adedi,indirimoran),end="")
                ucret = 200 * bilet_adedi
                indirim = 200 * bilet_adedi * (10/100)
                netTutar = 200 * bilet_adedi * (90/100)
                print("Toplamda {} adet bilet için tutar: {} TL\nUygulanan indirim: {} TL\nİndirimli tutar: {} TL".format(bilet_adedi,ucret,indirim,netTutar))
                hesapDokumu(kategori,bilet_adedi,netTutar)

            elif bilet_adedi >= 5 and bilet_adedi <= 7:
                file.seek(45)
                indirimoran = file.read(11)
                print("Seçmiş olduğunuz {}. kategorideki {} adet bilet için uygulanan indirim oranı(Kategori-Min/Max Bilet Adedi-İndirim Oranı): {}".format(kategori,bilet_adedi,indirimoran),end="")
                ucret = 200 * bilet_adedi
                indirim = 200 * bilet_adedi * (20/100)
                netTutar = 200 * bilet_adedi * (80/100)
                print("Toplamda {} adet bilet için tutar: {} TL\nUygulanan indirim: {} TL\nİndirimli tutar: {} TL".format(bilet_adedi,ucret,indirim,netTutar))
                hesapDokumu(kategori,bilet_adedi,netTutar)

            elif bilet_adedi >= 8 and bilet_adedi <= 10:
                file.seek(57)
                indirimoran = file.read(11)
                print("Seçmiş olduğunuz {}. kategorideki {} adet bilet için uygulanan indirim oranı(Kategori-Min/Max Bilet Adedi-İndirim Oranı): {}".format(kategori,bilet_adedi,indirimoran),end="")
                ucret = 200 * bilet_adedi
                indirim = 200 * bilet_adedi * (25/100)
                netTutar = 200 * bilet_adedi * (75/100)
                print("Toplamda {} adet bilet için tutar: {} TL\nUygulanan indirim: {} TL\nİndirimli tutar: {} TL".format(bilet_adedi,ucret,indirim,netTutar))
                hesapDokumu(kategori,bilet_adedi,netTutar)

        elif kategori == 2:
            if bilet_adedi >= 2 and bilet_adedi <= 4:
                file.seek(69)
                indirimoran = file.read(11)
                print("Seçmiş olduğunuz {}. kategorideki {} adet bilet için uygulanan indirim oranı(Kategori-Min/Max Bilet Adedi-İndirim Oranı): {}".format(kategori,bilet_adedi,indirimoran),end="")
                ucret = 150 * bilet_adedi
                indirim = 150 * bilet_adedi * (5/100)
                netTutar = 150 * bilet_adedi * (85/100)
                print("Toplamda {} adet bilet için tutar: {} TL\nUygulanan indirim: {} TL\nİndirimli tutar: {} TL".format(bilet_adedi,ucret,indirim,netTutar))
                hesapDokumu(kategori,bilet_adedi,netTutar)

            elif bilet_adedi >= 5 and bilet_adedi <= 7:
                file.seek(81)
                indirimoran = file.read(11)
                print("Seçmiş olduğunuz {}. kategorideki {} adet bilet için uygulanan indirim oranı(Kategori-Min/Max Bilet Adedi-İndirim Oranı): {}".format(kategori,bilet_adedi,indirimoran),end="")
                ucret = 150 * bilet_adedi
                indirim = 150 * bilet_adedi * (15/100)
                netTutar = 150 * bilet_adedi * (85/100)
                print("Toplamda {} adet bilet için tutar: {} TL\nUygulanan indirim: {} TL\nİndirimli tutar: {} TL".format(bilet_adedi,ucret,indirim,netTutar))
                hesapDokumu(kategori,bilet_adedi,netTutar)

            elif bilet_adedi >= 8 and bilet_adedi <= 10:
                file.seek(93)
                indirimoran = file.read(11)
                print("Seçmiş olduğunuz {}. kategorideki {} adet bilet için uygulanan indirim oranı(Kategori-Min/Max Bilet Adedi-İndirim Oranı): {}".format(kategori,bilet_adedi,indirimoran),end="")
                ucret = 150 * bilet_adedi
                indirim = 150 * bilet_adedi * (20/100)
                netTutar = 150 * bilet_adedi * (80/100)
                print("Toplamda {} adet bilet için tutar: {} TL\nUygulanan indirim: {} TL\nİndirimli tutar: {} TL".format(bilet_adedi,ucret,indirim,netTutar))
                hesapDokumu(kategori,bilet_adedi,netTutar)

        elif kategori == 3:
            if bilet_adedi >= 2 and bilet_adedi <= 4:
                file.seek(105)
                indirimoran = file.read(11)
                print("Seçmiş olduğunuz {}. kategorideki {} adet bilet için uygulanan indirim oranı(Kategori-Min/Max Bilet Adedi-İndirim Oranı): {}".format(kategori,bilet_adedi,indirimoran),end="")
                ucret = 100 * bilet_adedi
                indirim = 100 * bilet_adedi * (15/100)
                netTutar = 100 * bilet_adedi * (85/100)
                print("Toplamda {} adet bilet için tutar: {} TL\nUygulanan indirim: {} TL\nİndirimli tutar: {} TL".format(bilet_adedi,ucret,indirim,netTutar))
                hesapDokumu(kategori,bilet_adedi,netTutar)

            elif bilet_adedi >= 5 and bilet_adedi <= 7:
                file.seek(117)
                indirimoran = file.read(11)
                print("Seçmiş olduğunuz {}. kategorideki {} adet bilet için uygulanan indirim oranı(Kategori-Min/Max Bilet Adedi-İndirim Oranı): {}".format(kategori,bilet_adedi,indirimoran),end="")
                ucret = 100 * bilet_adedi
                indirim = 100 * bilet_adedi * (20/100)
                netTutar = 100 * bilet_adedi * (80/100)
                print("Toplamda {} adet bilet için tutar: {} TL\nUygulanan indirim: {} TL\nİndirimli tutar: {} TL".format(bilet_adedi,ucret,indirim,netTutar))
                hesapDokumu(kategori,bilet_adedi,netTutar)

            elif bilet_adedi >= 8 and bilet_adedi <= 10:
                file.seek(129)
                indirimoran = file.read(11)
                print("Seçmiş olduğunuz {}. kategorideki {} adet bilet için uygulanan indirim oranı(Kategori-Min/Max Bilet Adedi-İndirim Oranı): {}".format(kategori,bilet_adedi,indirimoran),end="")
                ucret = 100 * bilet_adedi
                indirim = 100 * bilet_adedi * (35/100)
                netTutar = 100 * bilet_adedi * (65/100)
                print("Toplamda {} adet bilet için tutar: {} TL\nUygulanan indirim: {} TL\nİndirimli tutar: {} TL".format(bilet_adedi,ucret,indirim,netTutar))
                hesapDokumu(kategori,bilet_adedi,netTutar)

        elif kategori == 4:
            if bilet_adedi >= 2 and bilet_adedi <= 4:
                file.seek(141)
                indirimoran = file.read(11)
                print("Seçmiş olduğunuz {}. kategorideki {} adet bilet için uygulanan indirim oranı(Kategori-Min/Max Bilet Adedi-İndirim Oranı): {}".format(kategori,bilet_adedi,indirimoran),end="")
                ucret = 60 * bilet_adedi
                indirim = 60 * bilet_adedi * (5/100)
                netTutar = 60 * bilet_adedi * (95/100)
                print("Seçmiş olduğunuz {}. kategorideki {} adet bilet için uygulanan indirim oranı(Kategori-Min/Max Bilet Adedi-İndirim Oranı): {}".format(kategori,bilet_adedi,indirimoran),end="")
                hesapDokumu(kategori,bilet_adedi,netTutar)

            elif bilet_adedi >= 5 and bilet_adedi <= 7:
                file.seek(153)
                indirimoran = file.read(11)
                print("Seçmiş olduğunuz {}. kategorideki {} adet bilet için uygulanan indirim oranı(Kategori-Min/Max Bilet Adedi-İndirim Oranı): {}".format(kategori,bilet_adedi,indirimoran),end="")
                ucret = 60 * bilet_adedi
                indirim = 60 * bilet_adedi * (10/100)
                netTutar = 60 * bilet_adedi * (90/100)
                
                hesapDokumu(kategori,bilet_adedi,netTutar)

            elif bilet_adedi >= 8 and bilet_adedi <= 10:
                file.seek(165)
                indirimoran = file.read(11)
                print("Seçmiş olduğunuz {}. kategorideki {} adet bilet için uygulanan indirim oranı(Kategori-Min/Max Bilet Adedi-İndirim Oranı): {}".format(kategori,bilet_adedi,indirimoran),end="")
                ucret = 60 * bilet_adedi
                indirim = 60 * bilet_adedi * (15/100)
                netTutar = 60 * bilet_adedi * (85/100)
                print("Toplamda {} adet bilet için tutar: {} TL\nUygulanan indirim: {} TL\nİndirimli tutar: {} TL".format(bilet_adedi,ucret,indirim,netTutar))
                hesapDokumu(kategori,bilet_adedi,netTutar) 
                        
        
def print_salon():
    global salon
    for x in range(len(salon)):
        line=''
        for y in range(len(salon[x])):
            sln = ''.join(salon[x][y])
            line=line+sln
        print(line)

        
def al_secim():
    secim=int(input('Seçiminiz:'))
    
    if secim==1:
        fiyatlistesi()

    elif secim==2:
        print_salon()
        
    elif secim==3:
        global salon
        global toplamCiro
        global ciro1
        global ciro2
        global ciro3
        global ciro4
        global satis1
        global satis2
        global satis3
        global satis4
        salon=[]
        for x in range(20):
            salon.append(['-' for i in range(20)])
        toplamCiro = 0
        ciro1 = 0
        ciro2 = 0
        ciro3 = 0
        ciro4 = 0
        satis1 = 0
        satis2 = 0
        satis3 = 0
        satis4 = 0

    elif secim==4:
        ciro_yaz()
                   
    elif secim==0:
        print('Çıkış yapılıyor...')
        time.sleep(1)
        return False

    
def bilet_yaz():
    global salon

    kategori=int(input('Kategori (1-4):'))
    while kategori not in range(1,5):
        kategori=int(input('Lütfen 1-4 Arasında Kategori Seçiniz: '))
        
    
    bilet_adedi=int(input('Bilet adedi (1-10):'))
    while bilet_adedi not in range(1,11):
        bilet_adedi=int(input('1 seferde en fazla 10 adet bilet alabilirsiniz !: '))
    
    #Kategori 1
    if kategori==1:
        line=''
        for x in range(0,10):
            for y in range(5,15):                   
                if salon[x][y]=='-':
                    if x==9 and y+bilet_adedi > 15:
                        print('Üzgünüm, bu kategoride '+ str(int(15-y)) +' kişilik yer kaldı !')
                        break
                        
                    else:
                        print('Rezerve edilen koltuklar (Sıra-Koltuk):')
                        for i in range(0,bilet_adedi):
                            
                            if y<15:
                                salon[x][y]='X'
                                line=line+str(x+1)+' - '+str(y+1)+', '
                                y+=1
    
                            else:
                                x+=1
                                y=5
                                salon[x][y]='X'
                                line=line+str(x+1)+' - '+str(y+1)+', '
                                y+=1
                                
                    if line!='':
                        break

                if line!='':
                    break
                
            if line!='':
                break
    
        print(line)
        if line!='':
            UcretHesapla(kategori,bilet_adedi)
        else:
            return bilet_adedi
            
    #Kategori 2
    if kategori==2:
        line=''
        for x in range(0,10):
            for y in range(4,0,-1):
                if salon[x][y]=='-':
                    if x == 9 and abs(bilet_adedi-y) > 6:
                        print('Üzgünüm bu kategoride ' + str(int(y+6)) + ' kişilik yer kaldı !')
                        break
                    else:
                        print('Rezerve edilen koltuklar (Sıra-Koltuk):')
                        for i in range(0,bilet_adedi):
                            if y > -1 and y < 5:
                                salon[x][y]='X'
                                line=line+str(x+1)+' - '+str(y+1)+', '
                                y-=1
                            elif y > 14 and y < 20:
                                salon[x][y]='X'
                                line=line+str(x+1)+' - '+str(y+1)+', '
                                y+=1
                            else:
                                y=15
                                salon[x][y]='X'
                                line=line+str(x+1)+' - '+str(y+1)+', '
                                y+=1
                        if line!='':
                            break
                if line!='':
                    break
            if line!='':
                break

            if line=='':
                for y in range(15,20):
                    if salon[x][y]=='-':
                        if x == 9 and y+bilet_adedi > 20:
                            print('Üzgünüm bu kategoride ' + str(int(20-y)) + ' kişilik yer kaldı !')
                            break
                        else:
                            for i in range(0,bilet_adedi):
                                if y > 14 and y < 20:
                                    salon[x][y]='X',
                                    line=line+str(x+1)+' - '+str(y+1)+', '
                                    y+=1
                                elif y==20:
                                    y=4
                                    x+=1
                                    salon[x][y]='X'
                                    line=line+str(x+1)+' - '+str(y+1)+', '
                                    y-=1
                                elif y > -1 and y < 5:
                                    salon[x][y]='X'
                                    line=line+str(x+1)+' - '+str(y+1)+', '
                                    y-=1
                                elif y==-1:
                                    y=15
                                    salon[x][y]='X'
                                    line=line+str(x+1)+' - '+str(y+1)+', '
                                    y+=1

                            if line!='':
                                break
                    if line!='':
                        break
        print(line)
        if line!='':
            UcretHesapla(kategori,bilet_adedi)
        else:
            return bilet_adedi
    #Kategori 3
    if kategori==3:
        line=''
        for x in range(10,20):
            for y in range(5,15):
                                    
                if salon[x][y]=='-':
                    if x==19 and y+bilet_adedi > 16:
                        print('Üzgünüm, bu kategoride '+ str(int(15-y)) +' kişilik yer kaldı !')
                        break
                        
                    else:
                        print('Rezerve edilen koltuklar (Sıra-Koltuk):')
                        for i in range(0,bilet_adedi):
                            
                            if y<15:
                                salon[x][y]='X'
                                line=line+str(x+1)+' - '+str(y+1)+', '
                                y+=1
    
                            else:
                                x+=1
                                y=5
                                salon[x][y]='X'
                                line=line+str(x+1)+' - '+str(y+1)+', '
                                y+=1
                                
                    if line!='':
                        break

                if line!='':
                    break
                
            if line!='':
                break
    
        print(line)
        if line!='':
            UcretHesapla(kategori,bilet_adedi)
        else:
            return bilet_adedi
    #Kategori 4
    if kategori==4:
        line=''
        for x in range(10,20):
            for y in range(4,0,-1):
                if salon[x][y]=='-':
                    if x == 19 and abs(bilet_adedi - y) > 6:
                        print('Üzgünüm bu kategoride ' + str(int(y+5)) + ' kişilik yer kaldı !')
                        break
                    else:
                        print('Rezerve edilen koltuklar (Sıra-Koltuk):')
                        for i in range(0,bilet_adedi):
                            if y > -1 and y < 5:
                                salon[x][y]='X'
                                line=line+str(x+1)+' - '+str(y+1)+', '
                                y-=1
                            elif y > 14 and y < 20:
                                salon[x][y]='X'
                                line=line+str(x+1)+' - '+str(y+1)+', '
                                y+=1
                            else:
                                y=15
                                salon[x][y]='X'
                                line=line+str(x+1)+' - '+str(y+1)+', '
                                y+=1
                        if line!='':
                            break
                if line!='':
                    break
            if line!='':
                break
            if line=='':
                for y in range(15,20):
                    if salon[x][y]=='-':
                        if x == 19 and y+bilet_adedi > 20:
                            print('Üzgünüm bu kategoride ' + str(int(20-y)) + ' kişilik yer kaldı !')
                            break
                        else:
                            for i in range(0,bilet_adedi):
                                if y > 14 and y < 20:
                                    salon[x][y]='X',
                                    line=line+str(x+1)+' - '+str(y+1)+', '
                                    y+=1
                                elif y==20:
                                    y=4
                                    x+=1
                                    salon[x][y]='X'
                                    line=line+str(x+1)+' - '+str(y+1)+', '
                                    y-=1
                                elif y > -1 and y < 5:
                                    salon[x][y]='X'
                                    line=line+str(x+1)+' - '+str(y+1)+', '
                                    y-=1
                                elif y==-1:
                                    y=15
                                    salon[x][y]='X'
                                    line=line+str(x+1)+' - '+str(y+1)+', '
                                    y+=1
                            if line!='':
                                break     
                    if line!='':
                        break
        print(line)
        if line!='':
            UcretHesapla(kategori,bilet_adedi)
        else:
            return bilet_adedi
        
def bilet_satis():
    secim=True
    while secim:
        
        print_ana_menu()
        
        if al_secim()==False:
            secim=False

#Ana Program:
            
bilet_satis()


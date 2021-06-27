#Salon Bilet Sistemi Proje Ödevi
#1800005101 Muhammed Hüseyin ÖZDEMİR

"""Salon tanımla"""
salon=[]

for x in range(20):
    salon.append(['-' for i in range(20)])

secim=True

def print_ana_menu():
    print('''************************
******  ANA MENÜ  ******
************************
1) Rezervasyon
2) Salonu Yazdır
3) Yeni Etkinlik
0) Çıkış
************************''')


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
        bilet_yaz()
        
    elif secim==2:
        print_salon()
        
    elif secim==3:
        global salon
        salon=[]
        for x in range(20):
            salon.append(['-' for i in range(20)])
            
            
    elif secim==0:
        print('Çıkış yapılıyor...')
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
                    if x==9 and y+bilet_adedi > 16:
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

    #Kategori 2
    if kategori==2:
        line=''
        for x in range(0,10):
            for y in range(4,0,-1):
                if salon[x][y]=='-':
                    if x == 9 and abs(bilet_adedi-y) > 6:
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

        
def bilet_satis():
    secim=True
    while secim:
        
        print_ana_menu()
        
        if al_secim()==False:
            secim=False

#Ana Program:
            
bilet_satis()


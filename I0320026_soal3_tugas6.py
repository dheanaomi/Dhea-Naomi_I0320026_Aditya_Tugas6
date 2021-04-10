batas_atas = 24
batas_bawah = 10

for angka in range(batas_bawah,batas_atas + 1):
    if angka > 0:
        for u in range(2,angka):
            if (angka % u) == 0:
                print(angka,'bukan bilangan prima')
                break
        else:
            print(angka, 'bilangan prima')
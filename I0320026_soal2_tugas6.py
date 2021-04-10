print ("=====Mencari Nilai Rata-Rata=====")
i = int(input("Banyaknya nilai yang akan dihitung : "))
x = 1

listnilai =[]
banyaknilai = 0

while x <= i :
    nilai = int(input("Nilai ke-%d : " % x))
    x += 1
    listnilai.append(nilai)

banyaknilai = sum(listnilai)
ratarata = banyaknilai/i
print(" ")
print("Rata-rata dari nilai yang diinput pengguna adalah", '%0.1f' % ratarata)
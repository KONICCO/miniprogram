import random

# 1 angka secara acak dari 1 - 10
angka = random.randrange(1,11) # mulai 1 hingga 10
awal= 0
max_tebak=3
tebak= False
temp= []
print('program tebak angka 1-10')
print('3x kali kesempatan menebak')
while awal< max_tebak:  #bersifat perulangan true maka akan memasuki kondisi selanjutnya
  awal = awal + 1
  tebakan = int(input('Masukkan angka : ')) #masukan angka tebakan
  temp.append(tebakan)
  if tebakan == angka:
    # Jika tebakan sama dengan angka random
    tebak= True
  elif tebakan > angka:
    #jika tebakan anda lebih besar dari angka random
    print('Angka terlalu besar')
  else:
    #jika tebakan anda lebih kecil dari angka random
    print('Angka terlalu kecil')

if tebak == True: #tebak memiliki nilai True
  print('Selamat Anda menebak!!!')
else: #tebak memiliki nilai False
  print('\t\t\tgame over\n')
  print('angka yang benar adalah', angka)
  no=1
  for i in temp:
    print(f'angka ke-{no} yang anda masukan adalah',i)
    no+=1
  



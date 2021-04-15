def fnum():
    print("""Selamat datang di menu Fungsi numerik, masukkan angka""")

    nilai = []

    kosong = ' '
    while kosong != 'quit':
        kosong = input('Masukkan nilai, ketik "quit" jika sudah selesai\n>> ')

        if kosong != 'quit':
            nilai.append(float(kosong))

    print(nilai)
    urut = input('Apakah anda ingin mengurutkan angka? [Y/N]\n>> ')
    if urut == 'Y' or urut == 'y':
        nilai.sort()
        print(nilai)
    else:
        print(nilai)

    choice = int(input('''Mau diapakan angkanya?
    [1] Nilai maksimum
    [2] Nilai minimum
    [3] Jumlah data
    [4] Keluar dari program
    >> '''))

    if choice == 1:
        print('Nilai maksimum = ', max(nilai))
    elif choice == 2:
        print('Nilai maksimum = ', min(nilai))
    elif choice == 3:
        jml = len(nilai)
        print(f'Data anda ada {jml} bilangan')
    else:
        exit()

fnum()

# Main Loop Program
if __name__ == "__main__": 
    while True :
        fnum()










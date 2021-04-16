#fungsi berisi semua nilai
nilai = []

#fungsi memasukkan angka ke list
def in_angka():

    kosong = ' '
    while kosong != 'next':
        kosong = input('Masukkan nilai, ketik "next" jika sudah selesai\n>> ')

        if kosong != 'next':
            nilai.append(float(kosong))
            print(nilai)


def fnum():
    print("""Selamat datang di menu Fungsi numerik, masukkan angka""")
    in_angka()
    urut = input('Apakah anda ingin mengurutkan angka? [Y/N]\n>> ')
    if urut == 'Y' or urut == 'y':
        nilai.sort()
        print(nilai)
    else:
        print(nilai)
    menu()

def menu():
    choice = int(input('''Mau diapakan angkanya?
    [1] Nilai maksimum
    [2] Nilai minimum
    [3] Jumlah data
    [4] Menambah angka
    [5] Keluar dari program
    >> '''))

    if choice == 1:
        print('Nilai maksimum = ', max(nilai))
        menu()
    elif choice == 2:
        print('Nilai maksimum = ', min(nilai))
        menu()
    elif choice == 3:
        jml = len(nilai)
        print(f'Data anda ada {jml} bilangan')
        menu()
    elif choice == 4:
        in_angka()
    else:
        exit()


# Main Loop Program
if __name__ == "__main__": 
    while True :
        fnum()










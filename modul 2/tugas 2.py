#menampilkan status gaji karyawan 
gaji = int(input("masukan gaji:"))
berkeluarga = (False, True) [input("sudah berkeluarga? (y/t)") =="y" ]
punya_rumah = (False, True) [input("punya rumah (y/t)") == "y" ]

if gaji > 3000000:
    print ("gaji sudah di atas UMR")
    if berkeluarga:
        print ("wajib ikut asuransi dan menabung untuk pensiun")
    else:
        print ("tidak perlu ikut asuransi")

    if punya_rumah:
        print ("wajib bayar pajak")
    else:
        print ("tidak wajib bayar pajak rumah")
else:
    print ("gaji belum umr")

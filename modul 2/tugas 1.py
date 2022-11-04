# menentukan nilai akhir 
nama = input("masukan nama:")
uts = input("masukan nilai UTS:")
UAS = input("masukan nilai UAS:")
tugas = input("masukan nilai tugas:")

akhir = (int(tugas) * .2) + (int(uts) * .4) + (int(UAS) *.4)
keterangan = ("tidak lulus", "lulus") [akhir > 60.0]
if akhir > 80:
    huruf = "A"
elif akhir > 70:
    huruf = "B"
elif akhir > 50:
    huruf = "C"
elif akhir > 40:
    huruf = "D"
else :
    huruf = "E"

print("nama             :",nama)
print("nilai UTS        :",uts)
print("nilai UAS        :",UAS)
print("nilai tugas      :",tugas)
print("nilai akhir      :",akhir)
print("nilai huruf      :",huruf)
print("keterangan       :",keterangan)
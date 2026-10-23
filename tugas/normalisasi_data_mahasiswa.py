def normalisasi_nama(nama):
    return nama.strip().title()

def buat_inisial(nama):
    kata_kata = normalisasi_nama(nama).split()
    return "".join([kata[0].upper() for kata in kata_kata])

def normalisasi_kode(kode):
    return "-".join(kode.strip().upper().split())

if __name__ == "__main__":
    nama_input = input("Nama: ")
    kode_input = input("Kode kelas: ")

    nama_bersih = normalisasi_nama(nama_input)
    kode_bersih = normalisasi_kode(kode_input)
    jumlah_kata = len(nama_bersih.split())
    inisial = buat_inisial(nama_input)

    print(f"Nama bersih : {nama_bersih}")
    print(f"Kode kelas  : {kode_bersih}")
    print(f"Jumlah kata : {jumlah_kata}")
    print(f"Inisial     : {inisial}")
import math

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_di_awal(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def tambah_di_akhir(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def tambah_di_antara(self, posisi, data):
        if posisi < 0: 
            print("Posisi tidak valid")
            return
        if posisi == 0:
            self.tambah_di_awal(data)
            return
        new_node = Node(data)
        current = self.head
        prev = None
        count = 0
        while current and count < posisi:
            prev = current
            current = current.next
            count += 1
        if not current:
            print("Posisi melebihi panjang Linked List")
            return
        prev.next = new_node
        new_node.next = current

    def hapus_di_awal(self):
        if not self.head:
            print("Linked List kosong")
            return
        self.head = self.head.next

    def hapus_di_akhir(self):
        if not self.head:
            print("Linked List kosong")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def hapus_di_posisi(self, posisi):
        if not self.head:
            print("Linked List kosong")
            return
        if posisi == 0:
            self.hapus_di_awal()
            return
        current = self.head
        prev = None
        count = 0
        while current and count < posisi:
            prev = current
            current = current.next
            count += 1
        if not current:
            print("Posisi melebihi panjang Linked List")
            return
        prev.next = current.next

    def tampilkan(self):
        if not self.head:
            print("Linked List kosong")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def quicksort(arr, key=lambda x: x['id'], reverse=False):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        left = [x for x in arr[1:] if key(x) < key(pivot)]
        right = [x for x in arr[1:] if key(x) >= key(pivot)]
        
        if reverse:
            return quicksort(right, key, reverse) + [pivot] + quicksort(left, key, reverse)
        else:
            return quicksort(left, key, reverse) + [pivot] + quicksort(right, key, reverse)

class TokoIkanHias:
    def __init__(self):
        self.ikan_hias = LinkedList()
        self.counter = 0

    def tambah_ikan_hias(self, nama, jenis, makanan, jenis_kelamin, harga, stok):
        self.counter += 1
        new_ikan = {
            'id': self.counter,
            'nama': nama,
            'jenis': jenis,
            'makanan': makanan,
            'jenis_kelamin': jenis_kelamin,
            'harga': harga,
            'stok': stok,
        }
        self.ikan_hias.tambah_di_akhir(new_ikan)

    def lihat_ikan_hias(self):
        print("Daftar Ikan Hias:")
        print("ID\tNama\t\tJenis\tMakanan\t\tJenis Kelamin\tHarga\tStok")
        print("----------------------------------------------------------------------------------------------------------------------------------")
        current = self.ikan_hias.head
        while current:
            ikan = current.data
            print(f"{ikan['id']}\t{ikan['nama']}\t{ikan['jenis']}\t{ikan['makanan']}\t\t{ikan['jenis_kelamin']}\t\t{ikan['harga']}\t{ikan['stok']}")
            current = current.next
        print("----------------------------------------------------------------------------------------------------------------------------------")

    def ubah_ikan_hias(self, id_ikan, field, ikan_baru):
        current = self.ikan_hias.head
        while current:
            if current.data['id'] == id_ikan:
                current.data[field] = ikan_baru
                print("=====================")
                print("Ikan Berhasil Diubah")
                print("=====================")
                return
            current = current.next
        print("=====================")
        print("Ikan Tidak Ditemukan")
        print("=====================")

    def hapus_ikan_hias(self, id_ikan):
        current = self.ikan_hias.head
        prev = None
        while current:
            if current.data['id'] == id_ikan:
                if not prev:
                    self.ikan_hias.hapus_di_awal()
                else:
                    prev.next = current.next
                print("===========================")
                print("Ikan Hias Berhasil Dihapus")
                print("===========================")
                return
            prev = current
            current = current.next
        print("=====================")
        print("Ikan Tidak Ditemukan")
        print("=====================")

    def sorting(self, key='id', order='ascending'):
        current = self.ikan_hias.head
        ikan_hias_list= []
        while current:
            ikan_hias_list.append(current.data)
            current = current.next
        reverse = False if order.lower() == 'ascending' else True
        key_func = lambda x: x[key]
        sorted_ikan_hias = quicksort(ikan_hias_list, key=key_func, reverse=reverse)
        self.ikan_hias = LinkedList()
        for idx, ikan in enumerate(sorted_ikan_hias):
            self.tambah_ikan_hias(ikan['nama'], ikan['jenis'], ikan['makanan'], ikan['jenis_kelamin'], ikan['harga'], ikan['stok'])
            self.ikan_hias.head.data['id'] = idx + 1


        print("Hasil Sorting:")
        self.lihat_ikan_hias()

    def jumpsearch(self, arr, x, n):
        step = math.floor(math.sqrt(n))
        prev = 0
        while arr[int(min(step, n) - 1)] < x:
            prev = step
            step += math.sqrt(n)
            if prev >= n:
                return -1
        while arr[int(prev)] < x:
            prev += 1
            if prev == min(step, n):
                return -1
        if arr[int(prev)] == x:
            return int(prev)
        return -1

    def cari_berdasarkan_harga(self, harga):
        current = self.ikan_hias.head
        while current:
            if current.data['harga'] == harga:
                print("Ikan dengan harga", harga, "ditemukan:", current.data)
                return
            current = current.next
        print("Ikan dengan harga", harga, "tidak ditemukan.")

    def cari_berdasarkan_id(self, id_ikan):
        current = self.ikan_hias.head
        while current:
            if current.data['id'] == id_ikan:
                print("Ikan dengan ID", id_ikan, "ditemukan:", current.data)
                return
            current = current.next
        print("Ikan dengan ID", id_ikan, "tidak ditemukan.")


def main():
    toko = TokoIkanHias()

    toko.tambah_ikan_hias("Ikan Guppy", "Guppy", "Pelet", "Jantan", 15.0, 20)
    toko.tambah_ikan_hias("Ikan Koi", "Koi", "Serangga Kecil", "Betina", 50.0, 10)
    toko.tambah_ikan_hias("Ikan Discus", "Discus", "Cacing Sutra", "Jantan", 100.0, 5)
    toko.tambah_ikan_hias("Ikan Mas", "Mas", "pelet", "Jantan", 25.000, 15)
    toko.tambah_ikan_hias("Ikan cupang", "cupang", "pelet", "Jantan", 75.000, 35)
    toko.tambah_ikan_hias("Ikan Badut", "Nemo", "planktont", "Jantan", 250.000, 5)
    toko.tambah_ikan_hias("Ikan Louhan", "Louhan", "cacing sutra", "Betina", 10.000, 40)

    while True:
        print("-------------------------")
        print("Pilihan Menu Ikan Hias ")
        print("-------------------------")
        print("1. Tambah ikan hias")
        print("2. Lihat ikan hias")
        print("3. Ubah ikan hias")
        print("4. Hapus ikan hias")
        print("5. Sorting ikan hias")
        print("6. Cari ikan hias berdasarkan harga")
        print("7. Cari ikan hias berdasarkan ID")
        print("8. Keluar Program")
        print("-------------------------")

        pilihan = input("Masukkan Pilihan Anda:")

        if pilihan == '1':
            nama = input("Masukkan Nama Ikan Hias:")
            jenis = input("Masukkan Jenis Ikan Hias:")
            makanan = input("Masukkan Jenis Makanan Ikan Hias:")
            jenis_kelamin = input("Masukkan Jenis Kelamin Ikan Hias:")
            harga = float(input("Masukkan Harga Ikan Hias:"))
            stok = int(input("Masukkan Stok Ikan Hias:"))
            toko.tambah_ikan_hias(nama, jenis, makanan, jenis_kelamin, harga, stok)

        elif pilihan == '2':
            toko.lihat_ikan_hias()

        elif pilihan == '3':
            id_ikan = int(input("Masukkan ID Ikan Hias Yang Ingin Diubah:"))
            field = input("Masukkan Nama field Yang Ingin Diubah (nama/jenis/makanan/jenis_kelamin/harga/stok):")
            ikan_baru = input("Masukkan Ikan Hias Baru:")
            toko.ubah_ikan_hias(id_ikan, field, ikan_baru)

        elif pilihan == '4':
            id_ikan = int(input("Masukkan ID Ikan Hias Yang Ingin Dihapus:"))
            toko.hapus_ikan_hias(id_ikan)

        elif pilihan == '5':
            key_input = input("Masukkan atribut untuk sorting (1. id, 2. harga): ")
            key = 'id' if key_input == '1' else 'harga'
            order_input = input("Masukkan urutan sorting (1. ascending, 2. descending): ")
            order = 'ascending' if order_input == '1' else 'descending'
            toko.sorting(key, order)

        elif pilihan == '6':
            harga = float(input("Masukkan harga yang ingin dicari: "))
            toko.cari_berdasarkan_harga(harga)

        elif pilihan == '7':
            id_ikan = int(input("Masukkan ID Ikan Hias yang ingin dicari: "))
            toko.cari_berdasarkan_id(id_ikan)

        elif pilihan == '8':
            print("Keluar Dari Program")
            break

        else:
            print("Pilihan Tidak Valid. Silahkan Masukkan Pilihan Yang Benar")

if __name__ == "__main__":
    main()

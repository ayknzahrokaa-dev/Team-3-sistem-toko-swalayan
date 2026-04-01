from barang import Barang

class Makanan(Barang):
    def __init__(self, nama, harga_jual, harga_modal, stok, tanggal_kadaluarsa, diskon):
        super().__init__(nama, harga_jual, harga_modal, stok, "Makanan", diskon)
        self.tanggal_kadaluarsa = tanggal_kadaluarsa

    def info_barang(self):
        return f"{self.nama} (Makanan)"
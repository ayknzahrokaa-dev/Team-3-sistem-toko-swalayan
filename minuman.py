from barang import Barang

class Minuman(Barang):
    def __init__(self, nama, harga_jual, harga_modal, stok, volume, diskon):
        super().__init__(nama, harga_jual, harga_modal, stok, "Minuman")
        self.volume = volume
        self.diskon = diskon

    def info_barang(self):
        return f"{self.nama} (Minuman)"
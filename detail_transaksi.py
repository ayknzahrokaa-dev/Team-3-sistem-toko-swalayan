class DetailTransaksi:
    def __init__(self, barang, jumlah):
        self.barang = barang
        self.jumlah = jumlah
        self.subtotal = self.hitung_subtotal()

    def hitung_subtotal(self):
        return self.barang.harga_jual * self.jumlah
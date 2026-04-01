from transaksi_penjualan import TransaksiPenjualan

class TokoSwalayan:
    def __init__(self):
        self.daftar_barang = []
        self.daftar_transaksi = []

    def tambah_barang(self, barang):
        self.daftar_barang.append(barang)

    def cari_barang(self, nama):
        for b in self.daftar_barang:
            if b.nama == nama:
                return b
        return None

    def buat_transaksi(self, pelanggan=None):
        transaksi = TransaksiPenjualan()
        self.daftar_transaksi.append(transaksi)
        return transaksi
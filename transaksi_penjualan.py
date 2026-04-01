from diskon_mixin import DiskonMixin
from log_mixin import LogMixin
from detail_transaksi import DetailTransaksi
from datetime import datetime
from metode_pembayaran import MetodePembayaran

class TransaksiPenjualan(DiskonMixin, LogMixin):
    def __init__(self):
        self.id_transaksi = datetime.now().strftime("%Y%m%d%H%M%S")
        self.tanggal = datetime.now()
        self.daftar_item = []
        self.total = 0

    def tambah_item(self, barang, jumlah):
        barang.kurangi_stok(jumlah)
        item = DetailTransaksi(barang, jumlah)
        self.daftar_item.append(item)
        self.log(f"Tambah {barang.nama} sebanyak {jumlah}")

    def hitung_total(self):
        self.total = sum(item.subtotal for item in self.daftar_item)
        return self.total

    def total_setelah_diskon_persen(self, persen):
        total = self.hitung_total()
        return self.hitung_diskon_persen(total, persen)

    def total_setelah_diskon_tetap(self, nominal):
        total = self.hitung_total()
        return self.hitung_diskon_tetap(total, nominal)
    
    def proses_pembayaran(self, metode_pembayaran, total_bayar):
        return metode_pembayaran.bayar(total_bayar)
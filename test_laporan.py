import unittest
from makanan import Makanan
from transaksi_penjualan import TransaksiPenjualan
from laporan_stok import LaporanStok
from laporan_penjualan import LaporanPenjualan

class TestLaporan(unittest.TestCase):

    def setUp(self):
        self.barang = Makanan("Roti", 10000, 8000, 10, "2026-12-01")
        self.transaksi = TransaksiPenjualan()
        self.transaksi.tambah_item(self.barang, 2)
        self.transaksi.hitung_total()

    # ✅ Test laporan stok sesuai
    def test_laporan_stok(self):
        laporan = LaporanStok([self.barang])
        hasil = laporan.generate()

        self.assertEqual(hasil[0][0], "Roti")
        self.assertEqual(hasil[0][1], self.barang.stok)

    # ✅ Test laporan penjualan sesuai
    def test_laporan_penjualan(self):
        laporan = LaporanPenjualan([self.transaksi])
        hasil = laporan.generate()

        self.assertEqual(hasil[0], self.transaksi.total)

if __name__ == "__main__":
    unittest.main()
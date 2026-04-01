import unittest
from makanan import Makanan
from transaksi_penjualan import TransaksiPenjualan

class TestTransaksi(unittest.TestCase):

    def setUp(self):
        self.barang = Makanan("Roti", 10000, 8000, 10, "2026-12-01")
        self.transaksi = TransaksiPenjualan()

    #  Test stok berkurang
    def test_stok_berkurang(self):
        self.transaksi.tambah_item(self.barang, 3)
        self.assertEqual(self.barang.stok, 7)

    #  Test stok tidak cukup
    def test_stok_tidak_cukup(self):
        with self.assertRaises(ValueError):
            self.transaksi.tambah_item(self.barang, 20)

    #  Test total transaksi
    def test_total_transaksi(self):
        self.transaksi.tambah_item(self.barang, 2)
        total = self.transaksi.hitung_total()
        self.assertEqual(total, 20000)

if __name__ == "__main__":
    unittest.main()
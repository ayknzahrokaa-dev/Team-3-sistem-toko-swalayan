import unittest
from transaksi_penjualan import TransaksiPenjualan

class TestDiskon(unittest.TestCase):

    def setUp(self):
        self.transaksi = TransaksiPenjualan()

    # ✅ Test diskon persen
    def test_diskon_persen(self):
        total = 10000
        hasil = self.transaksi.hitung_diskon_persen(total, 10)
        self.assertEqual(hasil, 9000)

    # ✅ Test diskon tetap
    def test_diskon_tetap(self):
        total = 10000
        hasil = self.transaksi.hitung_diskon_tetap(total, 2000)
        self.assertEqual(hasil, 8000)

    # ❌ Test diskon tidak boleh minus
    def test_diskon_tidak_minus(self):
        total = 5000
        hasil = self.transaksi.hitung_diskon_tetap(total, 10000)
        self.assertEqual(hasil, 0)

if __name__ == "__main__":
    unittest.main()
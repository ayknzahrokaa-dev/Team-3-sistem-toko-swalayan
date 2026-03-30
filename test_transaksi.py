import unittest
from makanan import Makanan
from transaksi_penjualan import TransaksiPenjualan

class TestTransaksi(unittest.TestCase):

    def test_stok_berkurang(self):
        barang = Makanan("Roti", 10000, 8000, 10, "2026-12-01")
        transaksi = TransaksiPenjualan()

        transaksi.tambah_item(barang, 2)

        self.assertEqual(barang.stok, 8)

    def test_total(self):
        barang = Makanan("Roti", 10000, 8000, 10, "2026-12-01")
        transaksi = TransaksiPenjualan()

        transaksi.tambah_item(barang, 2)
        self.assertEqual(transaksi.hitung_total(), 20000)

if __name__ == "__main__":
    unittest.main()
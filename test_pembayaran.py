import unittest
from pembayaran_tunai import PembayaranTunai
from pembayaran_ewallet import PembayaranEWallet

class TestPembayaran(unittest.TestCase):

    #  Test pembayaran tunai sukses
    def test_pembayaran_tunai_sukses(self):
        tunai = PembayaranTunai(20000)
        kembalian = tunai.bayar(15000)
        self.assertEqual(kembalian, 5000)

    #  Test pembayaran tunai gagal
    def test_pembayaran_tunai_gagal(self):
        tunai = PembayaranTunai(10000)
        with self.assertRaises(ValueError):
            tunai.bayar(15000)

    #  Test e-wallet sukses
    def test_ewallet_sukses(self):
        ewallet = PembayaranEWallet(50000)
        sisa = ewallet.bayar(20000)
        self.assertEqual(sisa, 30000)

    #  Test e-wallet gagal
    def test_ewallet_gagal(self):
        ewallet = PembayaranEWallet(10000)
        with self.assertRaises(ValueError):
            ewallet.bayar(20000)

if __name__ == "__main__":
    unittest.main()
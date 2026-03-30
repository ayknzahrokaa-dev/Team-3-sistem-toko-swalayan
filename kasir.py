from user import User

class Kasir(User):
    def role(self):
        return "Kasir"

    def buat_transaksi(self, toko):
        return toko.buat_transaksi()
from user import User

class Admin(User):
    def role(self):
        return "Admin"

    def tambah_barang(self, toko, barang):
        toko.tambah_barang(barang)
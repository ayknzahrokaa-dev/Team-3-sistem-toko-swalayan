from abc import ABC, abstractmethod
from validation_mixin import ValidationMixin

class Barang(ABC, ValidationMixin):
    def __init__(self, nama, harga_jual, harga_modal, stok, kategori):
        self.validate_nama(nama)
        self.validate_harga(harga_jual)
        self.validate_stok(stok)

        self.nama = nama
        self.harga_jual = harga_jual
        self.__harga_modal = harga_modal
        self.__stok = stok
        self.kategori = kategori

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, value):
        if value < 0:
            raise ValueError("Stok tidak boleh negatif")
        self.__stok = value

    def tambah_stok(self, jumlah):
        self.__stok += jumlah

    def kurangi_stok(self, jumlah):
        if jumlah > self.__stok:
            raise ValueError("Stok tidak cukup")
        self.__stok -= jumlah

    def get_harga_modal(self):
        return self.__harga_modal

    @abstractmethod
    def info_barang(self):
        pass
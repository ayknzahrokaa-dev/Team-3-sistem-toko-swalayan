class ValidationMixin:

    def validate_harga(self, harga):
        if harga <= 0:
            raise ValueError("Harga harus lebih dari 0")

    def validate_stok(self, stok):
        if stok < 0:
            raise ValueError("Stok tidak boleh negatif")

    def validate_nama(self, nama):
        if not nama or not nama.strip():
            raise ValueError("Nama tidak boleh kosong")
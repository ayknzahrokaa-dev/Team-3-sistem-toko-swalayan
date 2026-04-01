from makanan import Makanan
from minuman import Minuman
from rumah_tangga import RumahTangga
from toko import TokoSwalayan
from laporan_stok import LaporanStok
from laporan_penjualan import LaporanPenjualan
from admin import Admin
from kasir import Kasir
from pelanggan import Pelanggan
from pembayaran_tunai import PembayaranTunai
from pembayaran_ewallet import PembayaranEWallet

def main():
    print("=== SISTEM TOKO SWALAYAN ===\n")

    admin = Admin("A01", "Budi")
    kasir = Kasir("K01", "Siti")
    pelanggan = Pelanggan("P01", "Andi")

    print("User Sistem:")
    print(admin.info_user())
    print(kasir.info_user())
    print()

    toko = TokoSwalayan()

    print("Admin menambahkan barang...\n")
    barang1 = Makanan("Roti", 10000, 8000, 20,"2026-12-01",diskon=10,)
    barang2 = Minuman("Teh Botol", 5000, 3000, 30, "250ml",diskon=0, )
    barang3 = RumahTangga("Sabun Cuci", 15000, 10000, 25, "Deterjen", diskon=5)


    admin.tambah_barang(toko, barang1)
    admin.tambah_barang(toko, barang2)
    admin.tambah_barang(toko, barang3)

    print("Daftar Barang:")
    for b in toko.daftar_barang:
        print(f"- {b.info_barang()} | Harga: {b.harga_jual} | Stok: {b.stok}")
    print()

    # TRANSAKSI
    transaksi = toko.buat_transaksi(pelanggan)

    transaksi.tambah_item(barang1, 2)
    transaksi.tambah_item(barang2, 3)

    total = transaksi.hitung_total()

    # PEMBAYARAN (TUNAI SAJA)
    print("\nMemproses pembayaran...\n")

    pembayaran = PembayaranTunai(50000)
    kembalian = pembayaran.bayar(total)

    # STRUK
    transaksi.tampilkan_struk(
        metode="Tunai",
        jumlah_bayar=50000,
        kembalian=kembalian
    )

    print("Stok setelah transaksi:")
    for b in toko.daftar_barang:
        print(f"- {b.nama}: {b.stok}")
    print()

    print("=== LAPORAN STOK ===")
    laporan_stok = LaporanStok(toko.daftar_barang)
    for nama, stok in laporan_stok.generate():
        print(f"{nama}: {stok}")
    print()


    print("=== LAPORAN PENJUALAN ===")
    laporan_penjualan = LaporanPenjualan(toko.daftar_transaksi)
    for i, total in enumerate(laporan_penjualan.generate(), start=1):
        print(f"Transaksi {i}: Rp{total}")

    print("\n=== SELESAI ===")


if __name__ == "__main__":
    main()
from makanan import Makanan
from minuman import Minuman
from toko import TokoSwalayan
from laporan_stok import LaporanStok
from laporan_penjualan import LaporanPenjualan
from admin import Admin
from kasir import Kasir
from pembayaran_tunai import PembayaranTunai
from pembayaran_ewallet import PembayaranEWallet

def main():
    print("=== SISTEM TOKO SWALAYAN ===\n")

    admin = Admin("A01", "Budi")
    kasir = Kasir("K01", "Siti")

    print("User Sistem:")
    print(admin.info_user())
    print(kasir.info_user())
    print()

    toko = TokoSwalayan()

    print("Admin menambahkan barang...\n")
    barang1 = Makanan("Roti", 10000, 8000, 20, "2026-12-01")
    barang2 = Minuman("Teh Botol", 5000, 3000, 30, "250ml")

    admin.tambah_barang(toko, barang1)
    admin.tambah_barang(toko, barang2)

    print("Daftar Barang:")
    for b in toko.daftar_barang:
        print(f"- {b.info_barang()} | Harga: {b.harga_jual} | Stok: {b.stok}")
    print()

    print("Kasir melakukan transaksi...\n")
    transaksi = kasir.buat_transaksi(toko)

    transaksi.tambah_item(barang1, 2)  # beli 2 roti
    transaksi.tambah_item(barang2, 3)  # beli 3 teh

    total = transaksi.hitung_total()
    print(f"Total sebelum diskon: Rp{total}")

    total_diskon_persen = transaksi.total_setelah_diskon_persen(10)
    print(f"Total setelah diskon 10%: Rp{int(total_diskon_persen)}")

    total_diskon_tetap = transaksi.total_setelah_diskon_tetap(5000)
    print(f"Total setelah diskon Rp5000: Rp{int(total_diskon_tetap)}\n")

    total_bayar = transaksi.total_setelah_diskon_persen(10)

    print(f"Total yang harus dibayar: Rp{int(total_bayar)}\n")

    print("Pembayaran Tunai:")
    tunai = PembayaranTunai(50000)
    kembalian = transaksi.proses_pembayaran(tunai, total_bayar)
    print(f"Kembalian: Rp{int(kembalian)}\n")

    print("Pembayaran E-Wallet:")
    ewallet = PembayaranEWallet(100000)
    sisa = transaksi.proses_pembayaran(ewallet, total_bayar)
    print(f"Sisa saldo: Rp{int(sisa)}\n")

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
def phan_nguyen_phep_chia(a, b):
    if b == 0:
        return "Lỗi: Không thể chia cho 0"
    
    ket_qua = a // b
    return ket_qua

# Ví dụ sử dụng hàm
so_chia = int(input("nhập số chia :"))
so_bi_chia = int(input("nhập số bị chia"))

ket_qua_phep_chia = phan_nguyen_phep_chia(so_chia, so_bi_chia)
print("Phần nguyên của {}/{} là: {}".format(so_chia, so_bi_chia, ket_qua_phep_chia))

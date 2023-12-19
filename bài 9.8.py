def la_so_hoan_hao(so):
    if so <= 0:
        return False

    tong_uoc_so = 0
    for i in range(1, so):
        if so % i == 0:
            tong_uoc_so += i

    return tong_uoc_so == so

# Ví dụ sử dụng hàm
so_kiem_tra = int(input("nhập số kiểm tra :"))
ket_qua = la_so_hoan_hao(so_kiem_tra)

if ket_qua:
    print("{} là số hoàn hảo.".format(so_kiem_tra))
else:
    print("{} không phải là số hoàn hảo.".format(so_kiem_tra))

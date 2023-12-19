# Hàm tính diện tích và chu vi của hình tròn
tinh_dien_tich_chu_vi_hinh_tron = lambda r: (3.14159 * r**2, 2 * 3.14159 * r)

# Hàm tính diện tích và chu vi của hình chữ nhật
tinh_dien_tich_chu_vi_hinh_chu_nhat = lambda a, b: (a * b, 2 * (a + b))

# Ví dụ sử dụng hàm cho hình tròn
ban_kinh_hinh_tron = int(input("nhập bán kính r :"))
dien_tich_hinh_tron, chu_vi_hinh_tron = tinh_dien_tich_chu_vi_hinh_tron(ban_kinh_hinh_tron)
print("Diện tích hình tròn:", dien_tich_hinh_tron)
print("Chu vi hình tròn:", chu_vi_hinh_tron)

# Ví dụ sử dụng hàm cho hình chữ nhật
chieu_dai_hinh_chu_nhat = int(input("nhập chiêu dài hình chữ nhật :"))
chieu_rong_hinh_chu_nhat = int(input("nhập chiều rộng hình chữ nhật :"))
dien_tich_hinh_chu_nhat, chu_vi_hinh_chu_nhat = tinh_dien_tich_chu_vi_hinh_chu_nhat(chieu_dai_hinh_chu_nhat, chieu_rong_hinh_chu_nhat)
print("Diện tích hình chữ nhật:", dien_tich_hinh_chu_nhat)
print("Chu vi hình chữ nhật:", chu_vi_hinh_chu_nhat)

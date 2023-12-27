# 13.1
try:
    # Nhập tên tập tin từ người dùng
    ten_tap_tin = input("Nhập tên tập tin muốn đọc: ")

    # Mở tập tin trong chế độ đọc
    with open(ten_tap_tin, 'r', encoding='utf-8') as file:
        # Đọc nội dung của tập tin
        noi_dung = file.read()

        # In nội dung
        print("Nội dung của tập tin:")
        print(noi_dung)

except FileNotFoundError:
    print(f"Tập tin '{ten_tap_tin}' không tồn tại.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")

# 13.2
import re

try:
    # Nhập tên tập tin từ người dùng
    ten_tap_tin = input("Nhập tên tập tin muốn đọc: ")

    # Mở tập tin trong chế độ đọc
    with open(ten_tap_tin, 'r', encoding='utf-8') as file:
        # Đọc nội dung của tập tin
        noi_dung = file.read()

        # Đếm số dòng
        so_dong = noi_dung.count('\n') + 1

        # Đếm số ký tự
        so_ky_tu = len(noi_dung)

        # Đếm số từ
        so_tu = len(re.findall(r'\b\w+\b', noi_dung))

        # In thông tin
        print(f"Số dòng: {so_dong}")
        print(f"Số ký tự: {so_ky_tu}")
        print(f"Số từ: {so_tu}")

except FileNotFoundError:
    print(f"Tập tin '{ten_tap_tin}' không tồn tại.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")

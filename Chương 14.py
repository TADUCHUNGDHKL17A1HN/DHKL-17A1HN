# Bài 14.1
def kiem_tra_tam_giac(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Độ dài các cạnh phải là số dương và khác 0.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Độ dài các cạnh không thỏa mãn là một tam giác.")

    # Nếu không có ngoại lệ, thông báo là tam giác hợp lệ
    print("Đây là một tam giác hợp lệ.")

try:
    # Nhập độ dài các cạnh từ người dùng
    a = float(input("Nhập độ dài cạnh a: "))
    b = float(input("Nhập độ dài cạnh b: "))
    c = float(input("Nhập độ dài cạnh c: "))

    # Gọi hàm kiểm tra tam giác
    kiem_tra_tam_giac(a, b, c)

except ValueError as ve:
    print(f"Lỗi: {ve}")

except Exception as e:
    print(f"Có lỗi xảy ra: {e}")

# Bài 14.2
class InputError(Exception):
    pass

def nhap_so_nguyen_duong():
    while True:
        try:
            so_nguyen = int(input("Nhập một số nguyên dương (nhập 0 để kết thúc): "))
            
            if so_nguyen == 0:
                break  # Kết thúc khi nhập 0
            
            if so_nguyen < 0:
                raise InputError("Lỗi: Số không được là số nguyên âm.")
            
            if 'prev_input' in locals() and so_nguyen == prev_input:
                raise InputError("Lỗi: Bạn đã nhập 4 số nguyên dương giống nhau liên tiếp.")
            
            prev_input = so_nguyen
            
            print("Nhập thành công:", so_nguyen)

        except ValueError:
            print("Lỗi: Bạn đã nhập một chuỗi không phải số nguyên.")
        
        except InputError as ie:
            print(ie)

if __name__ == "__main__":
    nhap_so_nguyen_duong()

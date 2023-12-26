# 10.1
a,b,c,d=eval(input("Nhập  a,b,c,d :"))
print("giá trị lớn nhất là :",max(a,b,c,d))
# 10.2
x=int(input(" Nhập x :"))
print("|x| = ",abs(x))
# 10.3
import math
n=int(input("Nhập giá trị của n :"))
x=int(input("Nhập giá trị của x :"))
s=(math.pow(x,2)+1)*n
print(s)
# 10.4
import math
n=int(input("Nhập giá trị của n :"))
x=int(input("Nhập giá trị của x :"))
A=(math.pow((math.pow(x,2)+x+1),n)+math.pow(math.pow(x,2)-x+1,n))
print(A)
# 10.5
def kiem_tra_zip_code(zip_code):
    """
    Kiểm tra dữ liệu ZIP code ở Việt Nam.

    Parameters:
    - zip_code (str): Mã vùng cần kiểm tra.

    Returns:
    - True nếu ZIP code hợp lệ, False nếu không hợp lệ."
    """
    if not isinstance(zip_code, str):
        return False
    
    # Kiểm tra độ dài của ZIP code (mã vùng Việt Nam có độ dài 6 ký tự)
    if len(zip_code) != 6:
        return False

    # Kiểm tra xem tất cả các ký tự có phải là số không
    if not zip_code.isdigit():
        return False

    return True

# Sử dụng hàm kiểm tra
zip_code = "700000"
if kiem_tra_zip_code(zip_code):
    print(f"{zip_code} là mã vùng hợp lệ.")
else:
    print(f"{zip_code} không phải là mã vùng hợp lệ.")

# 10.6
import math
 
print("Giải phương trình bậc 2: ax2 + bx + c = 0 (a, b khác 0)")

# Nhập số a, b và kiểm tra điều kiện khác 0
a = float(input("Mời bạn nhập hệ số a: "))
while True:
    if a == 0:
        a = float(input("Số a phải khác 0. Mời nhập lại số a: "))
    else:
        break
    
b = float(input("Mời bạn nhập hệ số b: "))
while True:
    if b == 0:
        b = float(input("Số b phải khác 0. Mời nhập lại số b: "))
    else:
        break
    
# Nhập số c
c = float(input("Mời bạn nhập hệ số c: "))

# Tính Delta
delta = b**2 - 4 * a * c

# Tìm nghiệm của phương trình
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có nghiệm kép x1 = x2 = ", -(b / (2 * a)) )
else:
    print("Phương trình có hai nghiệm phân biệt:")
    print("x1 = ", (-(b) + math.sqrt(delta))/(2*a) )
    print("x2 = ", (-(b) - math.sqrt(delta))/(2*a) )
# 10.7
import string

def xu_ly_chuoi(chuoi):
    # Loại bỏ khoảng trắng ở đầu và cuối chuỗi
    chuoi = chuoi.strip()

    # In chuỗi với ký tự đầu viết hoa
    chuoi_in_hoa = chuoi.capitalize()
    print(f"Chuỗi sau khi in hoa: {chuoi_in_hoa}")

    # Đếm và in ra số lần chuỗi con xuất hiện trong chuỗi
    s_sub = input("Nhập chuỗi con cần kiểm tra: ")
    so_lan_xuat_hien = chuoi.count(s_sub)
    print(f"Số lần chuỗi s_sub '{s_sub}' xuất hiện trong chuỗi: {so_lan_xuat_hien}")

    # Nhập từ muốn thay thế và từ thay thế
    s_find = input("Nhập từ muốn thay thế: ")
    s_replace = input(f"Nhập từ thay thế '{s_find}' bằng: ")

    # Thực hiện thay thế và in ra chuỗi đã thay thế
    chuoi_thay_the = chuoi.replace(tu_thay_the, tu_thay_the_bang)
    print(f"Chuỗi sau khi thay thế: {chuoi_thay_the}")

# Sử dụng hàm
chuoi_input = input("Nhập chuỗi cần xử lý: ")
xu_ly_chuoi(chuoi_input)
import string

def xu_ly_chuoi(chuoi):
    """
    Xử lý chuỗi theo yêu cầu:
    - Loại bỏ khoảng trắng ở đầu và cuối chuỗi.
    - In chuỗi với ký tự đầu viết hoa.
    - Đếm và in ra số lần chuỗi con xuất hiện trong chuỗi.
    - Nhập từ muốn thay thế và từ thay thế, in ra chuỗi đã thay thế.

    Parameters:
    - chuoi (str): Chuỗi cần xử lý.

    Returns:
    - None.
    """
    # Loại bỏ khoảng trắng ở đầu và cuối chuỗi
    chuoi = chuoi.strip()

    # In chuỗi với ký tự đầu viết hoa
    chuoi_in_hoa = chuoi.capitalize()
    print(f"Chuỗi sau khi in hoa: {chuoi_in_hoa}")

    # Đếm và in ra số lần chuỗi con xuất hiện trong chuỗi
    chuoi_con = input("Nhập chuỗi con cần kiểm tra: ")
    so_lan_xuat_hien = chuoi.count(chuoi_con)
    print(f"Số lần chuỗi con '{chuoi_con}' xuất hiện trong chuỗi: {so_lan_xuat_hien}")

    # Nhập từ muốn thay thế và từ thay thế
    tu_thay_the = input("Nhập từ muốn thay thế: ")
    tu_thay_the_bang = input(f"Nhập từ thay thế '{tu_thay_the}' bằng: ")

    # Thực hiện thay thế và in ra chuỗi đã thay thế
    chuoi_thay_the = chuoi.replace(tu_thay_the, tu_thay_the_bang)
    print(f"Chuỗi sau khi thay thế: {chuoi_thay_the}")

# Sử dụng hàm



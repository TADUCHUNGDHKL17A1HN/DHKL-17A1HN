# hàm kiểm tra số nguyên tố
def tinh_so_nt(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        return True
n=int(input("nhập số tự nhiên :"))
if tinh_so_nt(n):
    print(n,"là số nguyên tố ")
else:
    print(n,"không phải là số nguyên tố ")
    
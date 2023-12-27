# hàm tìm số nguyên tố 
def is_prime(n):
    if n<=1:
        return False
    for i in range (2,n):
        if n%i==0:
            return False
    return True
n=int(input("nhập số tự nhiên "));
if is_prime(n):
    print(f"{n} là số nguyên tố ")
else:
    print(f"{n} không phải là số nguyên tố ")

# hàm giải phương trình bậc 1
def giai_pt_bac_1():
    a=int(input("nhập a"));
    b=int(input("nhập b"));
    print("giải phương trình bậc nhât ax+b=0")
    if(a==0 and b!=0):
        print(" phương trình vô nghiệm")
    elif(a==0 and b==0):
        print("phương trình vô số nghiệm")
    else:
        x=(-b)/a
        print("phương trinh có nghiệm x",x) 

giai_pt_bac_1()
# hàm giải  diện tích tam giác 
def dien_tich_tam_giac():
    import math
    a=float(input("nhập cạnh a :"));
    b=float(input("nhập cạnh b :"));
    c=float(input("nhập cạnh c :"));
    p=(a+b+c)/2
    dt=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("diện tích tam giác ",p)

dien_tich_tam_giac()

# hàm tính biểu thức s=(x^2+1)^n
def ham_bieu_thuc1():
    n=float(input("nhập số n :"));
    x=float(input("nhập số x :"));
    print(" tính giá trị biểu thức s=(x^2 + 1)^n ")
    s=(x*x + 1)**n
    print(" giá trị biểu thức :",s)

ham_bieu_thuc1()
# hàm tính biểu thức
def ham_bieu_thuc2():

    n=float(input("nhập số n:"));
    x=float(input("nhập số x:"));
    A=(x**2 + x + 1)**n +(x**2 - x +1)**n
    print("giá trị của biểu thức A :", A)

ham_bieu_thuc2()



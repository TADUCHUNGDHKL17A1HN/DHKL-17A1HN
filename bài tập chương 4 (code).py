#bài 4.1
so = float(input(" Nhập giá trị: "))
if so > 0:
    binh_phuong = so ** 2
    print(f"Bình phương của {so} là {binh_phuong}")
else:
    print("Số không phải là số dương.")
#bài 4.2
N = int(8)
if N > 0:
   for i in range(1, N + 1):
    print(i)    
else:
  print("N phải là số tự nhiên dương")
#bài
m = eval(input("Nhập giá trị m: "))
n = eval(input("Nhập giá trị n: "))
if n <= m:
   print("Vui lòng nhập giá trị m nhỏ hơn n")
else:
      print(f"các số chia hết trong khoảng từ {m} đến {n} là :")
      for x in range(1 , n+1):
         if x % m == 0:
            print(x)
#
A = int(input("nhập số 1: "))
B = int(input("nhập số 2: "))
C = int(input("nhập số 3: "))
#tìm max
Max = A
if A > B:
   print("Max trong 3 số là: ", A)
#bài 4.5
def ucln(a, b):
    while b:
        a, b = b, a % b
    return a
def bcnn(a, b):
    return abs(a * b) // ucln(a, b)
so1 = int(input("Nhập số thứ nhất: "))
so2 = int(input("Nhập số thứ hai: "))
result = bcnn(so1, so2)
print(f"BCNN của {so1} và {so2} là: {result}")
#bài 4.7
def tinh_tong_chu_so(N):
    chuoi_so = str(N)
    tong = 0
    for chu_so in chuoi_so:
        tong += int(chu_so)
    return tong
so_nguyen = int(input("Nhập một số nguyên: "))
tong_chu_so = tinh_tong_chu_so(so_nguyen)
print(f"Tổng các chữ số của {so_nguyen} là: {tong_chu_so}")
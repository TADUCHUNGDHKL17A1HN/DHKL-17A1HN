#bài 8.1
a = eval(input("nhập giá trị a:"))
b = eval(input("nhập giá trị b:"))
c = eval(input("nhập giá trị c:"))
d = eval(input("nhập giá trị d:"))
max_valua = max(a,b,c,d)
min_valua = min(a,b,c,d)
print("đây là số lớn  nhất:", max_valua)
print("đây là số nhỏ  nhất:", min_valua)
#bài 8.3
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
#bài 8.4
import math
a=float(input("nhập cạnh a :"));
b=float(input("nhập cạnh b :"));
c=float(input("nhập cạnh c :"));
p=(a+b+c)/2
dt=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("diện tích tam giác ",p)
#bài 8.5
x=int(input("nhập năm :"));
if ((x%4==0 and x%100!=0)or(x%400==0)):
    print("đây là năm nhuận")
else:
    print("đây không phải năm nhuận")
#bài 8.6
loaixe=int(input("nhập loại xe 4 chỗ hoặc 7 chỗ :"));
sokm=int(input("nhập số km :"));
tgtro=int(input("nhập thời gian chờ :"));
if (tgtro >=5):
    tientro=(tgtro-5)*800
    print("tiền chờ ",tientro)
else:
    print("05 phút đầu được miễn phí tiền trờ")
if(loaixe ==4):
    if(sokm<=20):
        tiendichuyen=12100*sokm
        tiencuoc=(tiendichuyen+tientro)
        print("tiền di chuyển ",tiendichuyen)
        print("tiên cước ",tiencuoc)
    else:
        tiendichuyen=(20*12100)+((sokm-20)*10000)
        tiencuoc=tiendichuyen+tientro
        print("tiền di chuyển ",tiendichuyen)
        print("tiên cước ",tiencuoc)
if(loaixe==7):
    if(sokm<=30):
        tiendichuyen=14100*sokm
        tiencuoc=tiendichuyen+tientro
        print("tiền di chuyển ",tiendichuyen)
        print("tiên cước ",tiencuoc)
    else:
        tiendichuyen=(30*14100)+((sokm-30)*12000)
        tiencuoc=tiendichuyen+tientro
        print("tiền di chuyển ",tiendichuyen)
        print("tiên cước ",tiencuoc)
#bài 8.7
x=int(input("nhập số điện :"));
if(x>0 and x<=50):
    td=x*1.678
    print("số tiền điện là :",td )
elif(x>=51 and x<=100):
    td=(50*1.678)+((x-50)*1.734)
    print("số tiền điện là :",td )
elif(x>=101 and x<=200):
    td=(50*1.678)+(50*1.734)+((x-100)*2.014)
    print("số tiền điện là :",td )
elif(x>=201 and x<=300):
    td=(50*1.678)+(50*1.734)+(100*2.014)+((x-200)*2.536)
    print("số tiền điện là :",td )
elif(x>=301 and x<=400):
    td=(50*1.678)+(50*1.734)+(100*2.014)+(100*2.536)+((x-300)*2.834)
    print("số tiền điện là :",td )
else:
    td=(50*1.678)+(50*1.734)+(100*2.014)+(100*2.536)+(100*2.834)+((x-400)*2.927)
    print("số tiền điện là :",td )
#bài 8.8
lp=int(input("nhập loại phòng từ 1-8:"));
sd=int(input(" nhập số đêm "));
if (lp ==1 ):
    print(" tên phòng Standard")
    if (sd >=2 and sd <= 3):
        tt=(1260000-(1260000*0.25))*sd
        print(" thành tiền =",tt)
    elif (sd >= 4):
        tt=(1260000-(1260000*0.3))*sd
        print(" thành tiền =",tt)
    else:
        tt=sd*1260000
        print(" thành tiên =",tt)
if (lp ==2):
    print(" tên phòng superior Garden View")
    if (sd>=2 and sd <=3):
        tt=(1550000-(1550000*0.25))*sd
        print(" thành tiên =",tt)
    elif(sd>=4):
        tt=(1550000-(1550000*0.3))*sd
        print(" thành tiên =",tt)
    else:
        tt=1550000*sd
        print(" thành tiền =",tt)
if(lp ==3):
    print("tên phòng Super Ocean View")
    if (sd >=2 and sd <=3):
        tt=(1830000-(1830000*0.25))*sd
        print(" thành tiền =",tt)
    elif(sd >=4):
        tt=(1830000-(1830000*0.3))*sd
        print(" thành tiền =",tt)
    else:
        tt=1830000*sd
        print(" thành tiền =",tt)
if(lp ==4):
    print("tên phòng Garden View Bungalow")
    if (sd >=2 and sd <=3):
        tt=(1830000-(1830000*0.25))*sd
        print(" thành tiền =",tt)
    elif(sd >=4):
        tt=(1830000-(1830000*0.3))*sd
        print(" thành tiền =",tt)
    else:
        tt=1830000*sd
        print(" thành tiền =",tt)
if(lp==5):
    print("tên phòng Pool View Bungalow")
    if (sd>=2 and sd<=3):
        tt=(2120000-(2120000*0.25))*sd
        print(" thành tiền =",tt)
    elif(sd>=4):
        tt=(2120000-(2120000*0.3))*sd
        print(" thành tiền =",tt)
    else:
        tt=2120000*sd
        print(" thành tiền =",tt)
if(lp==6):
     print("tên phòng Family Room ")
     if (sd>=2 and sd<=3):
            tt=(2120000-(2120000*0.25))*sd
            print(" thành tiền =",tt)
     elif(sd>=4):
            tt=(2120000-(2120000*0.3))*sd
            print(" thành tiền =",tt)
     else:
            tt=2120000*sd
            print(" thành tiền =",tt)
if (lp==7):
    print("tên phòng Beach Front Bungalow")
    if(sd>=2 and sd<=3):
        tt=(2540000-(2540000*0.25))*sd
        print(" thanh tiền =",tt)
    elif(sd>=4):
        tt=(2540000-(2540000*0.3))*sd
        print("  thành tiền =",tt)
    else:
        tt=2540000*sd
        print(" thành tiền =",tt)
if(lp==8):
    print("tên phòng VIP sea View")
    if (sd>=2 and sd<=3):
        tt=(4800000-(4800000*0.25))*sd
        print(" thành tiền =",tt)
    elif(sd>=4):
        tt=(4800000-(4800000*0.3))*sd
        print(" thành tiền =",tt)
    else:
        tt=4800000*sd
        print(" thành tiền =",tt)     
#bài 8.9
import time
def countdown (seconds) :
    while seconds > 0 :
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print("Countdown finished!")
countdown(10)
#bài 8.10
n=float(input("nhập số n :"));
x=float(input("nhập số x :"));
print(" tính giá trị biểu thức s=(x^2 + 1)^n ")
s=(x*x + 1)**n
print(" giá trị biểu thức :",s)
#bài 8.11
n=float(input("nhập số n:"));
x=float(input("nhập số x:"));
A=(x**x + x + 1)**n +(x**x - x +1)**n
print("giá trị của biểu thức A :", A)
#bài 8.12
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
#8.13
# A = tổng các số lẻ nhỏ hơn hoặc bằng n
# B = tổng các số chẵn nhỏ hơn hay bằng n
# C = tích các số từ 1 đến n
# D = tích các số chia hết cho 3
# E = tổng các cố nguyên tố nhỏ hơn hay bằng n
# F = tổng chuỗi đan dấu
import math
n = int(input("nhập số N: "))
def A(n):
    j = []
    a = 0
    for i in range(1,n):
        j.append(i)
    for v in j:
        a = a + v
    return print("A = ",a)
def B(n):
    j = []
    a = 0
    for i in range(1,n):
        if i%2==0:
            j.append(i)
    for v in j:
        a = a + v
    return print("B = ",a)
def C(n):
    j = []
    a = 1
    for i in range(1,n):
        j.append(i)
    for v in j:
        a = a*v
    return print("C = ",a)
def D(n):
    j = []
    a = 1
    for i in range(1,n):
        if i%3==0:
            j.append(i)
    for v in j:
        a = a + v
    return print("D = ",a)
def E(n):
    j = []
    a = 0
    for i in range(2,n+1):
        if i>0:
            for k in range(2,int(math.sqrt(i))+1):
                if i%k ==0:
                    break
            else:
                j.append(i)
    for v in j:
        a = a + v
    print("E = ",a)    
def F(n):
    j = []
    a = 1
    for i in range(1,n):
        j.append(i**-1)
    for v in j:
        if i%2==0:
            a = a + v
        else:
            a = a - v 
    return print("F = ",a - 1)
A(n)
B(n)
C(n)
D(n)
E(n)
F(n)
#bài 8.14
a = int(input("nhập số nguyên thứ 1:"))
b = int(input("nhập số nguyên thứ 2:"))
c = int(input("nhập số nguyên thứ 3:"))
S = a + b + c
print(f"S = {S}")
#bài 8.15
total = 0
while True:
    try:
        num = int(input("Nhập số nguyên (nhập 0 để kết thúc):"))
        if num == 0:
            break
        total += num
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ")
print("S=:", total)
#bài 8.16
def find_gcd(a,b):
    while b:
        a, b = b, a % b
    return a
a = int(input("Nhập số nguyên a:"))
b = int(input("Nhập số nguyên b:"))
gdc = find_gcd(a,b)
print(f"UCLN của {a} và {b} là: {find_gcd}")
#bài 8.17
def tim_ucln(a,b):
    while b:
        a,b = b,a%b
    return a
def tim_bcnn(a, b):
    return a* b// tim_ucln(a,b)
a = int(input("Nhập số nguyên a:"))
b = int(input("Nhập số nguyên b:"))
print(f"BCLN của {a} và {b} là {tim_bcnn(a,b)}")
#bài 8.18
def kiem_tra_so_hoan_hao(x):
    tong = 0
    for i in range(1,x):
        if x % i == 0:
            tong +=i
    return tong == x 
x = int(input("Nhập một số x:"))
if kiem_tra_so_hoan_hao(x):
    pritn(f"{x} là số hoàn hảo.")
else:
    print(f"{x} không phải là số hoàn hảo")
#bài 8.19
def dao_nguoc_day_so_so_le(n):
    day_so = list(range(1,2*n, 2))
    day_so_dao_nguoc = day_so[::-1]
    return day_so_dao_nguoc 
so_luong = int(input("Nhập số lượng số trong dãy:"))
ket_qua = dao_nguoc_day_so_so_le(so_luong)
print("Dãy số đâỏ ngược:", ket_qua)
#bài 8.20
import math
x=int(input("Nhap x:"))
ex=1
n=1
t=x
while math.fabs(t)>=0.0001:
    ex +=t
    n +=1
    t *=(x/n)
print("Gia tri gan dung cua e mu x la:",ex)



    


        





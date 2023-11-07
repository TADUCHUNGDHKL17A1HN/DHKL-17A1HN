#bài 6.1
print('**    **  ******  **      **      ******')
print('**    **  **      **      **      **  **')
print('********  ******  **      **      **  **')
print('**    **  **      **      **      **  **')
print('**    **  ******  ******  ******  ******')
#bài 6.2
x=10
y=5
print('x=10')
print('y=5')
print('tổng=',x+y)
print('Hiệu=',x-y)
print('Tích=',x*y)
print('thương=',x/y)
#bài 6.3
soluong=5
dongia=25000
thanhtien=soluong*dongia
print('tên hàng : sữa hộp vinamilk')
print('số lương',soluong)
print('dơn giá',dongia)
print('thành tiền',thanhtien)
#bài 6.4
a=(5-3)//2
b=8-(3*2)-(1+1)
print(a)
print(b)
#bài 6.5
a = int(input("nhập số lượng:"))
# nhap sl = 100
b = int(input("nhập đơn giá: "))
# nhap don gia = 5000
thanh_tien= a * b
print("thành tiền là :","\n",thanh_tien)
#bài 6.7
def c_to_f(DOC):
    DOF = (DOC * 9/5) + 32
    return DOF
DOC = float(input("Nhập nhiệt độ độ C: "))
DOF = c_to_f(DOC)
print(f"Nhiệt độ tương ứng ở độ F là: {DOF}°F")
#bài 6.8
a=(input("nhập chuỗi s1:"))
b=(input("nhập chuỗi s2:"))
c=(input("nhập chuỗi s3:"))
d=int(input("nhập index:"))
print("chiều dài chuỗi s1=",a)
print("chiều dài chuỗi s2=",b)
print("chiều dài chuỗi s3=",c)
print("chuỗi s4=",a[d:])
print("chuỗi s2 lặp lại 2 lần",b*2)
#bài 6.6
a=int(input("số kẹo alice có:",))
b=int(input("số kẹo bob có:",))
c=int(input("số kẹo carol có",))
print("số kẹo thừa:",(a+b+c)%3)
#bài 6.9
a=float(input("lãi suất 1 năm(%):"))
b=float(input("số tiền gửi:"))
c=float(input("số tháng gửi:"))
d=(b*c)*(a/100/12)
print("tiền lãi=",d)
print("tiền vốn+lãi",d+b)
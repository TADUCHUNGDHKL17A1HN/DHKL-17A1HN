#bài 4
import math
a=int(input("nhập số đo cạnh a:"));
b=int(input("nhập số đo cạnh b:"));
c=int(input("nhập số đo cạnh c:"));
chuvi=a+b+c
p=chuvi/2
dien_tich=math.sqrt((p*(p-a)*(p-b)*(p-c)))
print("diện tích=", dien_tich)
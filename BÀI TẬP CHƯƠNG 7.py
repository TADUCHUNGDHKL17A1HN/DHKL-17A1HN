#bài 7.1
x=int(input("nhập giá trị của x:"));
s=1+x+x**3/3+x**5/5
print("giá trị biểu thức s=1+x+x^3/3+x^5/5 là:",s)
#bài 7.2
result = 1+2
print('result=',result)
original_result = result
result = result - 1
print('result=',result)
original_result = result
result = result*2
original_result = result 
print('result=',result)
result = result**3
original_result = result
print('result=',result)
result = result+8
original_result = result
print('result=',result)
result = result % 7
original_result = result
print('result=',result)
result = result//2
original_result = result
print('result=',result)
#bài 7.3
result = 5
print('result=',result)
result -=1
print('result=',result)
result +=3
print('result=',result)
result = -result
print('result=',result)
result = True
print('not result=', not result)
#bài 7.4
x=10
y=4
print('x=%d,y=%d'%(x,y))
equivelence=x==y
print('x==y is',equivelence)
equivelence=x!=y
print('x!=y is',equivelence)
equivelence=x>y
print('x>y is',equivelence)
x=8
x=9
print('x=%d ,y=%d'%(x,y))
equivelence=x>=y
print('x>=y is',equivelence)
equivelence=x<y 
print('x<y is',equivelence)
equivelence=x<=y
print('x<=y is',equivelence)
#bài 7.5
x=15
y=12
print('Binary of x=', bin(x),',Binary of y=', bin(y))
print('x & y', bin(x&y))
print('x / y', bin(x|y))
print('x ^ y', bin(x^y))
print('~x=', bin(~x))
print('x << 2', bin(x<<2))
print('y >> 2', bin(y>>2))
#bài 7.6
x = True
y = False
print('x and y:',x and y)
print('x or y:',x or y)
print('not x:',not x)
print('x is y:',x is y)
print(' x is not y:', x is not y)
#bài 7.7 
x=int(input("nhập số tiền muốn đổi :"));
so_to1=x//500000
tien_con_lai=x%500000
print("số tờ 500k :",so_to1)
so_to2=tien_con_lai//200000
tien_con_lai=tien_con_lai%200000
print("số tờ 200k :",so_to2)
so_to3=tien_con_lai//100000
tien_con_lai=tien_con_lai%100000
print("số tờ 100k :",so_to3)
so_to4=tien_con_lai//50000
tien_con_lai=tien_con_lai%50000
print("số tờ 50k :",so_to4)
print("tiền còn lại ",tien_con_lai)



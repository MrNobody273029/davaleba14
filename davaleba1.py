
X1= int(input("X1 კოორდინანტი: "))
Y1= int(input("Y1 კოორდინანტი: "))
if X1>8 or X1<0:
	print("eror")
elif Y1>8 or Y1<0:
	print("eror")

X2= int(input("X2 კოორდინანტი: "))
Y2= int(input("Y2 კოორდინანტი: "))
if X2>8 or X2<0:
	print("eror")
elif Y2>8 or Y2<0:
	print("eror")

a=X1+Y1
a1=a%2

b=X2+Y2
b1=b%2

if a1 == b1:
	print("yes")
else: print("No")
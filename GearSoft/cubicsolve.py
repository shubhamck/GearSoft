def solve(a,b,c,d,acc):
	x = 20.0
	x_new = 21.0
	while abs(x - x_new)>=acc:
		x = x_new
		f_x = a*(x**3) + b*(x**2) + c*x + d
		df_x = 3*a*(x**2) + 2*b*x + c
		x_new = x - (f_x/float(df_x))
	return x_new

if __name__ == '__main__':
	print solve(1,1,1,-14,0.001)
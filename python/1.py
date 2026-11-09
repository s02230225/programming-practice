def factorization(n):
	p = {}
	d = 2
	while d * d <= n:
		while n % d == 0:
			p[d] = p.get(d,0) + 1
			n //= d
		d += 1
	if n > 1:
		if n not in p :
			p[n] = p.get(n,1)
	return p
n = int(input())
p = factorization(n)
x=1
for i,j in p.items():
	x=x*(i**(-((-j)//2)))
print(x)
import math
def mulmat2(ma, mb):
	return [
	ma[0]*mb[0] + ma[1]*mb[2],
	ma[0]*mb[1] + ma[1]*mb[3],
	ma[2]*mb[0] + ma[3]*mb[2],
	ma[2]*mb[1] + ma[3]*mb[3],
	]

coords = [0.707,-0.707,0,0,0.707,0.707,0,0,0,0,1,0,0,0,0,1]
N,P,Q,R,S,T,U,V,W = coords[0],coords[1],coords[2],coords[4],coords[5],coords[6],coords[8],coords[9],coords[10]

y = math.asin(U*-1)
E = math.cos(y)
H = math.cos(y)
z = math.acos(N/E)
x = math.asin(V/H)

# print(x,y,z)
# print(x/(math.pi/180),y/(math.pi/180),z/(math.pi/180))


		sinz = math.sin(z/2)
		cosz = math.cos(z/2)

		siny = math.sin(y/2)
		cosy = math.cos(y/2)

		sinx = math.sin(x/2)
		cosx = math.cos(x/2)

		mz = [0, 0, -sinz, cosz]
		my = [1, -siny, 0, cosy]
		mx = [-sinx, 0, 0, cosx]

		m1 = mulmat2(mz, my)
		m2 = mulmat2(mx, m1)
		print(m2)

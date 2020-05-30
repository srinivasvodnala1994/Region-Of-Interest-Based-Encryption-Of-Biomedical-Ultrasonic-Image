import random
import os,sys
import numpy
from PIL import Image
import timeit
start = timeit.default_timer()
im = Image.open("1.png")
#print (im.size, im.format)
row,col = im.size
pixels = im.load()

row1 = 1000003
phi = [0 for x1 in range(row1)]
occ = [0 for x1 in range(row1)]
primes = [] 
phi[1] = 1
#phi[2] = 1
#print (phi)
for i in range(2,1000001):
    if(phi[i] == 0):
        phi[i] = i-1
        primes.append(i)
        for j in range (2*i,1000001,i):
            if(occ[j] == 0):
                occ[j] = 1
                phi[j] = j
            phi[j] = (phi[j]*(i-1))//i


p = primes[random.randrange(1,167)]
q = primes[random.randrange(1,167)]


n = p*q
mod = n
phin1 = phi[n]
phin2 = phi[phin1]
e = primes[random.randrange(1,9000)]
mod1 = phin1
def power1(x,y,m):
    ans=1
    while(y>0):
        if(y%2==1):
            ans=(ans*x)%m
        y=y//2
        x=(x*x)%m
    return ans
d = power1(e,phin2-1,mod1)
enc = [[0 for x in range(row)] for y in range(col)]
dec = [[0 for x in range(row)] for y in range(col)]
#start = timeit.default_timer()
for i in range(col):
    for j in range(row):
        r,g,b = pixels[j,i]
        r1 = power1(r+10,e,mod)
        g1 = power1(g+10,e,mod)
        b1 = power1(b+10,e,mod)
        enc[i][j] = [r1,g1,b1]
#print (pixels[row-1,col-1])
img = numpy.array(enc,dtype = numpy.uint8)
img1 = Image.fromarray(img,"RGB")
img1.save('encr.png')
#stop = timeit.default_timer()
#execution_time = stop - start
#print("Program Executed in :",execution_time)
#star_t = timeit.default_timer()
for i in range(col):
    for j in range(row):
        r,g,b = enc[i][j]
        r1 = power1(r,d,mod)-10
        g1 = power1(g,d,mod)-10
        b1 = power1(b,d,mod)-10
        dec[i][j] = [r1,g1,b1]

img2 = numpy.array(dec,dtype = numpy.uint8)
img3 = Image.fromarray(img2,"RGB")
img3.save('decr.png')
#sto_p = timeit.default_timer()
#execution_time1 = sto_p - star_t

#print("Program Executed in1 :",execution_time1)
stop = timeit.default_timer()
execution_time = stop - start
print("Program Executed in :",execution_time)

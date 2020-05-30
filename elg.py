# Python program to illustrate ElGamal encryption 

import random 
from math import pow
import its
#import tup
from PIL import Image
import numpy as np
#from time import time
import timeit
start = timeit.default_timer()
#t1=time()

a = random.randint(2, 10) 

def gcd(a, b): 
	if a < b: 
		return gcd(b, a) 
	elif a % b == 0: 
		return b; 
	else: 
		return gcd(b, a % b) 

# Generating large random numbers 
def gen_key(q): 

	key = random.randint(pow(10, 20), q) 
	while gcd(q, key) != 1: 
		key = random.randint(pow(10, 20), q) 

	return key 

# Modular exponentiation 
def power(a, b, c): 
	x = 1
	y = a 

	while b > 0: 
		if b % 2 == 0: 
			x = (x * y) % c; 
		y = (y * y) % c 
		b = int(b / 2) 

	return x % c 

# Asymmetric encryption 
#start = timeit.default_timer()
def encrypt(msg, q, h, g): 

	en_msg = [] 

	k = gen_key(q)# Private key for sender 
	s = power(h, k, q) 
	p = power(g, k, q) 
	
	for i in range(0, len(msg)): 
		en_msg.append(msg[i]) 

	print("g^k used : ", p) 
	print("g^ak used : ", s) 
	for i in range(0, len(en_msg)): 
		en_msg[i] = s * ord(en_msg[i]) 

	return en_msg, p 
#stop = timeit.default_timer()
#execution_time = stop - start
#print("Program Executed in :",execution_time)
#star_t = timeit.default_timer()
def decrypt(en_msg, p, key, q): 

	dr_msg = [] 
	h = power(p, key, q) 
	for i in range(0, len(en_msg)): 
		dr_msg.append(chr(int(en_msg[i]/h))) 
		
	return dr_msg 
#sto_p = timeit.default_timer()
#execution_time1 = sto_p - star_t
#print("Program Executed in1 :",execution_time1)
# Driver code 
def main(): 
	#tart = timeit.default_timer()

	msg = its.its("brain.jpg")
   
	#print("Original Message :", msg, type(msg) )

	q = random.randint(pow(10, 20), pow(10, 50)) 
	g = random.randint(2, q) 

	key = gen_key(q)# Private key for receiver 
	h = power(g, key, q) 
	print("g used : ", g) 
	print("g^a used : ", h) 

	en_msg, p = encrypt(msg, q, h, g)
	#print ("x",en_msg,type(en_msg))
	l_r = ' '.join([str(elem) for elem in en_msg]) 
	#print("lsr",l_r, type(l_r))
	#a = (en_msg, p)
	#b =  ''.join(a)
	#b = ' '.join(map(str, a)) 
	#s_r = tup.cts(a)
	#enmsg = its.sti(''.join((b)), 'enc_baby.jpg' )
	#print("encrypted message :",b, type(b));
	#array = np.array(a, dtype=np.uint8)
	#new_image = Image.fromarray(array)
	#new_image.save('new.jpg')
	emsg = its.sti(''.join(l_r), 'ec_baby.png' )
	print("encrypted Message :", emsg)
	#stop = timeit.default_timer()
	#execution_time = stop - start
	#print("Program Executed in :",execution_time)


	#star_t = timeit.default_timer()
	#list_Str = (' '.join([str(elem) for elem in (en_msg, p)]) 
 
	dr_msg = decrypt(en_msg, p, key, q) 
	dmsg = its.sti(''.join(dr_msg), 'dec_baby.png' )
	print("Decrypted Message :", dmsg); 
	#sto_p = timeit.default_timer()
	#execution_time1 = sto_p - star_t
	#print("Program Executed in1 :",execution_time1)



if __name__ == '__main__': 
	main() 
#t2=time()
#print(t2-t1)


stop = timeit.default_timer()
execution_time = stop - start

print("Program Executed in :",execution_time)

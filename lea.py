#LEA encryption
import LEA
import its

import timeit
#start= timeit.default_timer()

def main():

	key = bytearray(b"blacksnakeblacksnake1234")
	#print(key)

	
	start= timeit.default_timer()

	input_str = its.its("1.png")
	#print("input string : " + input_str)

	
	#print("Start Encryption")
	
	pt = bytearray(input_str, "utf8")
	#print(pt,type(pt))

	leaECB = LEA.ECB(True, key, True)

	ct = leaECB.update(pt)
	ct += leaECB.final()
	#l_r = ' '.join([str(elem) for elem in ct]) 
	#emsg = its.sti(''.join(ct), 'ec_gbaby.jpg' )
	#print(str(ct),type(str(ct)))
	emsg = its.sti(''.join(str(ct)), 'ec_gbaby.png' )

	#print(ct,type(ct))

	#print("End Encryption")
	stop = timeit.default_timer()
	execution_time = stop - start

	print("Program Executed in :",execution_time)



	



	
	#print("Start Decryption")
	start= timeit.default_timer()

	
	leaECB = LEA.ECB(False, key, True)
	pt = leaECB.update(ct)
	pt += leaECB.final()

	#print(pt,type(pt))
	decrypt_output = pt.decode('utf8')
	dmsg = its.sti(''.join(decrypt_output), 'd_gbaby.png' )	
	#print( decrypt_output,type( decrypt_output))

	#print("End Decrypt")
	stop = timeit.default_timer()
	execution_time = stop - start

	print("Program Executed in :",execution_time)



	




if __name__ == "__main__":
    main()
   
#stop = timeit.default_timer()
#execution_time = stop - start

#print("Program Executed in :",execution_time)



import base64
def its(filename):
	with open(filename, "rb") as img_file:
    		my_string = base64.b64encode(img_file.read())
#print(my_string.decode('utf-8'))
	return(my_string.decode('utf-8'))

def sti(string, filename):
	d= base64.decodestring(str.encode(string))
	image_result = open(filename, 'wb')
	image_result.write(d)
	image_result.close()
	return image_result 
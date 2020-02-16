import base64
import sys

def link_base64(source):
	source=source.replace("-","+")
	source=source.replace("_","/")
	return str(base64.b64decode(source.encode('utf-8')),'utf-8')

def ssr_link_decode(source):
	dict_out={}

	source=source[source.index("ssr://")+6:]
	decode=link_base64(source)
	
	up=decode[:decode.index("/?")]
	up_list=up.split(':')

	str_list=["server","server_port","protocol","method","obfs","password"]
	for t in range(6):
		if(t!=5):
			dict_out[str_list[t]]=up_list[t]
		else:
			dict_out[str_list[t]]=link_base64(up_list[t])

	down=decode[decode.index("/?")+2:]
	if(down==""):
		return
	down_list=down.split("&")

	for temp in down_list:
		dict_out[temp[:temp.index("=")]]=link_base64(temp[temp.index("=")+1:])
	
	return dict_out

def ss_link_decode(source):
	dict_out={}
	
	source=source[source.index("ss://")+5:]
	decode=link_base64(source)
	decode=decode.replace("@",":")
	decode_list=decode.split(":")
	
	str_list=["method","password","server","port"]
	for t in range(4):
		dict_out[str_list[t]]=decode_list[t]
	
	return dict_out
	
def main():
	if(len(sys.argv)!=2):
		print("Param Error!")
		return
	source=sys.argv[1]
	if("ssr://" in source):
		dict_out=ssr_link_decode(source)
	elif("ss://" in source):
		dict_out=ss_link_decode(source)
	else:
		print("Is not SS or SSR link!")
		return
	for key,value in dict_out.items():
		print(key+"="+value)

if(__name__=="__main__"):
	try:
		main()
	except Exception as e:
		print("Something Error..")

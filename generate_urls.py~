from sys import argv
import re
rawfile=open('dump.txt','r')
wfile=open('links.txt','w')
fstring= rawfile.readline()
start=0
end=0
while start!=-1:
	start=fstring.find('src="https:',start)
	end=fstring.find('"',start+5)
	if(start!=-1):
		start=start+1
		wfile.write(fstring[(start+4):(end)]+'\n')		
rawfile.close()
wfile.close()









import zlib
file1= open('1.txt','r')
text= file1.read()
file1.close()

code= zlib.compress(text.encode('utf-8'))
code= code.decode('utf-8')

f=open('compres.txt','w')
f.write(code)
f.close()
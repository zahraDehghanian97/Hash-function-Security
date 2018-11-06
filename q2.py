import pyDes
data = b"0123456789ABCDEF"
k = pyDes.des(bytes.fromhex("133457799BBCDFF1"))
d = k.encrypt(data)
print("<--- question 2 --->")
print("##plain text : "+str(data))
print("##cipher text with DES : %r" % d)
print("##Decrypted text : %r" % k.decrypt(d))

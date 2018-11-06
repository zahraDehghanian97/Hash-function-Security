import hashlib

sha = hashlib.sha256()
md = hashlib.md5()

sha.update(b"If you want to keep a secret, you must also hide it from yourself")
md.update(b"If you want to keep a secret, you must also hide it from yourself")
print("<--- question 1 --->")
print("##plain text : If you want to keep a secret, you must also hide it from yourself")
print("##cipher text with sha256 : " + sha.hexdigest())
print("##cipher text with md5 : " + md.hexdigest())
print("<--- delete last character --->")
sha.update(b"If you want to keep a secret, you must also hide it from yoursel")
md.update(b"If you want to keep a secret, you must also hide it from yoursel")
print("##plain text : If you want to keep a secret, you must also hide it from yoursel")
print("##cipher text with sha256 : " + sha.hexdigest())
print("##cipher text with md5 : " + md.hexdigest())

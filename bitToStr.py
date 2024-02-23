import base64

mystr = 'O João mordeu o cão!'

# Encode
mystr_encoded = base64.b64encode(mystr.encode('utf-8'))
# b'TyBKb8OjbyBtb3JkZXUgbyBjw6NvIQ=='
print(mystr_encoded)

# Decode
mystr_encoded = base64.b64decode(mystr_encoded).decode('utf-8')
# 'O João mordeu o cão!'
print(mystr_encoded)

print()
print()

# Decode
mystr_encoded = base64.b64decode("J2z6fdvb/kiOwpprRuONsg==").decode('utf-8')
# 'O João mordeu o cão!'
print(mystr_encoded)
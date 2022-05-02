import hashlib

f = open("C:\\Users\\82109\\Desktop\\password_dictionary.txt", "rb")

salt = b'c13a0c9d457bc4f0cf03a4e5d0aba532'
hashs = b'8fbe43746de9600a656a411ebfb2005afe2eed54706f9040dc7ef72b1b76751a'


for line in f:
   
#   de_line = line.decode()
#   de_line = de_line.rstrip('\r\n')
#   en_line = de_line.encode()

   h = hashlib.sha256()  
   h.update(salt)
   h.update(line[0:-2])
   res = h.hexdigest()

   prt = line[0:-2].decode()

#  res_enc = res.encode()

   if hashs == res.encode() :
      print('===========================비밀번호는', prt,'입니다===========================')
      break
   else :
      continue

f.close()
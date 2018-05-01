import RSA_util
import pickle

pub_fp = open("public_key", "r")
priv_fp = open("private_key","r")
decode_fp = open("decrypted_message", "w+")

d = int (priv_fp.read())
modN = int(pub_fp.readline())

with open ('ciphertext', 'rb') as encode_fp:
    blocks = pickle.load(encode_fp)

msg = RSA_util.decrypt(blocks, modN, d, 15)


decode_fp.write(msg)
print (msg)

pub_fp.close()
priv_fp.close()
encode_fp.close()

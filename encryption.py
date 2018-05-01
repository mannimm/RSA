import RSA_util
import pickle


msg_fp = open("original_message", "r")
pub_fp = open("public_key", "r")

o_message = msg_fp.read()
modN 	= int(pub_fp.readline())
e 		= int(pub_fp.readline())


blocks 	= RSA_util.encrypt(o_message, modN, e, 15)


with open('ciphertext', 'wb') as encode_fp:
    pickle.dump(blocks, encode_fp)

msg_fp.close()
pub_fp.close()
encode_fp.close()

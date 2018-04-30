import generatePrime
import RSA_util



#str.message_file = input ("Enter message file name: ")

cipher_fd = open("ciphertext", "r")
priv_fd = open("private_key", "r")
pub_fd = open("public_key", "r")
decrypt_fd = open ("decrypted_message", "w")


modN = pub_fd.readline()
cipherText = cipher_fd.read()
d = priv_fd.read()

print cipherText
print modN




decrypted_msg = RSA_util.numList2string( RSA_util.decrypt(cipherText, modN, d, 15) )

print decrypted_msg

cipher_fd.close()
pub_fd.close()
decrypt_fd.close()
priv_fd.close()

#encode_fd.write(encrypted_msg)
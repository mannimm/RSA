import generatePrime
import RSA_util



#str.message_file = input ("Enter message file name: ")

msg_fd = open("msg", "r")
pub_fd = open("public_key", "r")
encode_fd = open("encrypt", "w")


message = msg_fd.read()

modN = pub_fd.readline()
e = pub_fd.readline()

print message
print e
print modN



# encrypted_msg = RSA_util.numList2string( RSA_util.blocks2numList(RSA_util.encrypt(message, modN, e, 15), 15) )

# numList = RSA_util.encrypt(message, modN, e, 15)

numList = RSA_util.string2numList(message)
blocks = RSA_util.numList2blocks(numList, 15)     #get the message in blocks

for m in blocks:
	print m



msg_fd.close()
pub_fd.close()
encode_fd.close()

#encode_fd.write(encrypted_msg)
import RSA_util
import generatePrime
import random


pub_k = open("public_key", "w")
priv_k = open("private_key", "w")

# pub_k.truncate()
# priv_k.truncate()

num = input("enter number of digit for prime number : ")


p = generatePrime.generateLargePrime(num)
q = generatePrime.generateLargePrime(num)


key = p*q
phi = (p - 1) * (q - 1)
e = phi
while (RSA_util.euclid(e, phi) != 1):
    e = random.randint(2, key - 1) #pick a random public key
d = RSA_util.modInv(e, phi)    #compute the secret key
  
priv_k.write (str(d))

pub_k.write (str(key)+"\n")
pub_k.write (str(e))


pub_k.close()
priv_k.close()





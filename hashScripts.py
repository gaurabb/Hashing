#!usr/bin/python
#Generate a random Salt value
#Get hash values in hexadecimal for supplied input
#Returns the hash and the salt
import hashlib
import uuid

def main():
	varToHash = raw_input("Enter the string to be hashed: ")
	varHashAlgo = raw_input("Enter: 1 for MD5 \n 2 for SHA1 \n 3 for SHA256 \n 4 for SHA384 \n 5 for SHA512 \n")
	saltValue = getSalt()
	print ("SALT: " + saltValue)
	if 1 == int(varHashAlgo):
		getMD5(varToHash + saltValue)
	elif 2 == int(varHashAlgo):
		getSHA1(varToHash + saltValue)
	elif 3 == int(varHashAlgo):
		getSHA256(varToHash + saltValue)
	elif 4 == int(varHashAlgo):
		getSHA384(varToHash + str(getSalt()))
	elif 5 == int(varHashAlgo):
		getSHA512(varToHash + saltValue)

		
def getMD5(toHash):
	varMD5 = hashlib.md5(toHash).hexdigest()
	print ("MD5 Hash: " + str(varMD5))
	return varMD5

def getSHA1(toHash):
	varSHA1 = hashlib.sha1(toHash).hexdigest()
	print ("SHA1 Hash: " + str(varSHA1))
	return varSHA1
	
def getSHA256(toHash):
	varSHA256 = hashlib.sha256(toHash).hexdigest()
	print ("SHA256 Hash: " + str(varSHA256))
	return varSHA256
	
def getSHA384(toHash):
	varSHA384 = hashlib.sha384(toHash).hexdigest()
	print ("SHA384 Hash: " + str(varSHA384))
	return varSHA384
	
def getSHA512(toHash):
	varSHA512 = hashlib.sha512(toHash).hexdigest()
	print ("SHA512 Hash: " + str(varSHA512))
	return varSHA512
	
def getSalt():
	return str(uuid.uuid4())
	
if __name__ == '__main__':
	main()
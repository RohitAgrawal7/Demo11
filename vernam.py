import string

def encryption_code(text):
	result=[]
	for char in text:
		result.append(alphas.index(char))
	return result

def add(key,text):
	result=[]

	l_text=len(text)
	l_key=len(key)
	l_diff=l_text-l_key

	if l_diff > 0:
		div=l_text/l_key
		rem=l_text%l_key
		for x in zip(key*div+key[:rem],text):
			result.append(x[0]+x[1])
	elif l_diff < 0:
		for x in zip(key,text[:l_text]):
			result.append(x[0]+x[1])
	else:
		for x in zip(key,text):
			result.append(x[0]+x[1])
	return result

alphas=list(string.ascii_lowercase)

encryption_text=input("enter encryption text:\n")
key_code=encryption_code(encryption_text)

input_text=input("enter text to be encrypted:\n")
input_code=encryption_code(input_text)
final=""

for x in add(key_code,input_code):
	if x > 25:
		final=final+alphas[x-25]	
	else:
		final=final+alphas[x]

print("----------------------------------------------")
print("encrypted text is-\n")
print(final)
print("----------------------------------------------")


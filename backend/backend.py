import string

def cesar_cipher(text: str, key: int):
	if type(text) == str and type(key) == int:
		return "".join([chr((ord(char) + key) % 1_114_112) for char in text])
	else:
		raise(TypeError)

def cesar_uncipher(crypted_text: str, key: int):
		return cesar_cipher(crypted_text, -key)

def hack_cesar_cipher(crypted_text: str, alphabet):
	if type(crypted_text) == str and type(alphabet) == str:
		for possible_key in range(0, 1_114_112):
			possible_uncryption = cesar_uncipher(crypted_text, possible_key)
			if possible_uncryption[0] in alphabet:
				print(possible_key)
				print(possible_uncryption)
				print("_"*20)
	else:
		raise(TypeError)

def vigenere_cipher(text: str, password: str):
	list_of_keys = [ord(char) for char in password]
	crypted_text = []
	for index, char in enumerate(text):
		current_key = list_of_keys[index%len(list_of_keys)]
		crypted_text.append(cesar_cipher(char, current_key))
	return "".join(crypted_text)

def vigenere_uncipher(text, password):
	password = "".join([chr(1114111-ord(elt)) for elt in password])
	return vigenere_cipher(text, password)

if __name__ == "__main__":
	message = "Hello World!"

	crypted_text = cesar_cipher(message, 12, cipher=True) # exo 1
	print(crypted_text)

	initial_message = cesar_cipher(crypted_text, 12, cipher=False) # exo 2
	print(initial_message == message)

	hack_cesar_cipher(crypted_text, alphabet=string.printable) # exo3

	crypted_message = vigenere_cipher(text=message, password="Azerty12345!", cipher=True)
	print(crypted_message)
	initial_message = vigenere_cipher(text=crypted_message, password="Azerty12345!", cipher=False)
	print(initial_message)
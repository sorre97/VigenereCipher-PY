""" Cypher matrix handler """

from string import ascii_lowercase as l

class CypherTable:
	
	""" Vigenere matrix initialization """
	def __init__(self):
		""" takes lsit of alphabet from the next letter and adds to the end the beginning cutted piece """
		self.matrix = [l[i:]+l[:i] for i in range(len(l))]

	def cross(self, b, a):
   		val1 = self.matrix[0].index(a)	# index of keyChar
		new_letter = [i for i in self.matrix if i[0] == b][0][val1]	# takes all rows that have as first char the wordToEncrypt char,
		# takes the first one and access to the char at keyCharPos
   		return new_letter

	def decross(self, b, a):
   		val1 = self.matrix[0].index(a)	# index of keyChar
   		val2 = self.matrix[0].index(b)	# index of encryptedChar
   		new_letter = [i for i in self.matrix if i[val1] == b][0][0]	# takes all rows that have as keyCharPos char the encryptedChar,
		# takes the first one and access to the first char of the row
   		return new_letter

	def __str__(self):
		return "\n".join('|'.join(row) for row in self.matrix)	# join each char with | and \n at end of the row
	
	def encrypt(self, string, key):
		encryptedString = ""
		keyRange = len(string) - len(key)
		for i in range(keyRange):	# stretching key to have length equal to the stringToEncrypt length
			key += key[i]
		
		for i in range(len(string)):
			encryptedString += self.cross(string[i], key[i])
		return encryptedString

	def decrypt(self, string, key):
		decryptedString = ""
		keyRange = len(string) - len(key)
		for i in range(keyRange):	# stretching key to have length equal to the stringToDecrypt length
			key += key[i]	
		for i in range(len(string)):
			decryptedString += self.decross(string[i], key[i])
		return decryptedString


"""
DOCUMENTATION

- Vigenere matrix

a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z
b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|a
c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|a|b
d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|a|b|c
e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|a|b|c|d
f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|a|b|c|d|e
g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|a|b|c|d|e|f
h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|a|b|c|d|e|f|g
i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|a|b|c|d|e|f|g|h
j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|a|b|c|d|e|f|g|h|i
k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|a|b|c|d|e|f|g|h|i|j
l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|a|b|c|d|e|f|g|h|i|j|k
m|n|o|p|q|r|s|t|u|v|w|x|y|z|a|b|c|d|e|f|g|h|i|j|k|l
n|o|p|q|r|s|t|u|v|w|x|y|z|a|b|c|d|e|f|g|h|i|j|k|l|m
o|p|q|r|s|t|u|v|w|x|y|z|a|b|c|d|e|f|g|h|i|j|k|l|m|n
p|q|r|s|t|u|v|w|x|y|z|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o
q|r|s|t|u|v|w|x|y|z|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p
r|s|t|u|v|w|x|y|z|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q
s|t|u|v|w|x|y|z|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r
t|u|v|w|x|y|z|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s
u|v|w|x|y|z|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t
v|w|x|y|z|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u
w|x|y|z|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v
x|y|z|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w
y|z|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x
z|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y

Encryption:
	cross between key char and stringToDecrypt char

Decryption:
	taken the column with the key char, the decrypted letter is the first
	char of the row that contains in pos(keyChar) the encryptedStringChar
"""


"""
DEBUG
table = CypherTable()
print(table)
print table.decross("r", "c")
print table.encrypt("programmazione", "cane")
print table.decrypt("rrbktazqczvspe", "cane")
"""

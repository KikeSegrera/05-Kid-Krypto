#Kid Krypto
import fileinput

def keygen(a,b,A,B):
	'''
	Realiza el cálculo de las llaves pública (n,e) y privada d
	a,b,A,B: parámetros para el algoritmo
	'''
	M = a * b - 1
	e = A * M + a
	d = B * M + b
	n = (e * d - 1) // M

	return [n,e,d]


def kidkrypto(option,a,b,A,B,text):
	'''
	Realiza el cifrado o descifrado del algoritmo Kid Krypto
	con los valores especificados del texto deseado
	option : cifrado o descifrado
	a,b,A,B: parámetros para el algoritmo
	text : texto a cifrar o descifrar
	'''

	[n,e,d] = keygen(int(a),int(b),int(A),int(B))

	if option == 'E':
		result = (int(text) * e) % n
	elif option == 'D':
		result = (int(text) * d) % n

	return result

lines = []

for line in fileinput.input():
	line = line.replace('\n','')
	lines.append(line)

print(kidkrypto(lines[0],lines[1],lines[2],lines[3],lines[4],lines[5]))
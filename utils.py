import subprocess as sp

def cls(header = True):
	tmp = sp.call('cls', shell=True)
	if header:
		print('''
===================
Chaos in Simpleland
===================

			''')

def readInt(txt = '', errtxt = ''):
	while True:
		try:
			val = int(input(txt))
		except:
			print(errtxt)
			continue
		else:
			break
	return  val

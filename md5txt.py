import hashlib


def aurkituKodetuta():
	arIzena="proba.txt"
	#uneko argazkia zabaltzen eta irakurtzen da.
	with open(arIzena, 'rb') as f:
		kodeona="797354a58eedfdea5b77b8c12d976256"
		bytes=f.read() #artxiboa byte-ak bezala irakurri
		#informazioa bueltatzen da string bezala
		hasheatu=hashlib.md5(bytes).hexdigest()
		#aurkitzen badu, esan aurkitu duela:
		if hasheatu==kodeona:
			print("AURKITUTA!")
			print(arIzena + ":")
			print(hasheatu)
		else:
		
			print("Ez da berdina!")







aurkituKodetuta()

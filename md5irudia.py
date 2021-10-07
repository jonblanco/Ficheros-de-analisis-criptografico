import hashlib


def aurkituKodetuta():
    #string-ak eratu ditut gero argazkiak berak bakarrik joateko aldatzen.
    imagen="imagen"
    jpg=".jpg"
    i=1

    #while bat argazki guztiak atzitzeko
    while i<47:
        #27. argazkia ez denez existitzen, salbuespen moduan if bat jarri dut:
        if i == 27:
            i = i + 1
        j=str(i)
        arIzena= imagen+j+jpg
        #uneko argazkia zabaltzen eta irakurtzen da.
        with open(arIzena, 'rb') as f:
            kodeona="e5ed313192776744b9b93b1320b5e268"
            bytes=f.read() #artxiboa byte-ak bezala irakurri

            #informazioa bueltatzen da string bezala
            hasheatu=hashlib.md5(bytes).hexdigest()

            #aurkitzen badu, esan aurkitu duela:
            if hasheatu==kodeona:
                print("AURKITUTA!")
                print(arIzena + ":")
                print(hasheatu)
            i=i+1







aurkituKodetuta()
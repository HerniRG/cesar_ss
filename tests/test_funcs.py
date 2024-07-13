from app.modelos import Cifrador

def test_cesar():
    cifrador = Cifrador(1)
    assert cifrador.cesar("HOLA") == "IPMB"
    cifrador.d = 2
    assert cifrador.cesar("ZARA") == "ACTC"
    cifrador.d = 1
    assert cifrador.cesar("HOLA") == "IPMB"
    cifrador.d = 2
    assert cifrador.cesar("ZARA") == "ACTC"
    cifrador.d = 10
    assert cifrador.cesar("") == ""
    cifrador.d = -1
    assert cifrador.cesar("HOLA") == "GÑK "
    cifrador.d = 1
    assert cifrador.cesar("ZIGZAG") == " JH BH"
    cifrador.d = -1
    assert cifrador.cesar(" JH BH") == "ZIGZAG"

def test_crea_cifrador():
    cifrador = Cifrador(3)
    cesar3 = cifrador.crea_cifrador()
    assert cesar3("ZIGZAG") == "BLJBDJ"

def test_crea_par_cesar():
    cifrador = Cifrador(3)
    cifrador_cesar_3, descifrador_cesar_3 = cifrador.crea_par_cesar()
    assert cifrador_cesar_3("ZIGZAG") == "BLJBDJ"
    assert descifrador_cesar_3("BLJBDJ") == "ZIGZAG"

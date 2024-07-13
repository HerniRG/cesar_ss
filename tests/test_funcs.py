from app.vistas import crea_cifrador, cesar, crea_par_cesar

def test_cesar():

    assert cesar("HOLA", 1) == "IPMB" 
    assert cesar("ZARA", 2) == "ACTC"
    assert cesar("HOLA", 1) == "IPMB"
    assert cesar("ZARA", 2) == "ACTC"
    assert cesar("", 10) == ""
    assert cesar("HOLA", -1) == "GÑK "
    assert cesar("ZIGZAG", 1) == " JH BH"
    assert cesar(" JH BH", -1) == "ZIGZAG"


def test_crea_cifrador():
    
    cesar3 = crea_cifrador(3)
    assert cesar3("ZIGZAG") == "BLJBDJ"


def test_crea_par_cesar():

    cifrador_cesar_3, descifrador_cesar_3 = crea_par_cesar(3)

    assert cifrador_cesar_3("ZIGZAG") == "BLJBDJ"
    assert descifrador_cesar_3("BLJBDJ") == "ZIGZAG"

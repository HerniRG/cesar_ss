from simple_screen import locate, init, finish
from app.modelos import Cifrador
from app.vistas import VistaCesar

class CesarController:
    def __init__(self):
        self.vista = VistaCesar()
        self.cifrador = Cifrador(0)
    
    def run(self):
        while True:
            locate(self.vista.ancho_terminal, 1)
            self.vista.print_cabecera()
            try:
                cifrado, mensaje = self.vista.obtener_cifrado_y_mensaje()
            except ValueError as e:
                self.vista.mostrar_error(str(e)) # Corrige el error convirtiendo a string
                continue

            self.cifrador.d = cifrado
            mensaje_cifrado = self.cifrador.cifrar(mensaje)
            self.vista.mostrar_mensaje_cifrado(mensaje_cifrado)

            if self.vista.salir_programa():
                break

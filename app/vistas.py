from simple_screen import cls, Print, pen, locate, Input, DIMENSIONS
from simple_screen.entities import Color
from app.modelos import *


class VistaCesar():
    def __init__(self) -> None:
        self.ancho_terminal = self.calculo_width()

    def calculo_width(self):
        width = DIMENSIONS.w
        column_center = (width - len("*          CIFRADO CESAR          *")) // 2 
        return column_center

    def obtener_cifrado_y_mensaje(self):
        try:
            locate(self.ancho_terminal, 7)
            cifrado = int(Input("Distancia de cifrado: "))   
            locate(self.ancho_terminal, 8)
            mensaje = Input("Mensaje a cifrar: ")
        except ValueError:
            raise ValueError("Error: El dato introducido no es válido.")
            
        return cifrado, mensaje

    def mostrar_mensaje_cifrado(self, mensaje_cifrado):
        locate(self.ancho_terminal, 10)
        Print(f"Mensaje cifrado: {mensaje_cifrado}")

    def mostrar_error(self, error):
        pen(Color(255, 0, 0))
        locate(self.ancho_terminal, 16)
        Print(error)
        locate(self.ancho_terminal, 17)
        Input("Pulsa cualquier tecla para continuar...") #lo he hecho así porque sino vuelve al bucle y me borra el print del error

    def salir_programa(self):
        locate(self.ancho_terminal, 14)
        salida = Input("¿Otro mensaje (S/N)?: ")
        return salida.lower() != 's'

    def print_cabecera(self):
        cls()
        pen(Color(0, 255, 0))  # Establece el color verde lima para la cabecera
        Print(f"{' ' * self.ancho_terminal}***********************************")
        Print(f"{' ' * self.ancho_terminal}*                                 *")
        Print(f"{' ' * self.ancho_terminal}*          CIFRADO CESAR          *")
        Print(f"{' ' * self.ancho_terminal}*                                 *")
        Print(f"{' ' * self.ancho_terminal}***********************************") 
    


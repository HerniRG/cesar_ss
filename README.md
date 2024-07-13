# Reto de Programación: Mini Aplicación de Consola con Cifrado César

## Objetivo

Crear una mini aplicación de consola utilizando `simple_screen` que implemente un cifrador César. El programa pedirá la distancia de cifrado y el mensaje a cifrar, mostrando el mensaje cifrado. Al finalizar, preguntará si se desea cifrar otro mensaje, permitiendo repetir el proceso o terminar el programa.

## Instrucciones

### 1. Inicialización de la Interfaz:

- Debes centrar el texto **CIFRADO CESAR** en la pantalla.
- La columna de inicio de los literales se calculará centrando el texto **CIFRADO CESAR** en la pantalla. Si el ancho de la pantalla es `w`, la columna será `(w - len("CIFRADO CESAR")) // 2`.

### 2. Entrada de Datos:

- Solicita la distancia de cifrado.
- Solicita el mensaje a cifrar.

### 3. Salida del Mensaje Cifrado:

- Muestra el mensaje cifrado.

### 4. Pregunta de Repetición:

- Al finalizar, muestra **¿otro mensaje (S/n)?**.
- Si el usuario responde `S` o `s`, reinicia el proceso; en cualquier otro caso, termina el programa.

## Estructura de la Interfaz:

    CIFRADO CESAR
    =============
    Distancia de cifrado:
    Entrada:
    Salida:
    ¿otro mensaje (S/n)?


## Requisitos

1. **Usar simple_screen**:
   - Usa `simple_screen.locate`, `simple_screen.Print`, `simple_screen.Input`, `simple_screen.init()`, y `simple_screen.finish()` para construir la interfaz.

2. **Crear una clase CifradoCesar**:
   - **Atributo**: `distancia`
   - **Métodos**: `cifrar` y `descifrar`

3. **Utilizar pytest para crear tests de funcionamiento de CifradoCesar**:
   - No se requieren tests para la interfaz, solo para la clase `CifradoCesar`.

---

"""
Código desarrollado por:

- Genis Cruz Lourdes Victoria (Número de cuenta: 420053978)
- Montes Cantero Zelene Yosseline Isayana (Número de cuenta: 317159923)

Materia: Sistemas Distribuidos
Facultad: Ingeniería
Institución: Universidad Nacional Autónoma de México (UNAM)

Fecha: 28 de febrero de 2024
"""

# Importar la biblioteca 'socket' para la comunicación de red
import socket

# Definir una función llamada 'iniciar_cliente'
def iniciar_cliente():
    # Crear un objeto de socket para el cliente
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar el cliente al servidor en la dirección IP '127.0.0.1' y puerto '8080'
    cliente.connect(('127.0.0.1', 8080))

    # Bucle para mantener la comunicación continua con el servidor
    while True:
        # Solicitar al usuario que ingrese un mensaje
        mensaje = input("Mensaje: ")

        # Enviar el mensaje codificado como UTF-8 al servidor
        cliente.send(mensaje.encode('utf-8'))

        # Recibir la respuesta del servidor (hasta 1024 bytes) y decodificarla desde UTF-8
        respuesta = cliente.recv(1024)
        
        # Imprimir la respuesta del servidor
        print(f"Servidor responde: {respuesta.decode('utf-8')}")

# Verificar si el script se está ejecutando como el programa principal
if __name__ == "__main__":
    # Llamar a la función 'iniciar_cliente' cuando se ejecuta el script
    iniciar_cliente()




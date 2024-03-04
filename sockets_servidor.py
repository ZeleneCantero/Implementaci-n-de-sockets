"""
Código desarrollado por:

- Genis Cruz Lourdes Victoria (Número de cuenta: 420053978)
- Montes Cantero Zelene Yosseline Isayana (Número de cuenta: 317159923)

Materia: Sistemas Distribuidos
Facultad: Ingeniería
Institución: Universidad Nacional Autónoma de México (UNAM)

Fecha: 28 de febrero de 2024
"""

# Importar las bibliotecas necesarias
import socket
import threading

# Definir una función para manejar la comunicación con un cliente
def manejar_cliente(socket_cliente):
    while True:
        # Recibir datos del cliente (hasta 1024 bytes)
        data = socket_cliente.recv(1024)
        # Verificar si no hay datos (el cliente ha cerrado la conexión)
        if not data:
            break
        # Mostrar el mensaje recibido del cliente
        print(f"Cliente dice: {data.decode('utf-8')}")
        # Solicitar al usuario del servidor una respuesta
        respuesta = input("Respuesta: ")
        # Enviar la respuesta al cliente
        socket_cliente.send(respuesta.encode('utf-8'))
    
    # Cerrar el socket cuando la comunicación con el cliente finaliza
    socket_cliente.close()

# Definir una función para iniciar el servidor
def iniciar_servidor():
    # Crear un socket para el servidor (IPv4, TCP)
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enlazar el socket a la dirección '0.0.0.0' en el puerto 8080
    servidor.bind(('0.0.0.0', 8080))
    # Escuchar por conexiones entrantes, permitiendo hasta 5 en espera
    servidor.listen(5)
    # Mostrar un mensaje indicando que el servidor está escuchando
    print("[*] Servidor escuchando en 0.0.0.0:8080")

    while True:
        # Aceptar una conexión entrante y obtener el socket del cliente y la dirección del cliente
        socket_cliente, addr = servidor.accept()
        # Mostrar información sobre la conexión aceptada
        print(f"[*] Conexión aceptada de {addr[0]}:{addr[1]}")
        # Iniciar un hilo para manejar la comunicación con el cliente
        hilo_cliente = threading.Thread(target=manejar_cliente, args=(socket_cliente,))
        hilo_cliente.start()

# Entrar al bloque principal del programa cuando se ejecuta el script
if __name__ == "__main__":
    # Llamar a la función para iniciar el servidor
    iniciar_servidor()



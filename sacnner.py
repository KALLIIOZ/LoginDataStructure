import bluetooth

# Dirección MAC de la caminadora (debes reemplazarla con la dirección de tu caminadora)
caminadora_mac = "00:00:00:00:00:00"

def descubrir_dispositivos_cercanos():
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, device_id=-1, duration_ = None, device_name=None)
    
    if not nearby_devices:
        print("No se encontraron dispositivos Bluetooth cercanos.")
        return
    
    print("Dispositivos Bluetooth cercanos:")
    for addr, name in nearby_devices:
        print(f"Nombre: {name}, Dirección MAC: {addr}")

def conectar_caminadora():
    try:
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((caminadora_mac, 1))  # El segundo argumento es el puerto RFCOMM (generalmente 1)
        print("Conexión establecida con la caminadora")
        return sock
    except Exception as e:
        print("Error al conectar con la caminadora:", e)
        return None

def main():
    caminadora_socket = conectar_caminadora()
    
    if caminadora_socket:
        # Aquí puedes enviar y recibir datos con la caminadora
        # Por ejemplo, enviar comandos para controlar la caminadora
        caminadora_socket.send("Comando de control")
        
        # Leer datos de la caminadora
        data = caminadora_socket.recv(1024)
        print("Datos recibidos de la caminadora:", data)

        caminadora_socket.close()

if __name__ == "__main__":
    main()

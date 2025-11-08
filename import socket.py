import socket

def server_program():
    # use the standard loopback interface address (localhost)
    HOST = "127.0.0.1"
    # Start with default port, try others if busy
    ports = [65432, 65433, 8080, 8888, 9999]
    socket_created = False

    for PORT in ports:
        try:
            # Create a socket object
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # Set SO_REUSEADDR to allow reuse of the address
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind((HOST, PORT))
                s.listen()
                print(f"✅ Server listening on {HOST}:{PORT}...")
                socket_created = True
                break
        except OSError as e:
            print(f"❌ Port {PORT} is busy, trying next port...")
            continue

    if not socket_created:
        print("❌ All ports are busy. Please try again later.")
        return

    # Accept a new connection
    conn, addr = s.accept()
    with conn:
        print(f"✅ Connected by {addr}")
        while True:
            # Receive data from the client
            data = conn.recv(1024)
            if not data:
                break
            # Decode the data and print it
            print(f"📩 Received from client: {data.decode()}")

            # Send a response back to the client
            response = f"Server received: {data.decode()}"
            conn.sendall(response.encode())
            print(f"📤 Sent response: {response}")

if __name__ == '__main__':
    server_program()
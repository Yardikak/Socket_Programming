import socket
import threading

def parse_request(request):
    # Memecah request menjadi bagian-bagian
    request_parts = request.split()
    file_path = ""
    method = "GET"
    # Jika request tidak kosong
    if len(request_parts) != 0:
        # Mengambil method dari request
        method = request_parts[0]
        print('req parts: ', request_parts)
        # print('method: ', method)
        # Mengambil path file dari request dan menghapus karakter '/' pada awal kata
        file_path = request_parts[1][1:] 
        # Jika path file kosong'
        if file_path == '':
            # Menggunakan 'index.html' sebagai default path file
            file_path = 'index.html'
    return method, file_path

def create_response(file_path, method):
    # Membuat respons HTTP
    if method == 'GET':
        try:
            # Membuka file dengan path yang diberikan
            with open(file_path, 'r') as file:
                # Membaca isi file dan menyusun respons HTTP
                response = f"HTTP/1.1 200 OK\n\n{file.read()}"
                print(f"File {file_path} terbuka")
        except FileNotFoundError:
            # Jika file tidak ditemukan, kirim respons '404 Not Found' dengan file HTML khusus
            try:
                with open('404.html', 'r') as error_file:
                    response = f"HTTP/1.1 404 Not Found\n\n{error_file.read()}"
                    print("File 404.html terbuka")
            except FileNotFoundError:
                # Jika file 404.html juga tidak ditemukan, kirim respons default
                response = "HTTP/1.1 404 Not Found\n\n404 Not Found"
                print("File 404.html Tidak Ditemukan")
    return response


def handle_client(client_socket):
    # Menerima data dari client (request)
        request = client_socket.recv(1024).decode()
        # Memecah request menjadi method dan path file
        method, file_path = parse_request(request)
        # Membuat respons HTTP berdasarkan path file dan method
        response = create_response(file_path, method)

        # Mengirim respons ke client
        client_socket.sendall(response.encode())
        # Menutup koneksi dengan client
        client_socket.close()

def run_web_server():
    # Membuat socket server
    # AF_INET: Menggunakan IPv4
    # SOCK_STREAM: Menggunakan TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Mengaitkan socket ke alamat dan port tertentu
    host = 'localhost'
    port = 80
    # Mengikat socket ke alamat host dan port tertentu
    server_socket.bind((host, port))
    # Mendengarkan koneksi yang masuk dengan batasan antrian sebesar 1
    server_socket.listen(1)
    print(f"Server berjalan di http://{host}:{port}")

    while True:
        # Menerima koneksi dari client
        client_socket, client_address = server_socket.accept()
        print(f"Koneksi diterima dari {client_address}")

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()
        
# Menjalankan server web dengan host 'localhost' dan port 7070
run_web_server()
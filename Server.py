#Server
from socket import * #Meng-import library socket
serverPort = 12000 #Membuat koneksi port
serverSocket = socket(AF_INET, SOCK_STREAM) #Membuat objek socket baru
serverSocket.bind(('', serverPort))  #Mengikat socket ke alamat dan port yang telah ditentukan
serverSocket.listen(1) #Mendengarkan koneksi TCP dari Client
print("The server is ready to recieve") #Menampilkan pesan server telah menerima
while True: #Menjalankan perulangan tanpa batas untuk menerima masukan dari client
    connectionSocket, addr = serverSocket.accept() #Menerima koneksi yang masuk dari client
    sentence = connectionSocket.recv(2048).decode() #Menerima data dari client
    capitalizedSentence = sentence.upper() #Memodifikasi kalimat menjadi kapital/Uppercase
    connectionSocket.send(capitalizedSentence.encode()) #Mengirim hasil modifikasi kepada client
    connectionSocket.close() #Menutup koneksi server
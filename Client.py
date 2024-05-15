#Client
from socket import* #Meng-import library socket

serverName = 'localhost' #Membuat nama server
serverPort = 12000 #Membuat koneksi port       	

clientSocket = socket(AF_INET, SOCK_STREAM) #Membuat objek socket baru
clientSocket.connect((serverName, serverPort)) #Membuat hubungan koneksi antar client dengan server
sentence = input('Input lowercase sentence: ') #Memberikan pesan berupa masukan/input
clientSocket.send(sentence.encode()) #Mengirimkan pesan "sentence" kepada server
modifiedSentence = clientSocket.recv(2048) #Menerima perubahan pesan "sentence" dari server
print('From server: ', modifiedSentence.decode()) #Memberikan pesan dari server berupa pesan "senttence" yang telah dimodifikasi
clientSocket.close() #Menutup koneksi client
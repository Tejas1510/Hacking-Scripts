#ALICE
import socket
s = socket.socket()
s.bind(("192.168.56.1",9999))
s.listen(3)
while True:
    c,addr = s.accept()
    print("client connect",addr)
    e=c.recv(1024)
    n=c.recv(1024)
    m = int(input("Enter the number to be sent: "))
    cipher = (m**int(e)) % int(n)
    print(f"The Cipher Text is: {cipher}")
    c.send(bytes(str(cipher),'utf-8'))
    

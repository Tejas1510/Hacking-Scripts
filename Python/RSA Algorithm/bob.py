#BOB
import math
import socket

c = socket.socket()
c.connect(("192.168.56.1",9999))
p = int(input("Enter prime no. (p): "))
q = int(input("Enter prime no. (q): "))
n = p*q;
phi = (p-1)*(q-1)
e = int(input("Bob, Enter the public key: "))

if e>1:
    if e<n:
        g = math.gcd(e,phi)
        if g==1:
            for i in range(1,phi):
                if (e*i)%phi==1:
                    d=i
            c.send(bytes(str(e),'utf-8'))
            c.send(bytes(str(n),'utf-8'))
            cipher = c.recv(1024)
            print(f"cipher text received is: {cipher}")
            m=(int(cipher)**d) % n
            print(f"message decrypted is: {m}")
        else:
            print("Invalid value of e")
    else:
        print("Invalid value of e")
else:
    print("Invalid value of e")
        

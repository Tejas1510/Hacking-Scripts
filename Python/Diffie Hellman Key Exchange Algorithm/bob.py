import socket 
def power(a,b,c):
    return ((a**b)%c)

c = socket.socket() 
c.connect(('192.168.1.101',9999))
p = c.recv(1024).decode()
q = c.recv(1024).decode()
x = c.recv(1024).decode()
s=int(input("Bob, enter your private key: "))
y = power(int(p),s,int(q))
c.send(bytes(str(y) ,'utf-8'))
kb = power(int(x),s,int(q))
print(f"The Key with Bob is: {kb}")



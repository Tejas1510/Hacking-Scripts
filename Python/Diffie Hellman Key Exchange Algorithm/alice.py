import socket

def power(a,b,c):
    return ((a**b)%c)

s = socket.socket() 
print("socket created")
s.bind(('192.168.1.101',9999))
print('Bind completed')
s.listen(3)
print('Server listening')

while True:
    c,addr = s.accept() 
    print('client connected', addr)
    p = int(input("Alice, Enter a prime number P: "))
    q = int(input("Alice, Enter a prime number Q: "))
    c.send(bytes(str(p),'utf-8'))
    c.send(bytes(str(q),'utf-8'))
    r = int(input("Alice, Enter your private number: "))
    x = power(p,r,q)
    print(f"X is: {x}")
    c.send(bytes(str(x),'utf-8'))
    y = c.recv(1024).decode()
    ka = power(int(y),r,q)
    print(f"The Key with Alice is: {ka}")
    c.close()

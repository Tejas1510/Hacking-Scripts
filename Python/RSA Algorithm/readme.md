## RSA Algorithm
RSA algorithm is asymmetric cryptography algorithm. Asymmetric actually means that it works on two different keys i.e. 
Public Key and Private Key. As the name describes that the Public Key is given to everyone and Private key is kept private.

An example of asymmetric cryptography :

A client (for example browser) sends its public key to the server and requests for some data.
The server encrypts the data using client’s public key and sends the encrypted data.
Client receives this data and decrypts it.

To know more about the logic of RSA Algorithm. Kindly visit https://www.geeksforgeeks.org/rsa-algorithm-cryptography/

## Libraries required for the game
- Socket
- Before working with the project, you need to keep ready ip address of your system. You can retrieve ip address by :
  In Command Prompt, run following command
  - On Windows
    ```ifconfig```
  - On MAC / LINUX based systems
    ```ipconfig```

## Steps to run the program
**1.** Fork [this](https://github.com/Tejas1510/Hacking-Scripts/) repository.
Click on the <a href="https://github.com/Tejas1510/Hacking-Scripts/"><img src="https://img.icons8.com/ios/24/000000/code-fork.png"></a> symbol at the top right corner.

**2.** Clone the forked repository.

```bash
git clone https://github.com/<your-github-username>/Hacking-Scripts
```
**3.** Navigate to the project directory.

```bash
cd Hacking-Scripts/python/RSA Algorithm
```
**4.** Run the python file.
- First run alice.py
```bash
python alice.py
```
- Then run bob.py
```bash 
python bob.py
```

## Output of Alice(Sender) file : 
    -You need to enter ip address of your system at underlined part :
   ![image](https://user-images.githubusercontent.com/59737567/138347454-dbcab6be-88ca-4e09-a914-0964d60d44e1.png)


## Output of Bob(Receiver) file : 
![image](https://user-images.githubusercontent.com/59737567/138347731-3cbb89fe-7f10-4d50-8d29-3529d91f5274.png)


### Contributed by : [@NikitaEmberi](https://github.com/NikitaEmberi)






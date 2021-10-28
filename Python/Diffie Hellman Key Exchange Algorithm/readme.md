## Diffie Hellman Key Exchange Algorithm
The Diffie–Hellman (DH) Algorithm is a key-exchange protocol that enables two parties communicating over public channel to establish a mutual secret without it being 
transmitted over the Internet. DH enables the two to use a public key to encrypt and decrypt their conversation or data using symmetric cryptography. </br>
***- https://www.hypr.com*** </br>

Symmetric encryption is a type of encryption where only one key (a secret key) is used to both encrypt and decrypt electronic information. The entities communicating via 
symmetric encryption must exchange the key so that it can be used in the decryption process. This encryption method differs from asymmetric encryption where a pair of keys, 
one public and one private, is used to encrypt and decrypt messages.

By using symmetric encryption algorithms, data is converted to a form that cannot be understood by anyone who does not possess the secret key to decrypt it. 
Once the intended recipient who possesses the key has the message, the algorithm reverses its action so that the message is returned to its original and understandable form.

To understand the Math behind DH Algorithm, Kindly visit https://mathworld.wolfram.com/Diffie-HellmanProtocol.html

## Libraries required for executing the algorithm :
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
# Demonstration of Exchange :
## Output of Alice(Sender) file : 
    -You need to enter ip address of your system at underlined part :
   ![image](https://user-images.githubusercontent.com/59737567/139343247-96b5a47b-5e37-486b-8b98-d61f1fa1f75d.png)

## Output of Bob(Receiver) file : 
![image](https://user-images.githubusercontent.com/59737567/139343330-22472403-62f7-4221-9752-2e480eda8a52.png)

## Conclusion:
As you can see how the secret key is established between sender and receiver without it being transmitted over the Internet to communicate with each other.

### References
- https://www.cryptomathic.com/news-events/blog/symmetric-key-encryption-why-where-and-how-its-used-in-banking


### Contributed by : [@NikitaEmberi](https://github.com/NikitaEmberi)

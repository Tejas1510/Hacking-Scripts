<h1 align="center"> File Transfer </h1>
<hr>

<h2>Description:</h2>

A. Steps to create the socket program on word transfer from client to server with Ubuntu on VM as the server:
- While creating the server file on Ubuntu(file_transfer_server):
	- a. First created a socket
	- b. Took an arbitary port number greater than 1023(in this case it is 2110) for the transfer of infromation
	- c. Binded the ports of the client and server
	- d. Listened to the client for information
	- e. Received the file name from the client
	- f. Opened a file with the same filename in write mode
	- g. Received the contents of the file and wrote it on the new file
	- h. Sent that the file has been received
	- i. Ended the connection
- While creating the client file on Windows(word_transfer_client):
	- a. First created a socket
	- b. Took the same port number as in the server(in this case 3603)
	- c. Looked for the ip address in the Ubuntu on VM
	- d. Entered the ip address for connecting with the server
	- e. Sent the filename to the server
	- f. Sent the file contents to the server
	- g. Received the file sending result from the server
	- h. Displayed it to the client
	- i. Ended the connection

<hr>

<h2>How to use:</h2>

- Need to switch off the local firewall in both the pcs
- To run the server in a VM or in a different computer and the client in the different computer and change the IP in the client folder based on the IP of the VM/Computer.

<hr>

<h2>Output</h2>
<img src = "https://github.com/kumarjeetray/Hacking-Scripts/blob/main/Python/File%20Transfer/Images/file_transfer_client_ss.jpg" />
<img src = "https://github.com/kumarjeetray/Hacking-Scripts/blob/main/Python/File%20Transfer/Images/file_transfer_server_ss_1.jpg" />
<img src = "https://github.com/kumarjeetray/Hacking-Scripts/blob/main/Python/File%20Transfer/Images/file_transfer_server_ss_2.jpg" />



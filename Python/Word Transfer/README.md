<h1 align="center"> Word Transfer </h1>
<hr>

<h2>Description:</h2>

A. Steps to create the socket program on word transfer from client to server with Ubuntu on VM as the server:
- First created a python file on ubuntu which contains a list of words
- Imported the words file while creating the server file on Ubuntu
- While creating the server file on Ubuntu(word_transfer_server):
	a. First created a socket
	b. Took an arbitary port number greater than 1023(in this case it is 3603) for the transfer of infromation
	c. Binded the ports of the client and server
	d. Listened to the client for information
	e. Received the word from the client
	f. Checked if the word was present in the predefined list
	g. Passed back the result of the search to the client
	h. Ended the connection
- While creating the client file on Windows(word_transfer_client):
	a. First created a socket
	b. Took the same port number as in the server(in this case 3603)
	c. Looked for the ip address in the Ubuntu on VM
	d. Entered the ip address for connecting with the server
	e. Took the word from the client
	f. Sent the word to check if it's present in the list
	g. Received the search result from the server
	h. Displayed it to the client
	i. Ended the connection

## Output
<hr>
<h2>Third-Party Libraries Required:</h2>
N.A
<h2>How to install the above Library:</h2>
N.A
<hr>
<h2>How to use:</h2>

- Need to switch off the local firewall in both the pcs
- To run the server in a VM or in a different computer and the client in the different computer and change the IP in the client folder based on the IP of the VM/Computer.

<hr>

<h2>Input</h2>
<img src="https://github.com/kumarjeetray/Hacking-Scripts/blob/main/Python/Word%20Transfer/Images/word_transfer_client_ss_1.jpg" />
<img src="https://github.com/kumarjeetray/Hacking-Scripts/blob/main/Python/Word%20Transfer/Images/word_transfer_client_ss_2.jpg" />
<h2>Output</h2>
<img src="https://github.com/kumarjeetray/Hacking-Scripts/blob/main/Python/Word%20Transfer/Images/word_transfer_server_ss.jpg" />


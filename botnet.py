import optparse
from pexpect import pxssh

# Resul Ucar 
# SSH Botnet
# Before running!
# pip3 install pexpect
# sudo apt install ssh
# sudo service ssh start
# To use: python3 sshbot.py


class Client: # create a client class

	def __init__(self, host, user, password): #assigning credentials
		self.host = host
		self.user = user
		self.password = password      
		self.session = self.connect()
	def connect(self):
		try:
			s = pxssh.pxssh() # screen scraping wrapper around your ssh session
			s.login(self.host, self.user, self.password)
			return s
		except Exception as e: # catching error exception
			print(e)
			print('[-] Error Connecting')
	def send_command(self, cmd): #function to send input to terminal during session
			self.session.sendline(cmd)
			self.session.prompt()
			return self.session.before
def botnetCommand(command): #function to send commands to the bot
	for client in botNet:
		output = client.send_command(command)
		print('[*] Output from ' + client.host)
		print('[+] ' +str(output, encoding='utf-8')+ '\n')

def addClient(host, user, password):
	client = Client(host, user, password) #instantiating the class
	botNet.append(client)
	
botNet = [] #array to store bots

#to add more clients add the host, username and password
addClient('10.0.2.255', 'resul', 'hello123')

#you can change the command to send to the bot
botnetCommand('ls')
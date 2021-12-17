def Bit():
    flag = []
    for i in range(16):
        flag.append(0)
    return flag

def bit_set(flag, index):
    flag[index//64] |= 1 << (index % 64)

def bit_clear(flag, index):
    flag[index//64] &= ~(1 << index % 64)

def bit_isset(flag, index):
    return flag[int(index//64)] & (1 << (index % 64))
# -*- coding: utf-8 -*-
import ctypes
import sys


class SDBM(object):

    def int_overflow(self, val):
        maxint = 2147483647
        if not -maxint - 1 <= val <= maxint:
            val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
        return val

    def unsigned_right_shitf(self, n, i):
        # 数字小于0，则转为32位无符号uint
        if n < 0:
            n = ctypes.c_uint32(n).value
        # 正常位移位数是为正数，但是为了兼容js之类的，负数就右移变成左移好了
        if i < 0:
            return -self.int_overflow(n << abs(i))

        return self.int_overflow(n >> i)

    def sdbm(self, string, mod):

        hash = 0
        for i in range(len(string)):
            hash = ord(string[i]) + self.int_overflow(hash << 6) + self.int_overflow(hash << 16) - hash

        sdbmNumber = self.unsigned_right_shitf(hash, 0)
        modNumber = sdbmNumber % mod

        return sdbmNumber, modNumber


if __name__ == '__main__':
    value, mod = sys.argv[1], sys.argv[2]
    try:
        mod = int(mod)
        sdbmNumber, modNumber = SDBM().sdbm(value, mod)
        print('sdbmNumber is %s \nmodNumber is %s' % (sdbmNumber, modNumber))
    except ValueError, e:
        print('mod value error')

#!/usr/bin/python3
class Mgc:
    x = 0
    def magic_string():
        Mgc.x += 1
        return ''.join(f"BestSchool{', ' if i < Mgc.x - 1 else ''}" for i in range(Mgc.x))

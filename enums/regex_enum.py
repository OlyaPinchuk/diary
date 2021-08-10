from enum import Enum


class RegEx(Enum):
    NAME = ('^[a-zA-Z]{2,255}$', 'Only Alfa, min 2, max 255')
    PASSWORD = ('^(?=.*\\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\\w\\d\\s:])([^\\s]){8,20}$',
                'password must have 8-20ch, 1uppercase, 1int, 1spec')

    def __init__(self, reg, msg):
        self.reg = reg
        self.msg = msg

# 0. test data
register = 0b00000100
bit_mask = 0b00000100


# 1. Check the state of the bit via AND
"""
register = 0b00000100
bit_mask = 0b00000100 &
------------------------
register = 0b00000100
"""

state = None
if register & bit_mask:
    print("Bit is '1'!")
    state = 1
else:
    print("Bit is '0'!")
    state = 0


# 2. Reset the bit (== set to '0') via ~AND
"""
register =  0b00000100
~bit_mask=  0b11111011 &
------------------------
register =  0b00000000
"""

register = register & ~bit_mask
# register &= ~bit_mask


# 3. Set bit (== set to '1') via OR
"""
register = 0b00000000
bit_mask = 0b00000100 |
------------------------
register = 0b00000100
"""

register = register | bit_mask
# register |= bit_mask


# 4. Negate bit (0->1 ; 1->0) via XOR
"""
register = 0b00000100
bit_mask = 0b00100100 ^
------------------------
register = 0b00100000
"""

register = register ^ bit_mask
# register ^= bit_mask

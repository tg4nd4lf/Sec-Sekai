class BitOperations:
    """
    Class that contains different methods for altering bits.
    """

    def __init__(self, bit_string):
        self.bit_string = bit_string

    @staticmethod
    def create_bit_mask(position: int) -> int:

        return 1 << position  # e.g. 0010 0000

    def check_bit_state(self, position: int) -> int:
        """
        Checks if the bit on the given position is '0' or '1' and
        returns this information.

        :param position: Position to check.
        :return: 1 or 0.
        """

        bit_mask = self.create_bit_mask(position=position)  # e.g. 0010 0000

        if self.bit_string & bit_mask:
            return 1
        else:
            return 0

    def reset_bit(self, position: int) -> None:
        """
        Reset the bit (== set to '0') via ~AND.

        :param position: Position to reset.
        :return:
        """

        bit_mask = self.create_bit_mask(position=position)  # e.g. 0010 0000

        self.bit_string &= ~bit_mask  # bit_string = bit_string & ~bit_mask

    def set_bit(self, position: int) -> None:
        """
        Set bit (== set to '1') via OR.

        :param position: Position to set.
        :return:
        """

        bit_mask = self.create_bit_mask(position=position)  # e.g. 0010 0000

        self.bit_string |= bit_mask  # bit_string = bit_string | bit_mask

    def negate_bit(self, position: int) -> None:
        """
        Negate bit (0->1 ; 1->0) via XOR/

        :param position: Position to negate.
        :return:
        """

        bit_mask = self.create_bit_mask(position=position)  # e.g. 0010 0000

        self.bit_string ^= bit_mask  # bit_string = bit_string ^ bit_mask

    def binary_shift(self, direction: str, positions: int = 1) -> None:
        """
        Shift in direction (left/right) positions.

        :param direction: Left: 'r' or right: 'r'.
        :param positions: How many positions to shit.
        :return:
        """

        if direction != 'l' or direction != 'r':
            return

        if direction == 'l':
            self.bit_string <<= positions  # bit_string = bit_string << 1
        else:
            self.bit_string >>= positions  # bit_string = bit_string >> 1


if __name__ == "__main__":
    register = 0b11111111  # 255

    c = BitOperations(bit_string=register)
    print(c.check_bit_state(3))  # 1
    c.negate_bit(3)
    print(c.bit_string)  # 0b11110111 (247)
    c.set_bit(3)
    print(c.bit_string)  # 0b11111111 (255)
    c.reset_bit(3)
    print(c.bit_string)  # 0b11110111 (247)

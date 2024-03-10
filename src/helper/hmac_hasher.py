import hashlib
import hmac


def create_hmac_hash(key_str: str, message_str: str, hash_algorithm: str = 'sha256') -> hmac:
    """
    Creates an HMAC hash with the specified key, message and hash algorithm.

    :param key_str: The key to the HMAC (bytes).
    :param message_str: Message to hash.
    :param hash_algorithm: The hash algorithm. The default is SHA256.
    :return: The HMAC hash (bytes).
    """

    __key = key_str.encode()  # str --> bytes
    __message = message_str.encode()  # str --> bytes

    return hmac.new(__key, __message, getattr(hashlib, hash_algorithm))


if __name__ == '__main__':
    # example:
    key = 'my_key'
    message = 'My message to hash.'
    hmac_hash = create_hmac_hash(key_str=key, message_str=message)

    print("HMAC-Hash:", hmac_hash.hex())

import base64

from Cryptodome.Cipher import AES
from Cryptodome.Hash import SHA1
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Util.Padding import pad, unpad

SALT_RAW: str = "tu89geji340t89u2"
PASSPHRASE_RAW: str = "PlayerData"


def generate_vault_key(passphrase: str) -> bytes:
    passphrase_b64: bytes = base64.b64encode(passphrase.encode("utf-8"))
    derived_input: bytes = passphrase_b64[:8]

    # PBKDF2 returns 32 bytes for AES-256
    return PBKDF2(
        derived_input,
        SALT_RAW.encode("utf-8"),
        dkLen=32,
        count=1000,
        hmac_hash_module=SHA1,
    )


def decrypt_save(encrypted_base64: str) -> str:
    """
    Decodes the Base64 cipher text and decrypts using Rijndael-128 CBC.
    Returns the JSON data string.
    """
    key: bytes = generate_vault_key(PASSPHRASE_RAW)
    cipher_text: bytes = base64.b64decode(encrypted_base64)

    # IV is reused from SALT
    cipher = AES.new(key, AES.MODE_CBC, iv=SALT_RAW.encode("utf-8"))

    try:
        # Decrypt and remove PKCS7 padding
        decrypted_raw: bytes = cipher.decrypt(cipher_text)
        decrypted_data: bytes = unpad(decrypted_raw, AES.block_size)
        return decrypted_data.decode("utf-8")
    except (ValueError, KeyError) as e:
        raise ValueError(f"Decryption failed: {str(e)}")


def encrypt_save(data: str) -> str:
    """
    Converts a Python dict/list to JSON and encrypts it.
    Returns a Base64 encoded string.
    """
    key: bytes = generate_vault_key(PASSPHRASE_RAW)

    data_bytes: bytes = data.encode("utf-8")

    cipher = AES.new(key, AES.MODE_CBC, iv=SALT_RAW.encode("utf-8"))

    # Add PKCS7 padding and encrypt
    cipher_text: bytes = cipher.encrypt(pad(data_bytes, AES.block_size))
    return base64.b64encode(cipher_text).decode("utf-8")

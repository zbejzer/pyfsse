import sys

from pyfsse.crypto import decrypt_save, encrypt_save


def main() -> None:
    filename: str = sys.argv[1]

    with open(filename, "r") as f:
        decrypted_json = decrypt_save(f.read())

    with open(f"{filename}.json", "w") as f:
        f.write(decrypted_json)

    encrypted_json = encrypt_save(decrypted_json)

    with open(f"{filename}.json.sav", "w") as f:
        f.write(encrypted_json)


if __name__ == "__main__":
    main()

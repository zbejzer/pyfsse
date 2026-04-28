import json
import pathlib

from pyfsse.crypto import decrypt_save
from pyfsse.save_schema import *
from pyfsse.types import JsonData


def deserialize_vault(data: str) -> JsonData:
    return json.loads(data)


def serialize_vault(data: JsonData) -> str:
    # # Use separators to ensure no extra whitespace
    # json_str: str = json.dumps(data, separators=(",", ":"))
    # json_bytes: bytes = json_str.encode("utf-8")

    raise NotImplementedError()


def load_vault(filepath: pathlib.Path) -> JsonData:
    try:
        with filepath.open(mode="r") as f:
            decrypted_json = decrypt_save(f.read())
    except OSError as e:
        return Dict()

    return deserialize_vault(decrypted_json)


def save_vault(filepath: pathlib.Path, data: JsonData) -> None:
    raise NotImplementedError()

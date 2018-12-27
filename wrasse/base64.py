import io
import base64

def to_bytes(base64str): 
    return io.BytesIO(base64.b64decode(base64str.encode()))

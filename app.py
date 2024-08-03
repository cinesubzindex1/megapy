from mega import Mega
import os

# Initialize Mega
mega = Mega()

# Log in using environment variables
email = os.getenv('MEGA_EMAIL')
password = os.getenv('MEGA_PASSWORD')
if not email or not password:
    raise ValueError("MEGA_EMAIL and MEGA_PASSWORD must be set as environment variables")

m = mega.login(email, password)

# Directory to upload files from
local_directory = 'path/to/your/local/files'

# Upload files
for filename in os.listdir(local_directory):
    file_path = os.path.join(local_directory, filename)
    if os.path.isfile(file_path):
        print(f"Uploading {filename}")
        m.upload(file_path)

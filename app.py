from mega import Mega
import os

# Initialize Mega
mega = Mega()
# Log in using environment variables
m = mega.login(os.getenv('MEGA_EMAIL'), os.getenv('MEGA_PASSWORD'))

# Directory to upload files from
local_directory = 'path/to/your/local/files'

# Upload files
for filename in os.listdir(local_directory):
    if os.path.isfile(os.path.join(local_directory, filename)):
        m.upload(os.path.join(local_directory, filename))

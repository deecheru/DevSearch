import subprocess
import time

# Start the Django server
server_process = subprocess.Popen(["python", "manage.py", "runserver"])

# Wait for the specified duration (e.g., 5 minutes)
time.sleep(30)

# Stop the server
server_process.terminate()

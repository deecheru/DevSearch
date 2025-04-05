#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

#import signal
#import time
#from threading import Timer
#from django.core.management import execute_from_command_line

def stop_server():
    print("Stopping Django server after timeout...")
    os.kill(os.getpid(), signal.SIGINT)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devsearch.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    #Timer(30, stop_server).start()
    execute_from_command_line(sys.argv)
    


if __name__ == '__main__':
    main()



  # Send interrupt signal

# Set a timer to stop the server after 5 minutes (300 seconds)


#if __name__ == "__main__":
   # execute_from_command_line(["manage.py", "runserver"])


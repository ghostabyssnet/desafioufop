from django.test import TestCase

# We don't have many test cases to worry about, so I'll just create a quick
# debug message for this little project.

# Disable this to disable debug messages.
VIRTUAL_DEBUG = True

def debug(message):
    if VIRTUAL_DEBUG:
        print(message)
    else:
        pass

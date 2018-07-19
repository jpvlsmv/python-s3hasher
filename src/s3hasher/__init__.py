__version__ = '0.1.1'
import sys

if sys.version_info < (3,):
    raise ImportError(
    """You are running s3hasher on Python 2

s3hasher is not compatible with Python 2, and you still 
ended up with this version installed. That's unfortunate; sorry about that. 
It should not have happened. Make sure you have pip >= 9.0 to avoid this kind 
of issue, as well as setuptools >= 24.2:

 $ pip install pip setuptools --upgrade

Your choices:

- Upgrade to Python 3.

It would be great if you can figure out how this version ended up being
installed, and try to check how to prevent that for future users.

See the following URL for more up-to-date information:

https://github.com/jpvlsmv/python-s3hasher/

""")
if sys.version_info < (3,6):
    raise ImportError(
    """You are running s3hasher on too low of a Python 3

s3hasher is not compatible with Python 3.x < 3.6, and you still 
ended up with this version installed. That's unfortunate; sorry about that. 
It should not have happened. Make sure you have pip >= 9.0 to avoid this kind 
of issue, as well as setuptools >= 24.2:

 $ pip install pip setuptools --upgrade

Your choices:

- Upgrade to Python 3.6
- Create a virtualenv with python>=3.6 and activate that

It would be great if you can figure out how this version ended up being
installed, and try to check how to prevent that for future users.

See the following URL for more up-to-date information:

https://github.com/jpvlsmv/python-s3hasher/

""")

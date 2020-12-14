# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='miro_uploader',  # Required
    version='0.1',  # Required
    description='A simple tool to upload/push new files to provided git repo',  # Optional
    url='https://github.com/pypa/sampleproject',  # Optional
    author='smate82',  # Optional
    author_email='author@example.com',  # Optional
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
   ],
    py_modules=["watchdog"],
    #
    #packages=find_packages(where='src'),  # Required
    python_requires='>=3.5, <4',
    install_requires=['peppercorn'],  # Optional
    entry_points={  # Optional
        'console_scripts': [
            'miro_uploader=miro_uploader:main',
        ],
    }
)

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

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
    packages=['miro_uploader'],  # Required
    python_requires='>=3.6, <4',
    install_requires=['watchdog'],  # Optional
    entry_points={  # Optional
        'console_scripts': [
            'miro_uploader=miro_uploader:main',
        ],
    }
)

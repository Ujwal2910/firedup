from os.path import join, dirname, realpath
from setuptools import setup
import sys

assert sys.version_info.major == 3 and sys.version_info.minor >= 6, \
    "The Spinning Up repo is designed to work with Python 3.6 and greater." \
    + "Please install it before proceeding."

setup(
    name='spinup',
    py_modules=['spinup'],
    version='0.0.1',
    install_requires=[
        'cloudpickle',
        'gym[atari,box2d,classic_control]',
        'ipython',
        'joblib',
        'matplotlib',
        'mpi4py',
        'numpy',
        'pandas',
        'pytest',
        'psutil',
        'scipy',
        'seaborn',
        'torch',
        'tqdm'
    ],
    description="Teaching tools for introducing people to deep RL.",
    author="Joshua Achiam",
)

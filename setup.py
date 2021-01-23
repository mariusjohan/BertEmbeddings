from setuptools import setup, find_packages
from distutils.command.clean import clean
import os

install_requirements = [i.replace('\n','') for i in open('./requirements.txt').readlines()]
    
classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

os.system('pip install -r requirements.txt --find-links https://download.pytorch.org/whl/torch_stable.html')

setup(
    name = 'embeddings lib',
    version = '0.0.1',
    description = 'Create positional embeddings based on TinyBERT',
    long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url = 'https://github.com/Sorcely/EmbeddingsLib',
    author = 'Marius J. Schlichtkrull',
    author_email = 'marius.schlichtkrull@gmail.com',
    license = 'MIT',
    classifiers = classifiers,
    keywords = 'embeddings',
    packages = find_packages(),
)
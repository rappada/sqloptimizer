from setuptools import setup, find_packages

setup(
    name='SQLOptimizer',
    version='2.1.3',
    packages=find_packages(),
    install_requires=[
        'discord.py',
        'requests'
    ],
    author='Rappada',
    author_email='rappada@gmail.com',
    description='A library to secure your sql in discord.py, discord.js or teamspeak!',
    long_description=open('README.md').read(),
    long_description_content_type='',
    url='-',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

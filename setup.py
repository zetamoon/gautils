import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='gautils',
    version='0.1',
    author='Jihoon Moon',
    author_email='jh03.moon@gmail.com',
    description='A module for making genetic algorithms',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    url='https://github.com/zetamoon/gautils',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

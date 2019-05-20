import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyLidar2",
    python_requires="<3",
    version="1.5",
    author="Lakshman mallidi",
    author_email="lakshman.mallidi@gmail.com",
    description="Library for Lidar. Currently supports YdLidar(X4,G4) from http://www.ydlidar.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lakshmanmallidi/PyLidar2",
    packages=['PyLidar2'],
    install_requires=[
        'pyserial',
        'enum'
    ],
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
   

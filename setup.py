import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bulksms-zw-donald",
    version="1.0.0",
    author="Donald Chinhuru",
    author_email="donychinhuru@gmail.com",
    description="",
    long_description=long_description,
    url="https://github.com/DonnC/BulkSms-ZW",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
)  
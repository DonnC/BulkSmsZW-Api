import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bulksms-donald",
    version="1.2.0",
    author="Donald Chinhuru",
    author_email="donychinhuru@gmail.com",
    description="send text messages with bulksmszw api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DonnC/BulkSms-ZW",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
)  

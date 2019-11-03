import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIRED = [
    'requests'
]

setuptools.setup(
    name="bulksmszw",
    version="1.0.0",
    author="Donald Chinhuru",
    author_email="donychinhuru@gmail.com",
    description="send text messages with bulksmszw api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DonnC/BulkSmsZW-Api",
    license="MIT",
    install_requires=REQUIRED,
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
)  

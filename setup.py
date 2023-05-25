import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pam-python-sdk",
    version="1.0.0",
    author="Ian  Duncan",
    author_email="ian.duncan@shiftech.co.ke",
    description="PAM api intergration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SHIFTECH-AFRICA/pam-python-sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
    ],
)
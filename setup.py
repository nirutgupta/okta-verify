from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="cloudera_vpn",
    version="0.1.0",
    description="Connects/ Disconnect to connect.cloudera.com VPN",
    long_description=long_description,
    author="Nirut Gupta",
    author_email="nirutgupta78@gmail.com",
    classifiers=[
        "Development Status ::  Phase 1",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7.5 && 2.7 ",
    ],
    keywords="okta verify multi factor authentication",
    packages=find_packages(),
    install_requires=[
        "pika==1.1.0",
        "psutil==5.6.7",
        "requests==2.22.0",
        "fallocate==1.6.4",
        "six==1.13.0",
        "enum34==1.1.9",
        "boto3==1.14.8",
        "daemons==1.3.1",
        "PyYAML==5.3.1"
    ],
    include_package_data=True,
    zip_safe=False
)

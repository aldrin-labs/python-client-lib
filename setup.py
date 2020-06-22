import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ccai-client", # Replace with your own username
    version="0.0.5",
    author="Cryptocurrencies.AI",
    author_email="support@cryptocurrencies.ai",
    description="Cryptocurrencies.AI client library for trading",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cryptocurrencies-AI/python-client-lib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

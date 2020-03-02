import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="antiplagiarism",
    version="0.0.2",
    author="Bernardi Riccardo",
    author_email="riccardo.bernardi@rocketmail.com",
    description="antiplagiarism library to detect plagiarism especially on code works",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/riccardobernardi/antiplagiarism",
    packages=setuptools.find_packages()+['antiplagiarism'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
		'pygraham'
    ],
)
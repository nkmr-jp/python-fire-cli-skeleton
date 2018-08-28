import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sample-command",
    version="0.0.1",
    author="[author]",
    author_email="[author_email]",
    description="[description]",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nkmr-jp/python-fire-cli-skeleton",
    install_requires=["fire"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=["sample_command"],
    entry_points={"console_scripts": ["sample_command=sample_command:main"]},
)

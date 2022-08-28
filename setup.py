import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="json_parser",
    version="0.1.0",
    author="Sumbono",
    author_email="sumbono102@gmail.com",
    description=("A json file parser package to demonstrate python cli module and tool packaging."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sumbono/json_parser",
    project_urls={
        "Bug Tracker": "https://github.com/sumbono/json_parser/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    packages=setuptools.find_packages(),
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "json_parser = json_parser.cli:main",
        ]
    }
)
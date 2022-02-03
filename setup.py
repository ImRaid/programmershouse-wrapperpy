import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="houseprogrammers-wrappers",
    version="1.0.0",
    author="Programmershouse", author_email="houseprogrammers@gmail.com",
    url = "https://www.programmershouse-api.ga",
    description="ProgrammersHouse Api official wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['discord', 'discordpy', 'programmershouse'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=["requests", "json"]
)

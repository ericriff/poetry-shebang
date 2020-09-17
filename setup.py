from setuptools import setup
import os

with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8") as f:
    readme = f.read()

if os.path.exists("/bin/bash"):
    scripts = ["bash/poetry-shebang"]
else:
    scripts = ["py/poetry-shebang"]

setup(
    name="poetry-shebang",
    version="0.0.4",
    url="https://github.com/ericriff/poetry-shebang",
    author="Eric Riff",
    author_email="ericriff@gmail.com",
    description="poetry-shebang allows you to put scripts in your path that run in a poetry environment.",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=[],
    install_requires=[],
    scripts=scripts,
    data_files=[("py", ["py/poetry-shebang"]), ("bash", ["bash/poetry-shebang"])],
)

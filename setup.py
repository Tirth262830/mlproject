from setuptools import find_packages, setup
from typing import List
import os

PROJECT_NAME = "mlproject"
VERSION = "0.0.1"
AUTHOR = "Tirth Parikh"
AUTHOR_EMAIL = "parikhtirth77@gmail.com"
REPO_URL = "https://github.com/Tirth262830/mlproject"

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, encoding="utf-8") as file:
        requirements = [req.strip() for req in file.readlines()]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements


with open(os.path.join(ROOT_DIR, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="End-to-end machine learning project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=REPO_URL,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=get_requirements(os.path.join(ROOT_DIR, "requirements.txt")),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
)

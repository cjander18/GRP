import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="grp",
    version="0.0.1",
    maintainer="Clinton Anderson",
    maintainer_email="cjander18@gmail.com",
    description="Geometric returns on a portfolio of 4 assets.",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"],
    extras_require={"test": ["pytest", "coverage"]},
    python_requires='>=3.7',
)
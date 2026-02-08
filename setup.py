from setuptools import setup, find_packages

setup(
    name="educational_rag_assistant",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)

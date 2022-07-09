from setuptools import setup, find_packages
import os
import io

def read(*filenames, **kwargs):
    encoding = kwargs.get("encoding", "utf-8")
    # io.open defaults to \n as universal line ending no matter on what system
    sep = kwargs.get("sep", "\n")
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

def read_requirements(req="base.txt"):
    content = read(os.path.join("requirements", req))
    requirements = list()
    for line in content.split("\n"):
        line = line.strip()
        if line.startswith("#"):
            continue
        elif line.startswith("-r"):
            requirements.extend(read_requirements(line[3:]))
        else:
            requirements.append(line)
    return requirements

setup(
    name='yourscript',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements('base.txt'),
    entry_points={
        'console_scripts': [
            'kawaii-pugs = cli.main:cli'
        ]
    }
)
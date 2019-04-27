from setuptools import setup, find_packages


def get_version():
    return "0.0.1"


setup(
    name='jeecf',
    version=get_version(),
    packages=find_packages(exclude=["tests*"]),
    entry_points={
        "console_scripts": ["jeecf=jeecf.command:main"]
    },
    install_requires=[
        'requests',
        'click'
    ],
    include_package_data=True,
    author="tcitry",
    author_email="tcitry@gmail.com",
    description="Jeecf client toolbox",
    license="Apache License 2.0",
    keywords="cloud factory client commandline",
    url="https://github.com/cgfly/jeecf-cli",
)

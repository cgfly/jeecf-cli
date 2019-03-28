from setuptools import setup, find_packages


def get_version():
    return "v0.1"


setup(
    name='jeecf',
    version=get_version(),
    packages=find_packages(),
    entry_points={
        "console_scripts": ["jeecf = jeecf-cli.jeecf:main"]
    },
    install_requires=[
        'requests',
        'retrying'
    ],
    include_package_data=True,
    author="tcitry",
    author_email="tcitry@gmail.com",
    description="Jeecf client toolbox",
    license="Apache License 2.0",
    keywords="cloud factory client commandline",
    url="https://github.com/cgfly/jeecf-cli",
    project_urls={
        "Jeecf page": "https://github.com/cgfly/jeecf",
        "Documentation": "https://github.com/cgfly/jeecf-cli/wiki",
        "Source Code": "https://github.com/cgfly/jeecf-cli",
    },
)
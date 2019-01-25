"""
O módulo de instalação.
"""

import os
from setuptools import find_packages
from setuptools import setup

BASE_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


def get_long_description():
    """
    Retorna a descrição longa.

    :return: A descrição longa.
    :rtype: str
    """

    with open(
        os.path.join(BASE_DIRECTORY, 'README.md'),
        'r',
        encoding='utf-8'
    ) as readme_file:
        return readme_file.read()


def get_packages():
    """
    Retorna os pacotes utilizados.

    :return: Os pacotes utilizados.
    :rtype: list(str)
    """

    packages = find_packages(exclude=['tests'])
    packages.append('')

    return packages


def get_package_data():
    """
    Retorna os pacotes utilizados com os arquivos estáticos.

    :return: Os pacotes utilizados com os arquivos estáticos.
    :rtype: dict(str, list(str))
    """
    package_data = {'': ['requirements.txt']}

    return package_data


def get_requirements():
    """
    Retorna o conteúdo do arquivo 'requirements.txt' através de uma lista.

    :return: O conteúdo do arquivo 'requirements.txt'.
    :rtype: list(str)
    """

    requirements = []
    with open(
        os.path.join(BASE_DIRECTORY, 'requirements.txt'),
        'r',
        encoding='utf-8'
    ) as requirements_file:
        lines = requirements_file.readlines()
        for line in lines:
            requirements.append(line.strip())
    return requirements

setup(
    name='dayout',
    description=(
        'Um servidor web para o gerenciamento de pacotes turisticos.'
    ),
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    version='1.0.0',
    url='https://github.com/mikefarias/vou_viajar',
    packages=get_packages(),
    package_data=get_package_data(),
    install_requires=get_requirements()
)

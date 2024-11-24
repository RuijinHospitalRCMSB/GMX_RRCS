# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='gmx_rrcs',
    version='0.1.6',
    author='',
    author_email='iqtzhou@gmail.com',
    description='The gmx_rrcs script is designed to calculate the residues-residues contact scores (rrcs) from a trajectory file generated by GROMACS.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/zhaolabSHT/GMX_RRCS',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    install_requires=[
        'colorama>=0.4.6',
        'matplotlib>=3.7.1',
        'MDAnalysis>=2.4.3',
        'numba>=0.60.0',
        'numpy>=1.23.5',
        'packaging>=24.1',
        'seaborn>=0.13.2',
        'termcolor>=2.4.0',
    ],
    entry_points={
        'console_scripts': [
            'gmx_rrcs=packages.gmx_rrcs:main',
            'gmxout2csv=packages.gmxout2csv:main',
            'rrcs=packages.rrcs:main',
        ],
    },
    include_package_data=True,
)


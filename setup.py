#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='vxfld',
    version='2.1',
    description='VXLAN Flooding Service',
    author='Cumulus Networks/Metacloud Engineering',
    author_email='info@cumulusnetworks.com',
    url='cumulusnetworks.com',
    scripts=[
        'bin/vxrd',
        'bin/vxrdctl',
        'bin/vxsnd',
        'bin/vxsndctl'
    ],
    setup_requires=[
        'setuptools>=0.6cc1'
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'docopt==0.6.1',
        'dpkt==1.9.2',
        'eventlet~=0.17',
        'protobuf',
        'python-daemon'
    ],
    license='GPLv2'
)

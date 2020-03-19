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
        'dpkt==1.8.6.2',
        'eventlet>=0.17',
        'protobuf==2.4.1',
        'python-daemon==1.5.5'
    ],
    license='GPLv2'
)

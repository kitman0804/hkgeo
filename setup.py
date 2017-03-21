# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='hkgeo',
    version='0.1',
    description='Hong Kong Geodesy.',
    long_description='Hong Kong Geodesy.',
    keywords='hk80g hk80 wgs84 geodesy',
    url='https://github.com/kitman0804/hkgeo',
    author='kitman0804 @ https://github.com/kitman0804',
    author_email='kitman0804@gmail.com',
    license='MIT',
    packages=[
        'hkgeo',
        'hkgeo.distance',
        'hkgeo.geometry',
        'hkgeo.transform',
    ],
    install_requires=[
        'numpy',
        'scipy'
    ],
    include_package_data=True,
    zip_safe=False
)


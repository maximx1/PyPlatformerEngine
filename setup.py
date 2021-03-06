#!/usr/bin/env python

from distutils.core import setup

setup(name='pyplatformerengine',
    version='1.3.0.0',
    description='Python Platformer Engine',
    author='Justin Walrath',
    author_email='walrathjaw@gmail.com',
    url='https://github.com/maximx1/PyPlatformerEngine',
    packages=[
        'pyplatformerengine',
        'pyplatformerengine.actors',
        'pyplatformerengine.components',
        'pyplatformerengine.engine',
        'pyplatformerengine.entities',
        'pyplatformerengine.models',
        'pyplatformerengine.physics',
        'pyplatformerengine.utilities'        
    ],
)
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from setuptools import setup

################################################################################
# 
#    Version determination
# 
################################################################################

try:
    import versioneer
    version = versioneer.get_version()
    
except:
    version = "dev"
    
finally:
    import os
    os.chdir( os.path.split( os.path.abspath( __file__ ) )[ 0 ] )
    
    with open( "wsq/version.py", "w+" ) as fp:
        fp.write( "__version__ = '%s'" % version )

################################################################################
# 
#    Setup configuration
# 
################################################################################

setup( 
    name = 'WSQ',
    version = version,
    description = 'Python library for encoding and decoding WSQ files. Simple wrapper for the NBIS library.',
    author = 'Marco De Donno',
    author_email = 'Marco.DeDonno@unil.ch; mdedonno1337@gmail.com',
    packages = [
        'wsq'
    ],
 )

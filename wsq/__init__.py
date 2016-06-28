#!/usr/bin/env python
#  *-* coding: cp850 *-*

from MDmisc.TemporaryDirectory import TemporaryDirectory
from MDmisc.imageprocessing import PILToRAW
import os
import random

from PIL import Image


libdir = os.path.split( os.path.abspath( __file__ ) )[ 0 ] + "/NBIS/"

class wsq:
    def __init__( self ):
        self.r = "2.25"
    
    def encode( self, img, size = ( 512, 512 ), res = 500 ):
        if isinstance( img, Image.Image ):
            img, size = PILToRAW( img ), img.size
        
        with TemporaryDirectory() as tempdir:
            os.chdir( tempdir )
            
            with open( tempdir + "/img.raw", "wb+" ) as fp:
                fp.write( img )
            
            os.system( libdir + 'cwsq.exe %s wsq "img.raw" -raw_in %d,%d,%d,%d' % ( self.r, size[ 0 ], size[ 1 ], 8, res ) )
    
            with open( tempdir + "/img.wsq", "rb" ) as fp:
                data = fp.read()
        
        return data
    
    def decode( self, img ):
        with TemporaryDirectory() as tempdir:
            os.chdir( tempdir )
            
            with open( tempdir + "/img.wsq", "wb+" ) as fp:
                fp.write( img )
            
            os.system( libdir + 'dwsq.exe raw "img.wsq" -raw_out' )
            
            with open( tempdir + "/img.raw", "rb" ) as fp:
                data = fp.read()
            
        return data

try:
    from .version import __version__
except:
    __version__ = "dev"

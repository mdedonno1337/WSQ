#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from MDmisc.TemporaryDirectory import TemporaryDirectory
from MDmisc.imageprocessing import PILToRAW
import os
import platform
import random
import subprocess

from PIL import Image



libdir = os.path.split( os.path.abspath( __file__ ) )[ 0 ] + "/NBIS/"

if platform.system() == "Windows":
    cwsq = libdir + "cwsq.exe"
    dwsq = libdir + "dwsq.exe"

else:
    cwsq = libdir + "cwsq"
    dwsq = libdir + "dwsq"

class WSQ:
    def __init__( self ):
        self.r = "2.25"
    
    def encode( self, img, size = ( 512, 512 ), res = 500 ):
        if isinstance( img, Image.Image ):
            img, size = PILToRAW( img ), img.size
        
        with TemporaryDirectory() as tempdir:
            with open( tempdir + "/img.raw", "wb+" ) as fp:
                fp.write( img )
            
            cmd = cwsq + ' %s wsq img.raw -raw_in %d,%d,%d,%d' % ( self.r, size[0], size[1], 8, res )
            cmd = cmd.split( " " )
            subprocess.Popen( cmd, cwd = tempdir, stdout = subprocess.PIPE, stderr = subprocess.PIPE ).communicate()
            
            with open( tempdir + "/img.wsq", "rb" ) as fp:
                data = fp.read()
        
        return data
    
    def decode( self, img ):
        with TemporaryDirectory() as tempdir:
            with open( tempdir + "/img.wsq", "wb+" ) as fp:
                fp.write( img )
            
            cmd = dwsq + ' raw img.wsq -raw_out'
            cmd = cmd.split( " " )
            subprocess.Popen( cmd, cwd = tempdir, stdout = subprocess.PIPE, stderr = subprocess.PIPE ).communicate()
            
            with open( tempdir + "/img.raw", "rb" ) as fp:
                data = fp.read()
            
        return data

try:
    from .version import __version__
except:
    __version__ = "dev"

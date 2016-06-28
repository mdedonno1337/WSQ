#!/usr/bin/env python
#  *-* coding: cp850 *-*

import os
import random


class wsq:
    def __init__( self, input = None ):
        if input != None:
            self.set_files( input )
        
        self.r = "2.25"
        self.w = None
        self.h = None
        
        self.d = 8
        self.dpi = 500
        
        return
    
    def set_files( self, input ):
        name, ext = os.path.splitext( input )
        
        self.input = input
        self.outdir = os.path.split( os.path.abspath( self.input ) )[0]
        
        if ext == ".raw":
            self.outfile = input.replace( ".raw", ".wsq" )
        elif ext == ".wsq":
            self.outfile = input.replace( ".wsq", ".raw" )
        else:
            print "format error"
            return
        
    def set_size( self, s ):
        w, h = s
        
        self.w = w
        self.h = h
    
    def encodeFromBuffer( self, img ):
        name = "%020d.raw" % random.randint( 0, 10e20 )
        
        self.set_files( name )
        
        with open( self.input, "wb+" ) as fp:
            fp.write( img )
        
        self.encode()
        
        with open( self.outfile, "rb" ) as fp:
            data = fp.read()
        
        os.unlink( self.input )
        os.unlink( self.outfile )
        
        return data

    def decodefromBuffer( self, img ):
        name = "%020d.wsq" % random.randint( 0, 10e20 )
        
        self.set_files( name )
        
        with open( self.input, "wb+" ) as fp:
            fp.write( img )
        
        self.decode()
        
        with open( self.outfile, "rb" ) as fp:
            data = fp.read()
        
        os.unlink( self.input )
        os.unlink( self.outfile )
        
        return data
    
    def encode( self, w = None, h = None ):
        if w != None and h != None:
            self.set_size( ( w, h ) )
            
        if self.w == None or self.h == None:
            print "size not defined"
            return
        
        if not os.path.isfile( self.input ):
            print "input file not found"
            return
        
        os.chdir( self.outdir )
        os.system( 'L:\\python\\src\\lib\\wsq\\cwsq.exe %s wsq "%s" -raw_in %d,%d,%d,%d' % ( self.r, self.input, self.w, self.h, self.d, self.dpi ), 0 )

        return

    def decode( self ):
        if not os.path.isfile( self.input ):
            print "input file not found"
            return
        
        os.chdir( self.outdir )
        os.system( 'L:\\python\\src\\lib\\wsq\\dwsq.exe raw "%s" -raw_out' % self.input, 0 )
        os.unlink( "%s.ncm" % os.path.splitext( self.input )[0] )
        
        return

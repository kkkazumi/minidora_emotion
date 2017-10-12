#import collections
from numpy import *

EPSIRON =      0.0001
ALPHA_THETA = 0.05
ALPHA_W =     0.05
ETA_W =       0.05
ETA_THETA =   0.05

def f( _u ):
    f_u = 1/ (1+exp(-(_u) ) )
    return f_u

def f_dash( _u ):
    f_re = ( _u * (1.0-_u) )
    return f_re
    
class Neural_Network:
    def __init__( self, N_layer, teaching_num ):
        self.R = len( N_layer )
        self.NN_layer = [ N_layer[0],N_layer[1],N_layer[2] ]
        self.P = teaching_num
        self.MAX_N = sum( N_layer )
        self.Teach_i = zeros( (self.P,N_layer[ 0 ]) )
        self.Teach_o = zeros( (self.P,N_layer[self.R-1]) )
        self.Layer_w = zeros( ( (self.R,self.MAX_N,self.MAX_N) ) )
        #self.Layer_1 = zeros( N_layer[0] )
        #self.Layer_2 = zeros( N_layer[1] )
        #self.Layer_3 = zeros( N_layer[2] )
        #self.hoge = [ self.Layer_1,self.Layer_2,self.Layer_3 ]
        self.Layer_theta = zeros( (self.R,self.MAX_N) )

        for k in range( 0,self.R,1 ):
            for j in range( N_layer[k] ):
                for i in range( N_layer[k-1] ):
                    self.Layer_w[k][j][i] = ALPHA_W * random.uniform( -1,1 )
                self.Layer_theta[k][j] = ALPHA_THETA * random.uniform( -1,1 )
        self.Layer_output = zeros( (self.R,self.MAX_N) )
        self.Layer_delta = zeros( (self.R,self.MAX_N) )

    def showdata( self ):
        print self.P
        print self.MAX_N
        #print self.Layer_w
        print self.Layer_theta
        #print self.hoge
        #print self.hoge[0]
        print self.Teach_i
        print self.Teach_o

    def Forward( self,_p ):
        for i in range( self.NN_layer[0] ):
            self.Layer_output[0][i] = self.Teach_i[_p][i]
        for k in range( 1,self.R,1 ):
            for i in range( self.NN_layer[k] ):
                u = 0.0
                for j in range( self.NN_layer[k-1] ):
                    u += self.Layer_w[k][i][j] * self.Layer_output[k-1][j]
                u -= self.Layer_theta[k][i]
                self.Layer_output[k][i] = f( u )

    def Backward( self,_p ):
        for i in range( self.NN_layer[self.R-1] ):
            self.Layer_delta[self.R-1][i] = -( self.Teach_o[_p][i] - self.Layer_output[self.R-1][i] ) * f_dash( self.Layer_output[self.R-1][i] )
        for k in range( self.R-2,0,-1 ):
            for i in range( self.NN_layer[k] ):
                delta = 0.0
                for j in range( self.NN_layer[k-1] ):
                    delta += self.Layer_w[k+1][j][i] * self.Layer_delta[k+1][j]
                self.Layer_delta[k][i] = delta * f_dash( self.Layer_output[k][i] )

    def Learn( self ):
        for k in range( self.R-1,0,-1 ):
            for i in range( self.NN_layer[k] ):
                for j in range( self.NN_layer[k-1] ):
                    self.Layer_w[k][i][j] += -ETA_W * self.Layer_delta[k][i] * self.Layer_output[k-1][j]
                self.Layer_theta[k][i] += ETA_THETA * self.Layer_delta[k][i]

    def Error( self ):
        E = 0.0
        for p in range( self.P ):
            self.Forward( p )
            for i in range( self.NN_layer[self.R-1] ):
                E += ( self.Teach_o[p][i] - self.Layer_output[self.R-1][i] ) * ( self.Teach_o[p][i] - self.Layer_output[self.R-1][i] )
        return E/2

    def before_L( self,writefile ):
        Loop = 0
        E = self.Error()
        while E > EPSIRON:
            Loop = Loop +1
            if Loop%100 == 0:
                print( Loop )
                print( E )
            for p in range( self.P ):
                self.Forward( p )
                self.Backward( p )
                self.Learn()
            E = self.Error()
            if Loop > 500000:
                break
        #self.WriteLearnfile( writefile )

    def input_date( self,teach_i,teach_o ):
        for p in range( self.P ):
            if len( teach_i[p] ) != len( self.Teach_i[p] ):
                print( "Input date are inequality" )
                break
            if len( teach_o[p] ) != len( self.Teach_o[p] ):
                print( "Input date are inequality" )
                break
            for i in range( len(teach_i[p]) ):
                self.Teach_i[p][i] = teach_i[p][i]
            for i in range( len(teach_o[p]) ):
                self.Teach_o[p][i] = teach_o[p][i]

    def testforward( self,test ):
        #if len( test ) != len( self.NN_layer[0] ):
         #   print "test date is bad argument"
        u = 0.0
        ansewr = zeros( self.NN_layer[self.R-1] )
        for i in range( self.NN_layer[0] ):
            self.Layer_output[0][i] = test[i]
        for k in range( self.R,1,1 ):
            for i in range( self.NN_layer[k] ):
                u = 0.0
                for j in range( self.NN_layer[k-1] ):
                    u += self.Layer_w[k][i][j] * self.Layer_output[k-1][j]
                u -= self.Layer_theta[k][i]
                self.Layer_output[k][i] = f( u )
        print self.Layer_output



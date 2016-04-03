#-*-encoding:utf-8-*-
'''
Created on 2016-3-24

@author: ThinkPad
'''

class FileIdentify(object):
    '''
    define file's name in IC card
    ONE PAY : PSE  = 1PAY.SYS.DDF01   for PBOC ECC
    TWO PAY : PPSE = 2PAY.SYS.DDF01   for QPBOC
    DEBIT/CREBIT AID  eg: A000000333010101,A000000333010102
    '''
    PSE  = [0x31,0x50,0x41,0x59,0x2E,0x53,0x59,0x53,0x2E,0x44,0x44,0x46,0x30,0x31]
    PPSE = [0x32,0x50,0x41,0x59,0x2E,0x53,0x59,0x53,0x2E,0x44,0x44,0x46,0x30,0x31]

    def __init__(self,params):
        '''
        Constructor
        '''
        
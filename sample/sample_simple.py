# coding: utf-8
import pyarrot

def sampleFunction():
    # sample function.
    print("sample function.")

if __name__=='__main__':
    # make PyArrot object.
    it = pyarrot.init(["description"])
    
    # add a target function to PyArrot.
    it.addFunction('s', 'Exec sampleFunction.', sampleFunction)
    
    # start PyArrot
    it.start()
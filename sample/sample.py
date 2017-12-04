# coding: utf-8
import pyarrot

def sampleFunction():
    print("sample function.")

if __name__=='__main__':
    # make PyArrot object.
    it = pyarrot.init(["description"])
    
    # add a target function to PyArrot.
    it.addFunction('s', 'Exec sampleFunction.', sampleFunction)
    
    # start PyArrot
    # if execute this script with no option,
    #    PyArrot work as Interactive mode.
    # if execute with batch option(-mode=batch -command=s),
    #    PyArrot work as Batch mode,
    #    and you need to set the target function( -command=s).
    it.start()
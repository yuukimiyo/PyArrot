# coding: utf-8
import pyarrot

class sampleClass():
    def __init__(self, it):
        self.it = it
    
    def sampleFunction01(self):
        # sample function01.
        print("sample function 01.")
    
    def sampleFunction02(self):
        # sample function02.
        print("sample function 02 - input value.")
        
        inputed_value = self.it.inputValue("Please input value : ", "default-value")
        print("You inputed : %s" % inputed_value)
        
    def sampleFunction03(self):
        # sample function03.
        print("sample function 03 - input date.")
        
        inputed_date = self.it.inputDate("Please input date[YYYYMMDD] : ", "20170101", "s01date", "%Y%m%d")
        print("You inputed : %s" % inputed_date)

    def sampleFunction04(self):
        # sample function04.
        print("sample function 04 - select file.")
        
        inputed_file = self.it.selectFile("Please input a file number[default=0] : ", "sample_dir", "0")
        print("You selected : %s" % inputed_file)
        
if __name__=='__main__':
    # make PyArrot object.
    it = pyarrot.init(["description",
                       "you can write multiline."])
    
    sampleClassObject = sampleClass(it)
    
    # add a target function to PyArrot.
    it.addFunction('s1', 'Run sampleFunction01.', sampleClassObject.sampleFunction01)
    it.addFunction('s2', 'Run sampleFunction02 - Input value.', sampleClassObject.sampleFunction02)
    it.addFunction('s3', 'Run sampleFunction03 - Input Date.', sampleClassObject.sampleFunction03)
    it.addFunction('s4', 'Run sampleFunction04 - Select File.', sampleClassObject.sampleFunction04)
    
    # start PyArrot
    it.start()
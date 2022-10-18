import os

#create a TXT test to a location
fn = r'C:\Users\PTE8BLJ\Desktop\AzureTest\language.txt'
try:
    fn = open(fn,'r')
except:
# if file does not exist, create it
    fn = open(fn,'w') 

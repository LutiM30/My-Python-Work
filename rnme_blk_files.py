#imports os version and info to python
import os

#defining main function
def main():
    ## setting up i to zero
    i=0
    ## PUTTING PATH IN WHICH I WANT TO CHANGE THE NAMES
    path = 'C:/Mitul/Practice/python/FCCPythonprjcts/trainfolder/'

    for filename in os.listdir(path):
        
        ##Creating Destination to setup the name with value of i and extension if i want to change it too
        my_destination = 'train'+str(i)+'.txt'

        ##GETTING SOURCE FILE INFO AND SETTING IT TO MY_SOURCE
        my_source = path + filename

        ## SETIING UP DESTINATION IN SAME PATH AS SOURCE FILE
        my_destination = path + my_destination

        ##USING OS.RENAME FUNCTION TO CHANGE THE NAME OF SOURCE FILE TO NEW FILE AS my_destination
        os.rename(my_source, my_destination) 

        ## i=I+1
        i+=1

# while True:
#     getting_path = input("enter Path to Change The All Files' name")

## RUNNING FUNCTION IMMEDIATELY AS THE PYTHON PROGRAM IS BEING RUN
if __name__ == '__main__':
    main()

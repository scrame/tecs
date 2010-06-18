from os import path,mkdir
class Parser:
    def __init__(self,input_file):
        print("initializing parser")
        print("loading input")
        input = self.__parse_file(input_file)
        print("creating output")
        output = self.__create_output(input_file)
        

    def __parse_file(self, input_file):
        print("opening: " + str(input_file))
        f = open(input_file)
        return f.readlines()

    #returns a writeable output handle to "build"
    #todo: y'know.
    def __create_output(self, input_file_name):
        build = "build"
        base = path.splitext(path.basename(input_file_name))[0]
        print "base: " + base
        if(not(path.exists(build))):
            mkdir(build)
        return open(build+"/"+base+".hack","w")

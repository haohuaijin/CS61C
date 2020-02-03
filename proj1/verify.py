import sys
import os

if(len(sys.argv)!=3):
    print("Incorrect number of arguments, use python verify.py <File 1> <File 2>")
    sys.exit()

def checkequal(file1, file2):
    with open(file1) as f:
        content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip().split(" ") for x in content]
    reference_content = []
# flattening the 2d array
    for each_row in content:
        reference_content.extend(each_row)

    with open(file2) as f:
        content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip().split(" ") for x in content]
    student_content = []
# flattening the 2d array
    for each_row in content:
        student_content.extend(each_row)

    if len(student_content)!=len(reference_content):
        print("Total number of pixels is incorrect! Your output has " + str(len(student_content)) + " pixels, but reference has " + str(len(reference_content)) + " pixels")
        sys.exit()
    else:
        number_of_inac = 0
        for i in range(len(student_content)):
            if int(student_content[i])!= int(reference_content[i]):
                number_of_inac += 1
        return number_of_inac, len(student_content)

def ppmequal(file1, file2):
    f, g = open(file1, "rb"), open(file2, "rb")
    headerf, headerg = f.readline(), g.readline()
    if(headerf != headerg):
        print("Error with header on ppm file " + file1)
        sys.exit()
    linecount, linelength = int(headerf.decode("utf-8").split(" ")[1]), int(headerf.decode("utf-8").split(" ")[2])
    a,b = 0,0
    for i in range(linecount):
        linef, lineg = f.read(3*linelength), g.read(3*linelength)
        if(len(linef) != 3*linelength or len(lineg) != 3*linelength):
            print("Error with length " + file1)
            sys.exit()
        for j in range(linelength):
            if(linef[3*j:3*j+2] != lineg[3*j:3*j+2]):
                a+=1
            b+=1
    return a,b


if(sys.argv[1][-4:]==".txt"):
    a,b = checkequal(sys.argv[1], sys.argv[2])
    print("You have " + str(a) +" inaccurate pixels" +
    ", which is a " + str((1-(a/b))*100)+"\% accuracy.")
elif(sys.argv[1][-4:] == ".ppm"):
    a,b = ppmequal(sys.argv[1], sys.argv[2])
    print("You have " + str(a) +" inaccurate pixels" +
    ", which is a " + str((1-(a/b))*100)+"\% accuracy.")
else:
    k = len(os.listdir(sys.argv[1]))
    a,b = 0,0
    for i in range(k):
        num = str(i)
        while(len(num)<5):
            num = "0"+num
        file1 = sys.argv[1]+"/frame" + num + ".ppm"
        file2 = sys.argv[2]+"/frame" + num + ".ppm"
        c,d = ppmequal(file1, file2)
        a+=c
        b+=d
    print("You have " + str(a) +" inaccurate pixels" + ", which is a " + str((1-(a/b))*100)+"\% accuracy.")

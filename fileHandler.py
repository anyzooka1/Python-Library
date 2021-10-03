def readFile(fName):
    with open(fName, "r") as f:
        return f.read()

def writeFile(fName, contents):
    with open(fName, "w+") as f:
        f.write(contents)

def appendFile(fName, contents):
    with open(fName, "a+") as f:
        f.write(contents)

def deleteFile(fName):
    import os
    try:
        os.remove(fName)
    except:
        pass

def main():
    print("\n--------------- FILE HANDLING TEST ---------------\n")
    deleteFile("test.txt")
    appendFile("test.txt", "Contents")
    print(readFile("test.txt"))
    writeFile("test.txt", "New Contents")
    print(readFile("test.txt"))

if __name__ == "__main__":
    main()
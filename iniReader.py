class iniReader:
    fName = ""
    vals = {}
    
    def __init__(self, fName):
        self.fName = fName

        self._loadIntoDict()
        

    def _loadIntoDict(self):
        try:
            wholeFile = self.readFile(self.fName).split("\n")
        except:
            return None

        for line in wholeFile:
            if line.strip() != "":
                try:
                    self.vals[line.split("=")[0].strip()] = line.split("=")[1].strip()
                except:
                    x = 1

    def get(self, index):
        try:
            return self.vals[index]
        except:
            return None

    def set(self, index, value):
        self.vals[index] = value

        self.save()

    def save(self):
        f = open(self.fName, "w")
        for key in self.vals:
            f.write(f"{key}={self.vals[key]}\n")
        f.close()


    def readFile(self, fName):
        with open(fName, "r") as f:
            return f.read()

def main():
    print("\n--------------- INI READER TEST ---------------\n")
    x = iniReader(".ini")
    x.set("Date created", "[Imagine time here]")
    x.set("Score", "2147483647")

    print(x.get("Score"))

if __name__ == "__main__":
    main()

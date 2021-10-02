import msvcrt as m

def optionSelector(optionList, start=">>>", end="<<<"):
    # optionlist should be an array of string, which will be returned
    # when the user has selected their option
    index = 0
    while True:

        for i in range(len(optionList)):
            if i == index:
                print(start + optionList[i] + end)
            else:
                print(optionList[i])

        
        inp = m.getch()

        if inp == b'P':
            index += 1
            if index >= len(optionList):
                index = 0

        if inp == b'H':
            index -= 1
            if index < 0:
                index = len(optionList) - 1

        if inp == b'\r':
            for i in optionList:
                print ("\033[A                             \033[A") 
            return optionList[index]

        for i in optionList:
            print ("\033[A                             \033[A") 

def main():
    print(f'Option: \'{optionSelector(["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"], start=">", end="<")}\' selected')

if __name__ == "__main__":
    main()
#!/usr/bin/env python3.10

# Import re for regular expressions
import re

# These could have been whatever input from the user to lower or UPPER, but we already imported re, so let us use it.
reQuit = re.compile(r"^[qQ][uU][iI][tT]")
reHelp = re.compile(r"^[hH][eE][lL][pP]")

# Banner on startup.
print("Pyculator, a Linux permissions calculator.\r\nType quit at any prompt to close Pyculator.")

# Method for "help" when calling help from the pycin method.
def help(strKind):
    if strKind == "numeric":
        print("This number should be THREE numbers long inclusively between 000 and 777. Where the permissions are respectively for the owner, group, and everyone.\r\nObserve the following 7, read,write,execute , rwx\r\n6, read,write , rw-\r\n5, read,execute, r-x\r\n4, read , r--\r\n3, write,execute , -wx\r\n2, write , -w-\r\n1, execute, --x\r\n0, none , ---")
    elif strKind == "symbolic":
        print("This is the NINE space symbolic representation is three groups of three characters rwx respectively and any of those may be represented with a \"-\". For example r-x. If there is are 10 symbols, this usually has a leading \"d\" or \"-\" or trailing \"\@\".")

# Method for input from user.
def pycin(strValue):
    # Declarations and initializations for this method.
    arrayNext = ["a","s","q"]
    arrayPerm = ["---","--x","-w-","-wx","r--","r-x","rw-","rwx"]
    strTest = ""
    strNext = ""

    # User input will be challenged against numbers.
    if strValue == "1":
        strPattern = re.compile(r"^[0-7]{3,3}$")
        while not re.fullmatch(strPattern, strTest):
            strTest = input("\r\nEnter your THREE number value range of 000 to 777: ")

            # Beginning of numeric challenge.
            if re.fullmatch(strPattern, strTest):
                strPerm = arrayPerm[int(strTest[0])] + arrayPerm[int(strTest[1])] + arrayPerm[int(strTest[2])]
                print("Your permissions are " + strPerm)

                # The while loop is redundant and can actually be a method.
                while strNext not in arrayNext:
                    strNext = input("(a)nother, (s)tart over, (q)uit: ")
                    if strNext == "a":
                        strTest = ""
                        pycin(strTest)
                    elif strNext == "s":
                        pyculator()
                    elif strNext == "q":
                        break
                    elif re.fullmatch(reHelp, strNext):
                        help("numeric")
                    elif re.fullmatch(reQuit, strNext):
                        exit()

            # Call for help.
            elif re.fullmatch(reHelp, strTest):
                help("numeric")

            # Exit.
            elif re.fullmatch(reQuit, strTest):
                exit()
            else:
                print("The entered value MUST be equal to or between 000 and 777. Type \"help\" for more informaiton.")

    # User input will be challenged against sybmols.
    elif strValue == "2":
        strPattern = re.compile(r"^((rwx)|(rw-)|(r-x)|(r--)|(-wx)|(-w-)|(rw-)|(--x)|(---)).{6}?")
        while not re.fullmatch(strPattern, strTest):
            strTest = input("\r\nEnter the last NINE of the symbolic permission: ")

            # We must use try-except to elegantly handle errors when attempting to challenge incorrect values that do not match the array while keeping the application from crashing.
            try:
                # Beginning of symbolic challnege.
                if re.fullmatch(strPattern, strTest):
                    strGroup1 = strTest[0:3] # Split first three of strTest.
                    strGroup2 = strTest[3:6] # Split next three of strTest.
                    strGroup3 = strTest[6:9] # Split last three of strTest.
                    print(str(arrayPerm.index(strGroup1)) + str(arrayPerm.index(strGroup2)) + str(arrayPerm.index(strGroup3)))

                    # The while loop is redundant and can actually be a method.
                    while strNext not in arrayNext:
                        strNext = input("(a)nother, (s)tart over, (q)uit: ")
                        if strNext == "a":
                            strTest = ""
                            pycin(strTest)
                        elif strNext == "s":
                            pyculator()
                        elif strNext == "q":
                            break
                        elif re.fullmatch(reHelp, strNext):
                            help("symbolic")
                        elif re.fullmatch(reQuit, strNext):
                            exit()

                # Call for help.
                elif re.fullmatch(reHelp, strTest):
                    help("symbolic")

                # Exit.
                elif re.fullmatch(reQuit, strTest):
                    exit()
                else:
                    print("The entered value MUST be the last NINE symbols. Try again: ")
            except ValueError:
                print("Value is incorrect")
                pycin(strValue)

# Method asking for what the user wants to do.
def pyculator():
    # Declarations and initializations for this method.
    strPyc = "0"
    arrayValidate = ["1","2"]

    while strPyc not in arrayValidate:
        strPyc = input("\r\nWhat needs to be pyculated?\r\n1. Numeric (777) to symbolic (rwxrwxrwx)\r\n2.Symbolic (rwxrwxrwx) to Numeric (777)\r\nAnswer: ")
        if strPyc == "1":
            pycin(strPyc)
        elif strPyc == "2":
            pycin(strPyc)
        elif re.fullmatch(reQuit, strPyc):
            exit()

# Beginning of Pyculator
pyculator()

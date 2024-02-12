####################################################################
"""
Developer: Julian Cotto
Date: 12/10/2023
File Name: program14.py
Description: This file contains the main function of program14
"""
####################################################################
from program14Functions import getProgPurpose
from program14Functions import getMain
from program14Functions import outro


def main():
    getProgPurpose()
    print('\n')
    getMain()
    print('\n')
    outro()

    return 0


if __name__ == "__main__":
    main()
else:
    pass

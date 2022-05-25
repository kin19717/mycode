#!/usr/bin/env python3
import shutil
import os

def main():
    #force our Python program to 'start' in the home user directory
    os.chdir("/home/student/mycode/")
    #copy the file at the path source to the folder at the path destination
    #If destination is a filename, it will be used as the new name of the copied file
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
    #copy an entire folder and every folder and file contained in it
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()


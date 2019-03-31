#!/usr/bin/python3
# Title: ZipCrack
# Description: Dictionary attack on password protected Zip files
# Author: Ross White
# Written: 3/30/2019

import argparse
import zipfile

def get_wordlist(wordlist):
    fobj = open(wordlist, 'r')
    passlist = fobj.readlines()
    fobj.close()
    # Remove trailing new line characters
    i = 0
    while i < len(passlist):
        passlist[i] = passlist[i].rstrip('\n')
        i += 1
    return passlist

def crack_attempt(zfile, passlist, extractpath):
    try:
        zfile.extractall(path=extractpath)      # Try to extract without password
    except RuntimeError:
        print('Password required')
        print('Wait while I try your password list...')
        for word in passlist:   # Iterate through list attempting to extract
            try:
                zfile.extractall(path=extractpath, pwd=bytes(word, 'utf-8'))
                print('Password found: ' + word)    # Print correct password
            except:
                continue
                print('Incorrect password attempt')
    zfile.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("zipfile", help="zip file name, include file path if not in same directory",
                    type=str)
    parser.add_argument("wordlist", help="word list file name, include file path if not in same directory",
                    type=str)
    parser.add_argument("extractpath", help="path for file extraction", type=str)
    args = parser.parse_args()
    
    passlist = get_wordlist(args.wordlist)
    zfile = zipfile.ZipFile(args.zipfile)
    crack_attempt(zfile, passlist, args.extractpath)
    

if __name__ == '__main__':
    main()

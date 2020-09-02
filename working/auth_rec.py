#! /usr/bin/env python

#MIT License

import argparse

def run(args):


def main():
    parser = argparse.ArgumentParser(description="Examine the stylistic similarity of a sample file with a text corpus.")
    parser.add_argument("-corpus",help="Folder of sample texts by suspected author(s).\n If multiple authors include a subfolder for each author.",dest="corpus",type=str,required=True)
    parser.add_argument("-in",help="File(s) being analyzed to determine similarity to corpus.",dest="input",type=str,required=True)
    parser.add_argument("-out",help="Specify what file you want the result of the analysis to be written to. Default=analysis-result",dest="output",type=str,default="analysis-result")

if __name__=="__main__":
    main()
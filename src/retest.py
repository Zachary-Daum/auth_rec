import argparse
import math
import pandas as pd
from os import listdir
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

def run(args):
    corpus_folder = listdir(args.corpus)
    analysis_case = listdir(args.input)

    ###Functions###
    def get_features(auth, phase):
        if phase == args.corpus:
            auth_articles = listdir(phase+'/'+auth)
        else:
            auth_articles = analysis_case
        #assemble author corpus
        auth_corpus = ''
        for article in auth_articles:
            if phase == args.corpus:
                with open(phase+'/'+auth+'/'+article) as active_file:
                    auth_corpus += active_file.read().lower()
            else:
                with open(phase+'/'+article) as active_file:
                    auth_corpus += active_file.read().lower()
        #tokenize corpus
        tokenized = word_tokenize(auth_corpus)
        corpus_len = len(tokenized)
        corpus_dist = list(FreqDist(tokenized).most_common(35))
        corpus_prob = {}
        for feature in corpus_dist:
            corpus_prob.update({feature[0]:feature[1]/corpus_len})
        return corpus_prob 

    def add_df(auth, feat):
        for feature in feat:
            freq_df.at[auth, feature] = feat[feature]

    def distance_list(auth):
        working_list = []
        for col in freq_df.loc[auth]:
            working_list.append(col)
        return working_list

    freq_df = pd.DataFrame()
    ###for training data###
    for auth in corpus_folder:
        feat = get_features(auth, args.corpus)
        #add to df
        add_df(auth, feat)

    ###for file(s) being analyzed###
    for test in analysis_case:
        feat = get_features(test, args.input)
        #add to df
        add_df(test,feat)
    freq_df = freq_df.fillna(0)

    ###Calculate distance###
    distance_dict = {}
    for author in corpus_folder:
        distance_dict.update({author:distance_list(author)})
    proximity_dict = {}
    for test in analysis_case:
        test_point = distance_list(test)
        eDist = {}
        for author in corpus_folder:
            eDist.update({author:math.dist(test_point, distance_dict[author])})
        proximity_dict.update({test:eDist})

    ###Output File###
    output = ''
    for analyzed_file in proximity_dict:
        output += 'For file' + analyzed_file + '\n'
        for score in proximity_dict[analyzed_file]:
            output += score + ' - score of:'+ str(proximity_dict[analyzed_file][score])+ '\n'
        output += '=====================\n'
    output += '\nLower score is better'

    result_file = open(args.output, "w")
    result_file.write(output)
    result_file.close()

def main():
    parser = argparse.ArgumentParser(description="Examine the stylistic similarity of a sample file with a text corpus.")
    parser.add_argument("-corpus",help="Folder of sample texts by suspected author(s).\n Have a subfolder named for every author.",dest="corpus",type=str,required=True)
    parser.add_argument("-in",help="Folder of text(s) being analyzed to determine similarity to corpus.",dest="input",type=str,required=True)
    parser.add_argument("-out",help="Specify what file you want the result of the analysis to be written to. \n This will erase the contents of the file. Default=analysis-result.txt",dest="output",type=str,default="analysis-result.txt")
    parser.set_defaults(func=run)
    args=parser.parse_args()
    args.func(args)

if __name__=="__main__":
    main()
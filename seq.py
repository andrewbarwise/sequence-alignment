from Bio import Align
import pandas as pd
import os
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
from matplotlib import pyplot as plt

# this function computes a pairwise alignment score
def alignment(cdr3_1, cdr3_2):
    aligner = Align.PairwiseAligner()
    score = aligner.score(cdr3_1,cdr3_2)
    denom = max(len(cdr3_1), len(cdr3_2))
    adjustedScore = score / denom
    return adjustedScore

# creates a data frame to hold the observations 
def createDF(inputFile):
    df = pd.read_csv('all.tsv', header=None, delimiter=r"\s+")
    lst1 = df.iloc[1:100, 0].tolist()
    lst2 = df.iloc[1:100, 3].tolist()

    lst = pd.DataFrame(
        {'CDR3':lst1,
        'patient':lst2}
    )
    # create a new column and remove first 4 characters from CDR3 string for computation
    lst['CDR3_Alt'] = lst['CDR3'].str[4:]
    return lst

# create a similarity matrix and fill with the pairwise scores
def simMat(inputFile):
    # create empty similarity matrix
    similarity_df = pd.DataFrame()
    
    # call createDF()
    lst = createDF(inputFile)
    
    # for each line compare the CDR3
    for index_1, row_1 in lst.iterrows():
        for index_2, row_2 in lst.iterrows():
            similarity_score = alignment(lst.at[index_1,'CDR3_Alt'], lst.at[index_2,'CDR3_Alt'])
            similarity_df.loc[lst.at[index_1,'CDR3'],lst.at[index_2,'CDR3']] = similarity_score

    print(similarity_df)
    linked = linkage(similarity_df, 'ward')
    return linked

# plot a dendogram using the similarity matrix
def plotDendo(inputFile):
    linked = simMat(inputFile)
    plt.figure(figsize=(15, 12))
    plt.title("Sequence Alignment Dendogram")
    dendrogram(
                linked,
                truncate_mode= 'lastp',
                p=20,
                orientation='right',
                #labels=True,
                distance_sort='descending',
                show_leaf_counts=False,
                
            )
    plt.show()

# compute similarity scores
def simScore(inputFile):
    # call createDF()
    lst = createDF(inputFile)
    for index_1, row_1 in lst.iterrows():
        for index_2, row_2 in lst.iterrows():
            simScore = alignment(lst.at[index_1,'CDR3_Alt'], lst.at[index_2,'CDR3_Alt'])
            if simScore >= 0.83:
                print(simScore)


def main(inputFile):
    createDF(inputFile)
    simMat(inputFile)
    plotDendo(inputFile)
    #simScore(inputFile)
    input("Press enter to exit ;)")
    
if __name__ == '__main__':   
    main('all.tsv')

# need to do : i) label dendogram ii) implement a cutoff score for dendogram iii) labels for simScore()
# iv) why is the output different for simScore() and simMat()?
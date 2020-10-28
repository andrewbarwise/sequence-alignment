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
    lst1 = df.iloc[24026:28727, 0].tolist()
    lst2 = df.iloc[24026:28727, 3].tolist()

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
    # call createDF()
    lst = createDF(inputFile)
    
    linked = simMat(inputFile)
    
    labels = lst['CDR3'].tolist()
    p = len(labels)
    
    plt.figure(figsize=(30, 15))

    R = dendrogram(
                linked,
                truncate_mode= 'lastp',
                p=p,
                no_plot=True,   
            )
    # create a label dictionary
    temp ={R['leaves'][ii]: labels[ii] for ii in range(len(R['leaves']))}
    def llf(xx):
        return "{}".format(temp[xx])
    
    dendrogram(
        linked,
        truncate_mode='lastp',
        p=p,
        leaf_label_func=llf,
        leaf_rotation= 90.,
        leaf_font_size=16.,
        show_contracted=True,
    )
    plt.tight_layout()
    plt.savefig('fig1.png')

def main(inputFile):
    createDF(inputFile)
    plotDendo(inputFile)
    input("Press enter to exit ;)")
    
if __name__ == '__main__':   
    main('all.tsv')

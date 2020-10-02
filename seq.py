# Import libraries and modules
from Bio import Align
import pandas as pd

# create a  pairwiseAligner object
aligner = Align.PairwiseAligner()

# set alignment parameters
aligner.match_score = 1.0
aligner.mismatch_score = -2.0
aligner.open_gap_score = -2.5
aligner.gap_score = -2.0

# read in the data
df = pd.read_csv('all.tsv', header=None, delimiter=r"\s+")
lst = df.iloc[1:, 0].tolist()


ii = 0
while ii+1 < len(lst):
    X = lst[ii]
    Y = lst[ii + 1]
    
    #obtain the score
    score = aligner.score(X,Y)
    
    # obtain the the variable of greatest length
    denom = max(len(X),len(Y))
    
    # obtain a % of similarity
    adjustedScore = score / denom 

    #alignments = aligner.align(X,Y)

    if adjustedScore >= 0.99:
        print(X," : ", Y, '=',adjustedScore)
        print(len(lst))
    ii = ii + 1

# need to create functions and a main()
"""# Import libraries and modules
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
    ii = ii + 1"""

#######################################################
from Bio import Align
import pandas as pd

def param(lst, xx, yy, zz, qq, cc):
    # create the aligner object
    aligner = Align.PairwiseAligner()

    aligner.match_score = xx
    aligner.mismatch_score = yy
    aligner.open_gap_score = zz
    aligner.gap_score = qq

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
        newLst = []
        if adjustedScore >= cc:
            newLst.append(adjustedScore)

        ii = ii + 1
    return newLst

def main(inputFile):
    # read in the data
    df = pd.read_csv(inputFile, header=None, delimiter=r"\s+")
    lst = df.iloc[1:, 0].tolist()
    
    xx = float(input("Please enter the score for a matching character: "))
    yy = float(input("Please enter the penalty for mismatched characters: ")) * - 1
    zz = float(input("Please enter the penalty for the opening of a gap: ")) * - 1
    qq = float(input("Please enter the penalty for the continuation of a gap: ")) * - 1

    cc = float(input("Please input the cut off percentage: "))

    output = param(lst, xx, yy, zz, qq, cc)
    print(output)

if __name__ == '__main__':
    main('all.tsv')


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

        
        if adjustedScore >= cc:
            print(X, ':', Y, '=', adjustedScore)

        ii = ii + 1
    
        

def main(inputFile):
    # read in the data
    df = pd.read_csv(inputFile, header=None, delimiter=r"\s+")
    lst = df.iloc[1:, 0].tolist()
    
    
    xx = float(input("Please enter the score for a matching character: "))
    yy = float(input("Please enter the penalty for mismatched characters: ")) * - 1
    zz = float(input("Please enter the penalty for the opening of a gap: ")) * - 1
    qq = float(input("Please enter the penalty for the continuation of a gap: ")) * - 1

    cc = float(input("Please input the cut off percentage: "))

    param(lst, xx, yy, zz, qq, cc)

    input("Press enter to exit ;)")
    
if __name__ == '__main__':
    main('all.tsv')


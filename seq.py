from Bio import Align
import pandas as pd

def param(lst, xx, yy, zz, qq, cc):
    # create the aligner object
    aligner = Align.PairwiseAligner()

    aligner.match_score = xx
    aligner.mismatch_score = yy
    aligner.open_gap_score = zz
    aligner.gap_score = qq

def alignment(cdr3_1, cdr3_2):
    aligner = Align.PairwiseAligner()
    score = aligner.score(cdr3_1,cdr3_2)
    denom = max(len(cdr3_1), len(cdr3_2))
    adjustedScore = score / denom
    return adjustedScore
        
        

def main(inputFile):
    # read in the data
    df = pd.read_csv(inputFile, header=None, delimiter=r"\s+")
    lst1 = df.iloc[1:, 0].tolist()
    lst2 = df.iloc[1:, 3].tolist()
    
    # create a dataframe
    lst = pd.DataFrame(
        {'CDR3':lst1,
        'patient':lst2}
    )

    xx = float(input("Please enter the score for a matching character: "))
    yy = float(input("Please enter the penalty for mismatched characters: ")) * - 1
    zz = float(input("Please enter the penalty for the opening of a gap: ")) * - 1
    qq = float(input("Please enter the penalty for the continuation of a gap: ")) * - 1

    cc = float(input("Please input the cut off percentage: "))

    param(lst, xx, yy, zz, qq, cc)
    

    input("Press enter to exit ;)")
    
if __name__ == '__main__':
    main('all.tsv')


# Enter your code here. Read input from STDIN. Print output to STDOUT
#import numpy as np
#from scipy.stats import pearsonr

scores = """
Physics Scores  15  12  8   8   7   7   7   6   5   3
History Scores  10  25  17  11  13  17  20  13  9   15
"""


def get_data(scores):
    """
    Returns data in array format.
    """
    data = {}
    for line in scores.split("\n")[1:-1]:
        key = ""
        for item in line.split(" "):
            item = item.strip()
            if not(item.isdigit()):
                key += item
            else:
                data.setdefault(key, [])
                data[key].append(int(item))
    return data


def main():
    """
    Run core functionality.
    """
    data = get_data(scores)

    hist_arr = np.array(data["HistoryScores"])
    phys_arr = np.array(data["PhysicsScores"])

    corr, p_val = pearsonr(hist_arr, phys_arr)

    print(round(corr, 3))

if __name__ == '__main__':
    main()

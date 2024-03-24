import re

def solution(S):
    #first separate all by finding the csv common separator for each row: \n
    rows = re.split(r'[\n]', S)
    headers = rows[0]
    cleancsv = []
    # check all but first row if they match with "NULL", because its case sensitive
    for row in rows[1:]:
        if re.search(r'\W(NULL)\b', str(row)) == None:
            cleancsv.append(row)

    # when all strings are checked for NULL then join them with the same separator: \n
    return headers +'\n'+ '\n'.join(cleancsv)

S = "header,header\nANNUL,ANNULLED\nnull,NILL\nNULL,NULL\nANNUL,ANNULLED\nANNUL,ANNULLED\nmoop,NULL"
print(solution(S))
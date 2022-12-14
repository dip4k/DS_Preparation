from collections import defaultdict


def findAnagrams(inputString: str, requiredChars: str):
    hashMapDict, res, reqCharLength, inputStrLength = defaultdict(int), [], len(requiredChars), len(inputString)
    if reqCharLength > inputStrLength: return []

    # build hashmap
    for ch in requiredChars: hashMapDict[ch] += 1

    # initial full pass over the window
    for i in range(reqCharLength-1):
        if inputString[i] in hashMapDict: hashMapDict[inputString[i]] -= 1
        
    # slide the window with stride 1
    for i in range(-1, inputStrLength-reqCharLength+1):
        if i > -1 and inputString[i] in hashMapDict:
            hashMapDict[inputString[i]] += 1
        if i+reqCharLength < inputStrLength and inputString[i+reqCharLength] in hashMapDict: 
            hashMapDict[inputString[i+reqCharLength]] -= 1
            
        # check whether we encountered an anagram
        if all(v == 0 for v in hashMapDict.values()): 
            res.append(i+1)
            
    return res

print(findAnagrams("cbaebabacd","abc"))
# These are for linking new schemas to the general adapters\
# Given two entities if thier attributes are similar, the entities should be too.
# What is similar?
from nltk.corpus import wordnet
import re
import nltk
from nested_lookup import nested_lookup
import operator
nltk.download('wordnet')

def getSynonyms(word):
    word_synonyms = []
    for synset in wordnet.synsets(word):
        for lemma in synset.lemma_names():
            word_synonyms.append(lemma)
    return word_synonyms

def getSynofls(ls):
    lsx=[]
    for x in ls:
        lsx.append(getSynonyms(x))
    return [item for sublist in lsx for item in sublist]

def similarity(biggerInt, string_match, semantic_match):
    if string_match == biggerInt:
        return 1
    else:
        return (string_match/biggerInt + semantic_match/biggerInt)/2

def PatternMatching(classA_ls, classB_ls):
    similarity_ls = []
    for classA in classA_ls:
        classA1 = classA.__annotations__
        sim_scores = {}
        for classB in classB_ls:
            classB1 = classB.__annotations__
            string_match = 0
            semantic_match = 0
            found_semantic_matches = []
            count1 = len(classA1)
            count2 = len(classB1)
            if count1 > count2:
                count = count1
            else:
                count = count2
            for k1,v1 in classA1.items():
                synonym1 = getSynonyms(k1)
                for k2,v2 in classB1.items():
                    if k1==k2: string_match+=1
                    synonym2 = getSynonyms(k2)
                    for syn in synonym1:
                        if syn in synonym2 and syn not in getSynofls(found_semantic_matches) and syn not in found_semantic_matches: 
                            semantic_match+=1
                            found_semantic_matches.append(k1)
            sim = similarity(count, string_match, semantic_match)
            sim_score = {type(classB).__name__: sim}
            sim_scores.update(sim_score)
            sim_scores_sorted = dict(sorted(sim_scores.items(), key=operator.itemgetter(1),reverse=True))
        similarity_ls.append({type(classA).__name__: sim_scores_sorted})
    return similarity_ls

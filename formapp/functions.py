################################### removing punctuation
def remove_punc(AI_tokens):
    import re

    punctuation = re.compile(r'[-.?!,;:()/|0-9]')

    post_punctuation = []
    for words in AI_tokens:
        word = punctuation.sub("", words)
        if len(word) > 0:
            post_punctuation.append(word)
    return post_punctuation


########################################
###################################### word distribution

def word_freq_distribution(AI_tokens):
    from nltk.probability import FreqDist
    fdist = FreqDist()
    fdist_list = []
    for word in AI_tokens:
        fdist[word.lower()] += 1  ###############to convert all to lower case, thus avoids double count and calculates the distrubution
    for word in fdist:
        # print(word,fdist[word])
        fdist_list.append(word)
        fdist_list.append(fdist[word])
    return fdist, fdist_list


#######################################

##################################################     Remove stopwords
def remove_SWords(AI_tokens):
    from nltk.corpus import stopwords
    post_Swords = []
    for words in AI_tokens:
        if words in post_Swords:
            continue
        elif (words.lower() in stopwords.words('english')):
            continue
        else:
            post_Swords.append(words)
    return post_Swords


################################################## compare with Job

def list_compare(Job, Resume):
    JobResumeCompareMatch = []
    JobResumeCompareMiss = []
    for words in Resume:
        if ((words in Job) and isinstance(words, int) == False):
            JobResumeCompareMatch.append(words)
        else:
            JobResumeCompareMiss.append(words)

    return JobResumeCompareMatch

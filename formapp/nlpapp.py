# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 20:57:53 2022

@author: simon
"""
from .functions import *

def NatLang(Jobx, Resume):
    #import numpy as np
    # import nltk
    #nltk.download()
    from nltk.tokenize import word_tokenize

    Job_token = word_tokenize(Jobx)
    Resume_token = word_tokenize(Resume)
    # print(len(Resume_token))

    Job_noPunc = remove_punc(Job_token)
    Resume_noPunc = remove_punc(Resume_token)
    # print(len(Resume_noPunc))

    Job_word = remove_SWords(Job_noPunc)
    Resume_word = remove_SWords(Resume_noPunc)

    # print(len(Resume_word))

    Job_word_dist, Job_word_dist_list = word_freq_distribution(Job_token)

    Resume_word_dist, Resume_word_dist_list = word_freq_distribution(Resume_word)

    # print (Job_word_dist_list, Resume_word_dist_list)

    matched_words = list_compare(Job_word_dist_list, Resume_word_dist_list)
    # print(list_compare(Job_word_dist, Resume_word_dist))

    Job_word_dist_WSWords, Job_word_dist_WSWords_list = word_freq_distribution(Job_token)
    Resume_word_dist_WSWords, Resume_word_dist_WSWords_list = word_freq_distribution(Resume_token)

    ################## removing unncessary words


    ######################

    # print("Job WO Stopwords")
    # print(Job_word_dist)
    # print("Job W Stopwords")
    # print(Job_word_dist_WSWords)
    # print("Resume WO Stopwords")
    # print(Resume_word_dist)
    # print("Resume W Stopwords")
    # print(Resume_word_dist_WSWords)

    print("There are " + str(len(Job_word)) + " unique words in Job Desc")
    print("There are " + str(len(Resume_word)) + " unique words in Resume")
    print("There are " + str(len(matched_words)) + " matched words in both resume and job desc")

    #print(Job_word_dist.max())
    # print(Resume_word_dist_list)
    #
    #print(list_compare(Job_noPunc, Resume_noPunc))
    # print(len(Job_noPunc))
    # print(len(list_compare(Job_noPunc, Resume_noPunc)))

    ############### Why am I getting fdist 0???????: fixed it: distribution func loop was commented out
    ################
    return len(Job_word), len(Resume_word), len(matched_words)

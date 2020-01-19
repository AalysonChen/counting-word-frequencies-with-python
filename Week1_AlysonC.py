#!/usr/bin/env python
# coding: utf-8

# ### Week one Homework 
# Submitted by Alyson Chen
# 
# Submitted to Professor Peigang Zhang

# In[4]:


from __future__ import print_function


def get_word_counts(data_path):
    """
    return sorted (word, count) list, sort by count
    """
    word_count_dict = {}

    with open(data_path, 'r') as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                if word not in word_count_dict:
                    word_count_dict[word] = 0
                word_count_dict[word] += 1

    sorted_word_counts = sorted(word_count_dict.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_word_counts


input_data_path = './big_data_intro.txt'
word_counts = get_word_counts(input_data_path)

for word, count in word_counts[:100]:
    print(word, count)


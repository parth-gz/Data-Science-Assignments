# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:07:35 2024

@author: Vaishnavi
"""
#import necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#load the CSV file
file_path="C:/10-reccomendation_engine/Entertainment.csv"
data=pd.read_csv(file_path)

#step 1:Preprocess the"category" column using TF-IDF
tfidf=TfidfVectorizer(stop_words='english')#remove common stop words
tfidf_matrix=tfidf.fit_transform(data['Category'])#fit and transform the category data

#step 2:compute the cosine similarity between titles
cosine_sim=cosine_similarity(tfidf_matrix,tfidf_matrix)

#step 3:create a function to recommend titles based on similarity
def get_recommendations(title,cosine_sim=cosine_sim):
    #get the index of the title that matches the input title
    idx=data[data['Titles']==title].index[0]
    '''data['Titles']==title
    this creates a boolean mask(a series of True and False values)
    indicating which rows in the Titles column match 
    '''
    #get the pairwise similarity scores of al titles with that title
    sim_scores=list(enumerate(cosine_sim[idx]))
    
    #sort the titles based on the similarity scores in descending order
    sim_scores=sorted(sim_scores,key=lambda x:x[1],reverse=True)
    
    #get the indices of the most similar titles
    sim_indices=[i[0] for i in sim_scores[1:6]]
    #exclude the first 
    
    #return the top 5 most similar titles
    return data['Titles'].iloc[sim_indices]

#test the recommendation system with an example title
example_title ="Toy Story (1995)"
recommended_titles=get_recommendations(example_title)

#print thw recommendations
print(f"Recommendations for '{example_title}':")
for title in recommended_titles:
    print(title)
"""Othello (1995)
Sense and Sensibility (1995)
Dracula: Dead and Loving It (1995)
American President, The (1995)
When Night Is Falling (1995)"""





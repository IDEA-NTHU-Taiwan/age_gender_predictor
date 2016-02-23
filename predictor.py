import csv
import numpy as np

age_intercept = 23.2188604687
gender_intercept = -0.06724152


def load_age_lexica(file_name = "emnlp14age.csv"):
	age_lexica = {}
	with open(file_name, mode='r') as infile:
	    reader = csv.DictReader(infile)
	    for data in reader:
	    	weight = data['weight']
	    	term = data['term']
	    	age_lexica[term] = weight


	del age_lexica['_intercept']
	return age_lexica


def load_gender_lexica(file_name = "emnlp14gender.csv"):
	gender_lexica = {}
	with open(file_name, mode='r') as infile:
	    reader = csv.DictReader(infile)
	    for data in reader:
	    	weight = data['weight']
	    	term = data['term']
	    	gender_lexica[term] = weight


	del gender_lexica['_intercept']
	return gender_lexica

def lexica_to_mapping_arrays(lexica):
	term_to_index = {}
	weighted_scores = np.zeros(len(lexica).dtype=float)
	i = 0 
	for term, score in lexica:
		term_to_index[term] = i
		weighted_scores[i] = score
	return term_to_index, weighted_scores





def get_gender(text, term_to_index, weighted_scores):
	words = text.split()
	term_to_index = 
	text_scores = np.zeros(weighted_scores.shape[0],dtype=float)




age_lexica = load_age_lexica()
gender_lexica = load_gender_lexica()

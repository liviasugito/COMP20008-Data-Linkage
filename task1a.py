import csv
import textdistance
import pandas as pd
from fuzzywuzzy import fuzz
import re

def check_bigger(a,b):
    if(a>b):
        return a
    else:
        return b
    
#weight for each column
w_title = 70
w_price = 30

data_amazon = pd.read_csv('amazon_small.csv',encoding = 'ISO-8859-1')
data_google = pd.read_csv('google_small.csv',encoding = 'ISO-8859-1')

csv_file1 = open('task1a.csv','w')
csv_writer1 = csv.writer(csv_file1)
csv_writer1.writerow(['idAmazon','idGoogleBase'])

for ind, row_amz in data_amazon.iterrows():
    #list of matched scores that passes threshold
    score = []
    #contains google link that product matches with amazon product
    #and passes threshold
    matches = []
    for ind, row_ggl in data_google.iterrows():
        
        total = 0
        regex = re.compile(".*?\((.*?)\)")
        result_amz = re.sub("[\(\[].*?[\)\]]", "", row_amz['title'])
        result_ggl = re.sub("[\(\[].*?[\)\]]", "", row_ggl['name'])
        
        textdist = textdistance.jaro_winkler(result_amz,result_ggl)
        
        #searching for possible name matches
        if(textdist < 0.46):
            continue
        else:
            sc_title = fuzz.token_set_ratio(result_amz,result_ggl)
            denom = w_title
            
        #searching for possible price matches    
        if row_amz['price'] != 0 and row_ggl['price'] != 0:
            denom += w_price
            
            #normalising price difference, ranges from 0 to 1
            price_diff = row_amz['price']-row_ggl['price']
            price_ratio = 1 - abs((price_diff/check_bigger(row_amz['price'],row_ggl['price'])))
            
        else:
            price_ratio = 0
            
        #weighted total score    
        total = round(((sc_title*w_title)+(price_ratio*w_price*100))/denom,0)
        
        
        if total > 70:
            matches.append(row_ggl['idGoogleBase'])
            score.append(total)
            
    if len(score) > 0:
        #find the index of maximum score then write to csv
        maximum = score.index(max(score))
        csv_writer1.writerow([row_amz['idAmazon'],matches[maximum]])
            
csv_file1.close()
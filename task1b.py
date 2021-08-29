import csv
import pandas as pd
import numpy as np
import math
data_amazon = pd.read_csv('amazon.csv',encoding = 'ISO-8859-1')
data_google = pd.read_csv('google.csv',encoding = 'ISO-8859-1')



csv_file = open('amazon_blocks.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['block_key','product_id'])
csv_file2 = open('google_blocks.csv','w')
csv_writer2 = csv.writer(csv_file2)
csv_writer2.writerow(['block_key','product_id'])

def check_bucket_small(value):
    if val <=5 and val >0:
        return 1    
    elif val <= 30 and val > 5:
        return 2
    elif val <=72 and val> 30:
        return 3    
    elif val <= 90 and  val>72:
        return 4
    elif val <= 110 and val > 90:
        return 5
    elif val <=160 and val> 110:
        return 6
    else:
        return 0
    
def check_bucket_med(value):
    
    if val <= 225 and val > 160:
        return 7
    elif val <= 250 and val > 225:
        return 8
    elif val <=270 and val> 250:
        return 9
    elif val <= 330 and val > 270:
        return 10
    elif val <= 385 and val > 330:
        return 11
    elif val <=600 and val>385:
        return 12
    elif val <= 800 and val >600:
        return 13
    else:
        return 0
    
def check_bucket_big(value):
    if val <= 1100 and val > 800:
        return 14
    elif val <= 1500 and val > 1100:
        return 15
    elif val <=4000 and val> 1500:
        return 16
    elif val > 4000:
        return 17
    else:
        return 0

for idx,row in data_amazon.iterrows():
    val = math.ceil(row['price'])
    small = check_bucket_small(val)
    item = row['idAmazon']
    if small != 0:
        csv_writer.writerow([str(small),item])
    else:
        med = check_bucket_med(val)
        if med != 0:
            csv_writer.writerow([str(med),item])
        else:
            big = check_bucket_big(val)
            if big != 0:
                csv_writer.writerow([str(big),item])
            else:
                continue
                
for idx,row in data_google.iterrows():
    if isinstance(row['price'], str):
        row_price = row['price'].strip(' gbp')
        val = math.ceil(float(row_price))
        
    else:
        
        val = math.ceil(float(row['price']))
        
    small = check_bucket_small(val)
    item = row['id']
    if small != 0:
        csv_writer2.writerow([str(small),item])
    else:
        med = check_bucket_med(val)
        if med != 0:
            csv_writer2.writerow([str(med),item])
        else:
            big = check_bucket_big(val)
            if big != 0:
                csv_writer2.writerow([str(big),item])
            else:
                continue   
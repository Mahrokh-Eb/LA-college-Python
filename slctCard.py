# video-15
# how to use boolean array

import sys
import random

n = int(sys.argv[1]) # n misahe un chanjur k mikham, like dell, khaj, khesht, pik, az har kudum yeki mikham.

count = 0 #mige chan ta entekhab kardam - tedade entekhab ham
collected_count = 0 #mige az un "n" ta chantasho entekhab kardam
is_collected = [False]* n

while collected_count < n:
     count += 1
     value = random.randrange (0, n)
     if not is_collected[value]: #age mese avalesh nabashe
         collected_count +=1
         is_collected_value = True

print(count)

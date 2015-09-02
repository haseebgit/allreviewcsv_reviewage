import csv
import datetime
from collections import Counter, OrderedDict
# This is "import matplotlib.pyplot as plt"
import matplotlib.pyplot as plt
y = []
with open('all-review.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
    	if row[4] == 'lastchanged':
    		continue
    		#Connverting time from csv to proper datetime object
        x = str(datetime.datetime.strptime(row[4], '%Y-%m-%dT%XZ')).split()[0]
        y.append(datetime.datetime.strptime(x, '%Y-%m-%d'))
        z = Counter(y)

z = OrderedDict(sorted(z.items(), key=lambda pp: pp[0]))
q = z.keys()
w = z.values()

plt.plot(q,w)
plt.gcf().autofmt_xdate()
plt.show()
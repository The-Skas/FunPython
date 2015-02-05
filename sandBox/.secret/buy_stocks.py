import urllib2
import time 

price = 99.99 
while price > 6.74: 
	# We tell the computer to sleep
    time.sleep(3)     
    page = urllib2.urlopen("http://beans-r-us.appspot.com/prices.html") 
    text = page.read().decode("utf8") 
    where = text.find('>$') 
    start_of_price = where + 2 
    end_of_price = start_of_price + 4 
    price = float(text[start_of_price:end_of_price]) 
print ("Buy!")

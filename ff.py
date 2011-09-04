from BeautifulSoup import BeautifulSoup
import urllib2
import re

def findRegex(findStr, regexStr):
    found = False
    match = re.search(regexStr, findStr)
    if match:
        found = True
    return found

def fairnessFunction(fairStr, idNum, fairNum):
    fairRegex = r'.*[Ff][Aa][Ii][Rr].*'
    isFair = findRegex(fairStr, fairRegex)
    if isFair == True:
        fairNum = fairNum + 1
        print str(idNum) + " needs Fair:" + oddStr
    return fairNum

#Loop through 10 marriage classified pages

#totalAds is used to count the number of ads scanned
totalAds = 1.0
#number of fair requests
fairNum = 0.0
for pageNum in range(1,11):
    print "Processing page " + str(pageNum) + " ..."

    #Getting all content from webpage
    urlStr = "http://www.thehindu.com/classifieds/matrimonial/?list1=brides&pageNo="+str(pageNum)
    page = urllib2.urlopen(urlStr)
    soup = BeautifulSoup(''.join(page))

    #Finding and storing only the classified information
    classifieds = soup.findAll("div","search-classifieds")

    #Looping through all the classifieds
    #Since div - search-classifieds is used for all odd number of classifieds
    #need to find the even numbered ones by using nextSibling function



    for classified in classifieds:
        #Odd numbered classified information
        oddStr = classified.contents[0].string
        #process the string for interesting patterns
        #find strings with the word fair in it
        fairNum = fairnessFunction(oddStr, totalAds, fairNum)
          
        #Even numbered classified information
        evenStr = classified.nextSibling.string 
        #find strings with the word fair in it
        fairNum = fairnessFunction(evenStr, totalAds, fairNum)
        
        totalAds = totalAds + 2
    
#Print a percentage of number asking for Fair vs total Ads
fairPer = fairNum / totalAds * 100.0
print "Percentage asking for a Fair better half: " + str(fairPer)

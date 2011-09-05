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
    goodLookingRegex = r'.*[gG][oO][oO][dD].*[lL][oO][oO][kK][iI][nN][gG].*'
    isGoodLooking = findRegex(fairStr, goodLookingRegex)
    beautifulRegex = r'.*[bB][eE][aA][uU][tT][iI][fF][uU][lL].*'
    isBeautiful = findRegex(fairStr, beautifulRegex)
    if isFair == True or isGoodLooking == True or isBeautiful == True:
        fairNum = fairNum + 1
        #print str(idNum) + " needs Fair:" + fairStr
    return fairNum

def intelligenceFunction(inStr, idNum, inNum):
    intelligenceRegex = r'.*[iI][nN][tT][eE][lL][lL][iI][gG][eE][nN][tT].*'
    isIntelligent = findRegex(inStr, intelligenceRegex)
    smartRegex = r'.*[sS][mM][aA][rR][tT].*'
    isSmart = findRegex(inStr, smartRegex)
    educatedRegex = r'.*[eE][dD][uU][cC][aA][tT][eE][dD].*'
    isEducated = findRegex(inStr, educatedRegex)
    if isIntelligent == True or isSmart == True or isEducated == True:
        inNum = inNum + 1
        #print str(idNum) + " needs Intelligent:" + inStr
    return inNum

def girlIntelligenceFunction(ginStr, idNum, ginNum):
    adFound = False
    
    #Synonyms for intelligence
    intelligenceRegexArray = [r'.*[eE]ducated.*', r'.*[iI]ntelligent.*', r'.*[sS]mart.*']

    #Remove the cases where an intelligent boy is being advertised
    intelligentBoyRegexArray = [r'.*[Bb]oy.*', r'.*[Gg]room.*', r'.*[Gg]uy.*', r'.*[Pp]arents.*', r'.*[Ff]amily.*', r'.*[Dd]ivorcee.*']
    
    #Synonyms for bride    
    brideRegexArray = [r'[mM]atch.*', r'[bB]ride.*', r'[gG]irl.*']
                
    #Controlling for ads that advertise the boy as intelligent
    #but do not care about the girl
    
    resultWithoutBoy = False
    for inRegex in intelligenceRegexArray:
        for brideRegex in brideRegexArray:
            withoutBoyCombiRegex = inRegex + brideRegex
            iswithoutBoyBride = findRegex(ginStr, withoutBoyCombiRegex)
            if iswithoutBoyBride == True:
                resultWithoutBoy = True
    
    resultWithBoy = False
    for inRegex in intelligenceRegexArray:
        for brideRegex in brideRegexArray:
            for boyRegex in intelligentBoyRegexArray:
                withBoyCombiRegex = inRegex + boyRegex + brideRegex
                iswithBoyBride = findRegex(ginStr, withBoyCombiRegex)
                if iswithBoyBride == True:
                    resultWithBoy = True
    
    if resultWithoutBoy == True and resultWithBoy == False:
        adFound = True
    else:
        resultWithBG = False
        for inRegex in intelligenceRegexArray:
            for brideRegex in brideRegexArray:
                for boyRegex in intelligentBoyRegexArray:
                    withBoywithGirlRegex = inRegex + boyRegex + inRegex + brideRegex
                    isbg = findRegex(ginStr, withBoywithGirlRegex)
                    if isbg == True:
                        resultWithBG = True
        
        if resultWithBG == True:
            adFound = True
                    
    if adFound == True:
        ginNum = ginNum + 1
        print str(idNum) + " needs Intelligent Bride:" + ginStr
    
    return ginNum
    

#Loop through 10 marriage classified pages

#totalAds is used to count the number of ads scanned
totalAds = 1.0
#number of fair requests
fairNum = 0.0
#number of intelligent requests
inNum = 0.0
#number of intelligent girl requests
ginNum = 0.0

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
        inNum = intelligenceFunction(oddStr, totalAds, inNum)
        ginNum = girlIntelligenceFunction(oddStr, totalAds, ginNum)
        #Even numbered classified information
        evenStr = classified.nextSibling.string 
        #find strings with the word fair in it
        fairNum = fairnessFunction(evenStr, totalAds, fairNum)
        inNum = intelligenceFunction(evenStr, totalAds, inNum)
        ginNum = girlIntelligenceFunction(evenStr, totalAds, ginNum)
        
        totalAds = totalAds + 2
    
#Print a percentage of number asking for Fair vs total Ads
fairPer = fairNum / totalAds * 100.0
print "Percentage valuing Fairness: " + str(fairPer)
inPer = inNum / totalAds * 100.0
print "Percentage valuing Intelligence: " + str(inPer)
ginPer = ginNum / totalAds * 100.0
print "Percentage valuing Intelligent brides: " + str(ginPer)

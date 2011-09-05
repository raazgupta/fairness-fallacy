#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi
#from BeautifulSoup import BeautifulSoup
import urllib2
import re

# enable debugging
import cgitb
cgitb.enable(1)

# print out the type of content on the site
print "Content-Type: text/html\n"

#Function to check whether there is a regular expression match in a string
#def findRegex(findStr, regexStr):
#    found = False
#    match = re.search(regexStr, findStr)
#    if match:
#        found = True
#    return found

##Function to find all the Ads that are interested in Appearances
#def fairnessFunction(fairStr, idNum, fairNum):
#    global fairList
#    
#    fairRegex = r'.*[Ff][a][i][r].*'
#    isFair = findRegex(fairStr, fairRegex)
#    goodLookingRegex = r'.*[gG][o][o][d].*[lL][o][o][k][i][n][g].*'
#    isGoodLooking = findRegex(fairStr, goodLookingRegex)
#    beautifulRegex = r'.*[bB][e][a][u][t][i][f][u][l].*'
#    isBeautiful = findRegex(fairStr, beautifulRegex)
#    if isFair == True or isGoodLooking == True or isBeautiful == True:
#        fairNum = fairNum + 1
#        fairList.append(fairStr)
#    return fairNum

##Function to find all the Ads that are interested in intelligent girls
#def girlIntelligenceFunction(ginStr, idNum, ginNum):
#    global intelligentList
#    
#    adFound = False
#    
#    #Synonyms for intelligence
#    intelligenceRegexArray = [r'.*[eE]ducated.*', r'.*[iI]ntelligent.*', r'.*[sS]mart.*']

#    #Remove the cases where an intelligent boy is being advertised
#    intelligentBoyRegexArray = [r'.*[Bb]oy.*', r'.*[Gg]room.*', r'.*[Gg]uy.*', r'.*[Pp]arents.*', r'.*[Ff]amily.*', r'.*[Dd]ivorcee.*']
#    
#    #Synonyms for bride    
#    brideRegexArray = [r'[mM]atch.*', r'[bB]ride.*', r'[gG]irl.*']
#                
#    #Controlling for ads that advertise the boy as intelligent
#    #but do not care about the girl
#    
#    resultWithoutBoy = False
#    for inRegex in intelligenceRegexArray:
#        for brideRegex in brideRegexArray:
#            withoutBoyCombiRegex = inRegex + brideRegex
#            iswithoutBoyBride = findRegex(ginStr, withoutBoyCombiRegex)
#            if iswithoutBoyBride == True:
#                resultWithoutBoy = True
#    
#    resultWithBoy = False
#    for inRegex in intelligenceRegexArray:
#        for brideRegex in brideRegexArray:
#            for boyRegex in intelligentBoyRegexArray:
#                withBoyCombiRegex = inRegex + boyRegex + brideRegex
#                iswithBoyBride = findRegex(ginStr, withBoyCombiRegex)
#                if iswithBoyBride == True:
#                    resultWithBoy = True
#    
#    if resultWithoutBoy == True and resultWithBoy == False:
#        adFound = True
#    else:
#        resultWithBG = False
#        for inRegex in intelligenceRegexArray:
#            for brideRegex in brideRegexArray:
#                for boyRegex in intelligentBoyRegexArray:
#                    withBoywithGirlRegex = inRegex + boyRegex + inRegex + brideRegex
#                    isbg = findRegex(ginStr, withBoywithGirlRegex)
#                    if isbg == True:
#                        resultWithBG = True
#        
#        if resultWithBG == True:
#            adFound = True
#                    
#    if adFound == True:
#        ginNum = ginNum + 1
#        intelligentList.append(ginStr)
#    return ginNum

def main():
#    ##Loop through 10 marriage classified pages

#    ##totalAds is used to count the number of ads scanned
#    #totalAds = 1.0
#    ##number of fair requests
#    #fairNum = 0.0
#    ##number of intelligent girl requests
#    #ginNum = 0.0
#    ##list of fair ads
#    #fairList = []
#    ##list of intelligent girl ads
#    #intelligentList = []

    #Adding header information
    print "<html>"
    print "<head>"
    print '<link rel="stylesheet" type="text/css" href="http://www.soulofmachine.com/css/ff.css" />'
    print "<title>Fairness Fallacy</title>"
    print "</head>"

    #Adding body information
    print "<body>"

#    #for pageNum in range(1,11):
#    #    
#    #    #Getting all content from webpage
#    #    urlStr = "http://www.thehindu.com/classifieds/matrimonial/?list1=brides&pageNo="+str(pageNum)
#    #    page = urllib2.urlopen(urlStr)
#    #    soup = BeautifulSoup(''.join(page))

#    #    #Finding and storing only the classified information
#    #    classifieds = soup.findAll("div","search-classifieds")

#    #    #Looping through all the classifieds
#    #    #Since div - search-classifieds is used for all odd number of classifieds
#    #    #need to find the even numbered ones by using nextSibling function



#    #    for classified in classifieds:
#    #        #Odd numbered classified information
#    #        oddStr = classified.contents[0].string
#    #        #process the string for interesting patterns
#    #        fairNum = fairnessFunction(oddStr, totalAds, fairNum)
#    #        #ginNum = girlIntelligenceFunction(oddStr, totalAds, ginNum)
#    #        #Even numbered classified information
#    #        evenStr = classified.nextSibling.string 
#    #        fairNum = fairnessFunction(evenStr, totalAds, fairNum)
#    #        #ginNum = girlIntelligenceFunction(evenStr, totalAds, ginNum)
#    #        
#    #        totalAds = totalAds + 2
#        
#    #Print a percentage of number asking for Fair vs total Ads
#    #fairPer = fairNum / totalAds * 100.0
#    #fairPer = int(fairPer)
#    #print "<div>People interested in a bride that has fair skin, beauty, and good looks: " + str(fairPer) + "%</div>"
#    ##Print a percentage of number asking for Intelligence vs total Ads
#    ##ginPer = ginNum / totalAds * 100.0
#    ##ginPer = int(ginPer)
#    #print "<div>People interested in a bride that has education and intelligence: " + str(ginPer) + "%</div>"

#    ##Loop through Fair List and print the Ads
#    #print "<div>List of Ads interested in the Cover of the Book:</div>"
#    #for fair in fairList:
#    #    print "<div>" + fair + "</div"
#    ##Loop through Intelligent List and print the Ads
#    ##print "<div>List of Ads interested in the Contents of the Book:</div>"
#    ##for intelligent in intelligentList:
#    ##    print "<div>" + intelligent + "</div>"
#    #    
    #Close the body and html tags
    print "</body>"
    print "</html>"
    
main()


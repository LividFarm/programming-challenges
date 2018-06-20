'''Web crawlers marry queuing and HTML parsing and form the basis of search engines
etc. Writing a simple crawler is a good exercise in putting a few things together.
Writing a well behaved crawler is another step up.'''
from bs4 import BeautifulSoup
import urllib.request
import time

def main():
    input_url = "https://www.google.com/" #input("Input URL: ")
    depth = 2 #int(input("Recursion Depth: "))

    visited = []    #ensures no repeated nodes
    unchecked = []
    checked_robots = []   #the 'core' of the url, e.g. 'reddit' to allow robots.txt checking
    banned = []
    checked_robots = []
    topLevelDomains = [".com", ".co.uk", ".org", ".info"]
    
    #add first url to unchecked to get started
    unchecked.append(input_url)
    
    #repeat for depth
    for i in range(depth):
        retryCount = 0
        for link in unchecked:
            tempStore = [] #remove all vars in tempStore
            
            #get the 'core' of the link and check robot.txt
            core = get_core(link, topLevelDomains)
            #ensure robots.txt checked
            robot = check_robots(link, topLevelDomains)
            if robot != [] and robot != "":
                checked_robots.append(core)
            
            #for link in the unchecked links list, check the page and extract the link
            notBanned = True
            retry = True

            #check for banned things in robots.txt
            for line in banned:
                if line in link:
                    notBanned = False
                    
            if notBanned == True:
                while retry == True:
                    try:
                        tempLinks = extract_links(get_page(link))
                        for temp in tempLinks:
                            if temp not in visited and temp not in unchecked and temp != link:
                                tempStore.append(temp)
                        retry = False
                        print("Success for: {}.".format(link))
                    except:
                        retryCount = retryCount + 1
                        print("Retrying attmept {0} for {1}...".format(retryCount, link))
                        if retryCount == 15:
                            print("Retry attempts limit reached, aborting...")
                            retry = False
                        time.sleep(2)
                        
            visited.append(link)
            unchecked.remove(link)
        unchecked = unchecked + tempStore
        
    #combine and output data
    links = visited + unchecked
    print()
    print("{0} links found at max depth {1}.".format(len(links), depth))
    for link in links:
        print(link)
    print()
    print("{} robots.txt successful:".format(len(checked_robots)))
    for robot in checked_robots:
        print(robot)

def get_core(url, topLevelDomains):
    #gets the index of the start and end of thestring
    startChar = int(url.find("www.")) + 4
    for domain in topLevelDomains:
        if domain in url:
            endChar = int(url.find(domain) + len(domain))
    coredURL = url[startChar:endChar]
    if "/" in coredURL:
        print("Coring Failed for url: {}.".format(coredURL))
    return coredURL
    
def check_robots(url, topLevelDomains):
    banned = []
    domain = False
    
    if 'Failed' not in str(url):
        domainBool = True
        
    if domainBool == True:
        print("Checking robot {0}/robots.txt".format(url))
        robots = str(get_page(url + "/robots.txt")).split('\n')
        for line in robots:
            if "Disallow" in line and len(line[line.find(" ") + 1:len(line)]) > 2:
                banned.append(line[line.find(" ") + 1:len(line)])
    return banned

def extract_links(page):
    links_found = []
    for link in page.findAll('a'):
        item = str(link.get('href'))
        if "http://" in item or "https://" in item:
            links_found.append(item)
    return links_found

def get_page(url):
    '''Takes a url and returns as a variable the contents of the page that url links
    to.'''
    page = urllib.request.urlopen(url)
    return BeautifulSoup(page, "html.parser")
    

if __name__ == "__main__":
    main()

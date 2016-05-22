import urllib2
from bs4 import BeautifulSoup
import getopt
import sys
import pdb

def makeint(s):
  s.strip()
  ans=0
  for i in xrange(len(s)):
    if s[i].isdigit():
      ans=10*ans+int(s[i])
  return ans
    
def main(argv):

  try:
    opts, args = getopt.getopt(argv,'hp:k:', )
    if len(opts) == 0:
      print 'Use python webcrawler.py -h for help'
      sys.exit(2)
  except getopt.GetoptError:
    print 'Use python webcrawler.py -h for help'
    sys.exit(2)
 
  for op,ar in opts: 
     
    if op == '-p':
      try: 
        int(ar)
      except ValueError:
        print 'Error. Page number should be a number'
        sys.exit(2)
      pageno = ar
    elif op == '-k':
      keyword = ar
    elif op == '-h':
      print 'Use python webcrawler.py -p pagenumber -k keyword'
      sys.exit(2)
    else:  assert False, 'unhandled option'

  if 'keyword' not in locals():
    print 'Keyword not specified try again'
    sys.exit(2)

  if 'pageno' in locals():
    test = 'http://www.shopping.com/products~PG-'+str(pageno)+'?KW='+str(keyword)
  else:
    test = 'http://www.shopping.com/products?KW=' + str(keyword)

  page = urllib2.urlopen(test).read()

  soup = BeautifulSoup(page)

  if soup.body['id'] == 'noResults':
    print 'No results for this keyword'
    sys.exit(1)
  else:
    alltext = soup.get_text()
    res = alltext[alltext.find('Results '): alltext.find('Results ')+25]
    if 'pageno' in locals():
      firstno = makeint(res[res.find('Results ')+8: res.find('-')-1])
      lastno = makeint(res[res.find('-')+2:res.find('of ')])
      print 'Number of results on page', pageno, ':', lastno-firstno+1 
    else:
      print 'Number of results found', res[res.find('of ')+3:res.find('\n')]

if __name__ == '__main__':
  main(sys.argv[1:])

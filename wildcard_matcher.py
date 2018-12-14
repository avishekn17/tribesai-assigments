import re
import fnmatch

class Solution(object):
    def isMatch(self, s, p):
       fnregex = fnmatch.translate(p)
       regex = re.compile(fnregex)
       matchObj = regex.match(s)
       if matchObj:
          return True
       else:
          return False
        

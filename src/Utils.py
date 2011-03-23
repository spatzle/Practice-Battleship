'''
Created on 2011-03-23

@author: joyce
'''
import re
def matched(pattern, string, repl='_._'):

    r = re.compile(pattern)
    m = r.search(string)

    if m:
        return True
#        i = 0
#        while m:
#            m_start = m.start()
#            m_end = m.end()
#
#            i += 1
#            print( '%d) start: %d, end: %d, str: %s' %
#                   (i, m_start, m_end, string[m_start:m_end]) )
#
#            if m.groups():           # capturing groups
#                print('   groups: ' + str(m.groups()))
#
#            if m_end == len(string): # infinite loop if
#                break                #    m_start == m_end == len(string)
#            elif m_start == m_end:   # zero-width match;
#                m_end += 1           #    keep things moving along
#
#            m = r.search(string, m_end)                
#
#        print( 'global replace (%s):\n%s' %
#               (repl, re.sub(pattern, repl, string)) )

    else:
        return False
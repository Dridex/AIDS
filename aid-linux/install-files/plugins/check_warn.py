#!/usr/bin/python
 
# imports
from optparse import OptionParser
 
# Define return codes
UNKNOWN = -1
OK = 0
WARNING = 1
CRITICAL = 2
 
# Template for reading parameters from command line
parser = OptionParser()
parser.add_option("-m", "--message", dest="message", 
   default='', help="A message to print after OK - ")
(options, args) = parser.parse_args()
 
# Return output using the exmaple -m parameter parsed from commandline
print 'I\'m warning you %s' % (options.message)
raise SystemExit, WARNING

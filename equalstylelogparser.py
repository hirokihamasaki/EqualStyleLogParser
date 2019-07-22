
#!/usr/bin/env python

import pandas as pd
import sys
import re
import argparse

pd.set_option('line_width', 1000000000)
pd.set_option('display.max_rows', 10000000000)


def parseLog(data):
    result = pd.DataFrame()
    lineNum = 1
    for i in data:
        split = re.findall(pat, i)
        try:
            split = map(lambda x: (x[0], x[1].strip("\"")), split)
        except:
            print "parse error on {} line:".format(lineNum, split)

        try:
            if len(split) != 0:
                result = pd.concat([result, pd.DataFrame(dict(split), index=[0])], ignore_index=True)
        except:
            print "merge error on {} line: {}".format(lineNum, split)
        lineNum += 1
    
    return result


parser = argparse.ArgumentParser(description="conert '=' style log to columns style log", epilog="sample command: python %(prog)s path/to/log -t time,sourceIP")
parser.add_argument("logfile", help="filepath of log file")
parser.add_argument("-t", "--targetcol", type=str, help="target columns to display")
parser.add_argument("-q", "--quote", type=str, default="\"", help="quote charactor")
parser.add_argument("-d", "--displayheader", action='store_true', help="get header name observed in first 100 lines")
args = parser.parse_args()


pat = r"\s*({0}[^{0}]+{0}|[^=\s]+)=({0}[^{0}]+{0}|[^\s]+)".format(args.quote)

with open(args.logfile, "r") as fobj:
    data = fobj.read().splitlines()

if args.displayheader:
    data = data[:(len(data)-1)%100]
    result = parseLog(data)
    for i, name in enumerate(result.columns):
        print i+1, name
    exit()

result = parseLog(data)
if args.targetcol:
    result = result[map(lambda x: x.strip(), args.targetcol.split(","))]
    print "\t".join(result.columns)
    for i, row in result.iterrows():
        print "\t".join(row)
else:
    print "\t".join(result.columns)
    for i, row in result.iterrows():
        print "\t".join(row)

#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

from sets import Set
import os
fname='relationships_w_pops_121708.txt'
d = set()
file = open(fname, 'r')


for line in file :
    # hold the populations name

    linelist = line.strip().split()
    (FID, IID, dad, mom, sex, pheno,pop) = linelist[0:7]
    if pop == 'population':
        continue
    else:
        d.add(pop) # add the population name to the set

    for item in d:
        filename= item      # for each population in the set compare it with the population in list
        # then add the population to the appropriate file


        if item== pop:
            with open(filename+'.txt', 'a') as f:# create a new file for each population
                f.write(str(FID +"\t"+ IID+"\n")) # write the first two columns




for item in d:
    cmd = ('wc -l ' +item+'.txt') # write the number of lines of each file to the command line
    os.system(cmd)
#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

from sets import Set


# read the realtionships file and divide them by populations

fname='relationships_w_pops_121708.txt'
d = set()  # hold the populations name
file = open(fname, 'r')
for line in file :
    linelist = line.strip().split()
    (FID, IID, dad, mom, sex, pheno,pop) = linelist[0:7]
    if pop == 'population':
        continue
    else:
        d.add(pop) # add the population name to the set


for item in d: # for each population in the set compare it with the population in list
                # then add the population to the appropriate file
        filename= item
        if item== pop:
            with open(filename+'.txt', 'a') as f:  # create a new file for each population
                f.write(str(FID +"\t"+ IID+"\n"))  # write the first two columns


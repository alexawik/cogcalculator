'''
Vowel center of gravity calculator written by Alexandra Wikström (alexandra.wikstrom@helsinki.fi), Feb 2023
Reads a list of words and calculates a spatial center point (x,y) of vowels for each word
based on the two-dimensional position of a vowel in the IPA vowel chart.
Writes the CoG coordinates into a .txt file.
'''

#Import the module containing vowels and their coordinates
import vowelcoordinates

# open file and read the content in a list
# empty list to read list from a file
wordlist= []

with open(r'wordforms.txt', 'r', encoding='utf8') as fp:
    for line in fp:
        # remove linebreak from a current name
        # linebreak is the last character of each line
        x = line[:-1]
        # add current item to the list
        wordlist.append(x)
fp.close()

print(wordlist)

#-----helper function to extract list of coordinates from a list of vowels
def vows2coord(word):
    coord= []
    vows=[]
    #goes through the word as a list and matches vowels to ones in the vowels list
    for i in word:
        if i not in vows:
        #adds the (vowel, (x,y,1)) tuple into the coord list
            coord.append(vowelcoordinates.givecoord(i))
            vows.append(i)
        else:
        #adds one more weight to the mass of the existing vowel coordinate
            for j in coord:
                if j!=[] and i==j[0]:
                    j[2]+=1

    #clean the empty lists from coord
    while [] in coord:
        coord.remove([])
    #return the list of coordinate tuples for the CoG function to do its calculations
    return coord

#print(vows2coord("alemoyaanay"))
#test vows2coord
#print(vows2coord("b"))

#-----helper function that takes the list of coordinates and returns a CoG value
def coords2cog(coords, weighted):
    xs=[]
    ys=[]
    ms=[]
    cogvalue=[]
    x=0
    y=0
    n=0
    m=0

    if coords!=[]:
        #extract the x and y coordinates into their own lists
        for i in coords:
            xs.append(i[1][0])
            ys.append(i[1][1])
            ms.append(i[2])

        #calculate CoG
        if weighted:
        #weighted CoG
            for i in range(len(xs)):
                n+=(xs[i]*ms[i])
                m+=(ys[i]*ms[i])
            x=n/sum(ms)
            y=m/sum(ms)
            cogvalue=x,y
        else:
        #unweighted CoG, each mass = 1
            x=sum(xs)/len(xs)
            y=sum(ys)/len(ys)
            cogvalue=x,y
    else:
        #return NA if the word does not have vowels
        cogvalue="NA","NA"

    return cogvalue

#print(coords2cog(vows2coord("aeaae"), True))

#-----MAIN: takes a list of words, writes a list of CoG values
cogs= []

for i in wordlist:
    #give the word to the vows2coord function, can be nested inside coords2cog
    #append the new CoG value to the cogs list
    if wordlist!=[]:
        cogs.append(coords2cog(vows2coord(i), weighted=False))
    else:
        print("File empty or could not be read.")

#print(cogs)
#write the completed list into a text file

with open(r'vowelcogs.txt', 'w') as fp:
    for item in cogs:
        # write each item on a new line
        fp.write('{}\t'.format(item[0])+'{}\n'.format(item[1]))
    print('Done')
fp.close()

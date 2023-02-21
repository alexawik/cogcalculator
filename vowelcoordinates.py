
#each tuple contains the vowel char and another tuple, which in turn has
#the x-coord, y-coord, and an initial mass of 1 for the vowel
lst = [["i",(0.0,6.0),1.0],["y",(0.0,6.0),1.0],["ɨ",(4.0,6.0),1.0],["ʉ",(4.0,6.0),1.0],["ɯ",(8.0,6.0),1.0],["u",(8.0,6.0),1.0],
    ["ɪ",(1.75,5.0),1.0],["ʏ",(1.75,5.0),1.0],["ʊ",(6.5,5.0),1.0],
    ["e",(1.25,4.0),1.0],["ø",(1.25,4.0),1.0],["ɘ",(4.75,4.0),1.0],["ɵ",(4.75,4.0),1.0],["ɤ",(8.0,4.0),1.0],["o",(8.0,4.0),1.0],
    ["ə",(5.0,3.0),1.0],
    ["ɛ",(2.75,2.0),1.0],["œ",(2.75,2.0),1.0],["з",(5.25,2.0),1.0],["ɞ",(5.25,2.0),1.0],["ʌ",(8.0,2.0),1.0],["ɔ",(8.0,2.0),1.0],
    ["æ",(3.0,1.0),1.0],["ɐ",(5.5,1.0),1.0],
    ["a",(4.0,0.0),1.0],["ɶ",(4.0,0.0),1.0],["ɑ",(8.0,0.0),1.0],["ɒ",(8.0,0.0),1.0]]

#matches the given character with one from list
def givecoord(str):
    coordinates=[]
    for i in lst:
        #if char is found in list, return its coordinates
        if i[0]==str:
            coordinates=i
        else:
            continue

    #if the char is not a vowel, an empty tuple will be returned
    return coordinates


#print(givecoord("a")[2])

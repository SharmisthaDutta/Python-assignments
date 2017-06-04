import csv
#import matplotlib.pyplot as plt, mpld3

# try opening the file
with open('portland_or_2011 - 26Apr2017.csv') as f:
        reader =csv.reader(f)
        raincount =[]
        windspeed =[]
        for row in reader:
                if(not row[0].isdigit()):
                        next(reader)
            
                elif(len(row[0])==4):
                    if row[0] not in raincount:
                            raincount.append(row[0])
                            windspeed.append(row[0])
                            next(reader)
                    else:
                            next(reader)

                else:
                        
                        if("Rain" in row[20]):
                                raincount.append("Rain")
                        #windspeed lets add it to a list
                        windspeed.append(row[18])

windjson ={}
rainjson ={}
list2={}
raindata ={}
for entry in windspeed:
        if len(entry)==4:
                #make it a key
                key = entry
                windjson[key] =[]
        else:
                windjson[key].append(entry)
for keys,values in sorted(windjson.items()):
        max =0
        for item in values:
                if item =='-':
                        continue
                
                if (int(item) >max):
                        max = int(item)
        print ("For the year "+keys+" maximum windspeed is "+str(max))
        list2[keys]=max
for entry in raincount:
        if len(entry)==4 and entry.isdigit():
                #make it a key
                key = entry
                rainjson[key] =[]
        else:
                rainjson[key].append(entry)
for keys, values in sorted(rainjson.items()):
        print("For the year "+keys+" the number of days it rained is "+str(len(values)))
        raindata[keys] = len(values)
        
""" plotting the data (max windspeed vs year) using mpld3 and matplotlib
in order for this to work we have to install matplotlib and mpld3 and we can view it in browser
hence I am commenting this part out now if you uncomment these part you can see a data visualization """
##fig =plt.figure(dpi=128, figsize=(10,6))
##list1 = [int(item) for item in list2.keys()]
##list3 = [int(item) for item in list2.values()]
##plt.plot(list1, list3, 'ks-', mec='w', mew=5, ms=1)
##plt.xlabel('years',fontsize=16)
##plt.ylabel('maximum wind speed',fontsize=16)
##mpld3.show()


""" plotting the data (raincount vs year) using mpld3 and matplotlib
in order for this to work we have to install matplotlib and mpld3 and we can view it in browser
hence I am commenting this part out now if you uncomment these part you can see a data visualization """

##fig =plt.figure(dpi=128, figsize=(10,10))
##list1 = [int(item) for item in raindata.keys()]
##list3 = [int(item) for item in raindata.values()]

##plt.scatter(list1, list3, c='red')
##
##plt.xlabel('years',fontsize=16)
##plt.ylabel('raincount',fontsize=16)
##mpld3.show()


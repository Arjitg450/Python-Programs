import numpy as np

names=['arjit','brett','chetan','deval','farukh','govind','harshit']
ndict={'arjit':'0','brett':'1','chetan':'2','deval':'3','farukh':'4',
       'govind':'5','harshit':'6'}

year=['2010','2011','2012','2013','2014','2015','2016']
ydict={'2010':'0','2011':'1','2012':'2','2013':'3','2014':'4','2015':'5',
       '2016':'6'}
#marksobtained_in_english
arjit=[90.3,88,22,56,78,89,85]
brett=[23,81,23,56,73,86,84]
chetan=[23,81,23,56,73,86,84]
deval=[23,81,23,56,73,86,84]
farukh=[23,81,23,56,73,86,84]
govind=[23,81,23,56,73,86,84]
harshit=[23,81,23,56,73,86,84]
marksobtained_in_english=np.array([arjit,brett,chetan,deval,farukh,govind,harshit])
#marksobtained_in_maths
arjit=[90.3,88,22,56,78,89,85]
brett=[23,81,23,56,73,86,84]
chetan=[23,81,23,56,73,86,84]
deval=[23,81,23,56,73,86,84]
farukh=[23,81,23,56,73,86,84]
govind=[23,81,23,56,73,86,84]
harshit=[23,81,23,56,73,86,84]

marksobtained_in_maths=np.array([arjit,brett,chetan,deval,farukh,govind,harshit])

print((marksobtained_in_maths + marksobtained_in_english/200)*100)

print(marksobtained[0][4])




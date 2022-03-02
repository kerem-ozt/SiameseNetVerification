import os
dosya_yolu="C:/Users/mkere/Desktop/Yeni klasör (3)/test"
dirs = []

for i in os.listdir(dosya_yolu):
    if len(i)==2:
        for j in os.listdir(dosya_yolu + '/' + i + '_forg'):
            for k in os.listdir(dosya_yolu + '/' + i):
                print(j[:2] + '/' + j + ',' + k[:2] + '/' + k + ',1')

for i in os.listdir(dosya_yolu):
    if len(i)==2:
        for j in os.listdir(dosya_yolu + '/' + i ):
            for k in os.listdir(dosya_yolu + '/' + i):
                if (j!=k):
                    print (j[:2] + '/' + j + ',' + k[:2] + '/' + k + ',0')

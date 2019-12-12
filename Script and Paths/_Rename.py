##############################################
#
#Script: Renaming Files from CSV of a google sheet.
#
##############################################
#           USER CONFIG
#       Characters and Actors Folders
pathChar = ['Butcher','Chicken','Civilian M','Civilian F','Cockatrice','Guard']
pathActor = ['Ajai','Curtis','Julia','Mostafa','Nico','Saige']
actorInitials = ['AR','CM','JH','MS','ND','SB']
#       Output folder within the character actor directory
#
#IMPORTANT: Name your .csv file as the name of the character folder, pls
##############################################
import csv, os, shutil
_path = os.getcwd()

def PrintCharAct(dic):
    print('Character : Actor(s)\n')
    for i in dic:
        print(i,':',dic[i])

def ReadToDic(file,r,c,dic = {}):
    row = open(file,"r").read().split(r)
    for i in range(len(row)):
        col = row[i].split(c)
        dic[col[0]] = [col[x] for x in range(len(col)) if x > 0 and col[x] != '']
    return dic

def DicWrite(file,dic): #file, dictionary, row, column and line for string sum
    value = 'File Name\tContainer\n' #string sum whole dic
    z = ''
    for i in dic: #loop list
        try:
            z = i.split('_')
            z2 = z[1] + '_' + z[2] + '_' + z[3] + '_' + z[4] + '_' + z[5]
            value = value + i + '\t' + z2 + '\n'#save a long string that represents the dictionary = "key[i]|1|2|3\n" + "key[i]|1|2|3\n" + "etc" ends with a \n
        except:
            print('There are no more files.')
    x = open(file,"w").write(value)


def ParseCSV(fileName):
    counter = 0
    fileName = fileName + '.csv'
    with open(fileName, newline = '') as file_data:
        file_reader = csv.reader(file_data,delimiter = '\t')
        file_matrix = [x for x in file_data]
        for file_data in file_reader:
            file_matrix[counter] = file_data
            counter += 1
    tab = ['' for x in range(len(file_matrix))]
    for i in range(len(file_matrix)): #split to lists
        tab[i] = file_matrix[i].split(',')
    _index = tab[0].index('File Name') #find File Name column
    _desc = tab[0].index('Description')

    tabNum = [['',''] for x in range(len(tab))]
    for i in range(len(tab)):
        tabNum[i][0] = tab[i][0]
        tabNum[i][1] = tab[i][_index]

    for i in range(len(tabNum)): #cleanup
        if ['',''] in tabNum:
            tabNum.remove(['',''])
    return tabNum

def Cleanup(_list):
    for i in range(len(_list)):
        if '' in _list:
            _list.remove('')


def RenameList(wavs_old,csv):
    for i in range(len(_files_list)):
        if '.wav' in _files_list[i]:
            wavs_old[i] = wavs_old[i].strip('.wav')
    Cleanup(wavs_old)
            
    wavs_index = [x.split('_')[0] for x in wavs_old]
    wavs_rest = [x.split('_')[1] for x in wavs_old]

    wavsFileName = ['' for x in wavs_index]
    
    for i in range(len(wavs_index)):
        for j in csv: #go through pair
            if wavs_index[i] == j[0]: #compare number of current file to all the csv id numbers
                wavsFileName[i] = j[1] #FILE NAME Yay
                
    for i in range(len(wavsFileName)): #add stuff
        wavsFileName[i] = wavs_index[i] + '_' + wavsFileName[i] + '_' + actorInitials[pathActor.index(actorName)] + '_' + wavs_rest[i]
    return wavsFileName

##############################################
#Start the stuff, read the .csv
rolesDict = ReadToDic('Roles.csv','\n',',')
PrintCharAct(rolesDict)
while True:
    try:
        fileName = input('\nInput name of .csv file (Without Extension)\n')
        _csv = ParseCSV(fileName)
        break
    except:
        print('File not found. Try again pls.')
while True:
    try:
        actorName = input('\nInput name of the actor.\n')
        if actorName in pathActor: 
            break
        else:
            print('Actor name not found. Try again pls.')
    except:
        print('Actor name not found. Try again pls.')

pathFiles = _path + '/' + fileName + '/' + actorName 
_files_list = os.listdir(pathFiles) #Search for files .wavs

try:
    for i in range(len(_files_list)):
        if '.wav' not in _files_list[i]:
            _files_list.pop(i)
except:
    print(_files_list)

check_user = input('File was read, press any key to continue.')

wavsFileName = RenameList(_files_list,_csv)

##############################################
##THIS IS THE PART FOR COPYING THE FILES

file_name_final = [(wavsFileName[x] + '.wav') for x in range(len(wavsFileName))]
for i in file_name_final:
    print(i)
print('\nDone.')

for i in range(len(file_name_final)): #This is the part that renames
    shutil.move(pathFiles + '/' + _files_list[i] + '.wav', pathFiles + '/' + file_name_final[i])


##############################################

_files_list = os.listdir(pathFiles) #Re-Scan

while True:
    try:
        txtName = input('Input how you wanna call your text file. Without .txt extension.')
        if txtName == '':
            print('Error, try again.\n')
        else:
            open(txtName + '.txt', 'a').close()
            DicWrite(txtName + '.txt',_files_list)
            print('\nDone.\n')
            break
    except:
        print('Error, try again.\n')


#That's it, it works with a .csv file and .wavs









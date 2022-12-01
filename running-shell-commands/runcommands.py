import os

try:

    print('run a script')
    print('----------------------------------------------')
    print()
    print(
        '''
        [1] create a folder
        [2] display  contents of current folder 
        [3] format a drive 
        [4] restart computer 
        [5] turn off computer

        ''')
    yourchoice = input('enter your choice:')

    if(yourchoice=='1'):
        try:
            fname = input("enter a folder name:")
            os.system("mkdir %s" %(fname))
            print('command completed successfully')
        except ValueError as ve:
            print(ve)
    elif(yourchoice=='2'):
        try:
            #fname = input("enter a folder name:")
            os.system("dir")
            print('command completed successfully')
        except ValueError as ve:
            print(ve)

    
    else:
        print('other opstions coming soon')

except ValueError as ve:
    print(ve)

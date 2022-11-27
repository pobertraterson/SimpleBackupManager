import selection

print("Simple Backup Manager\nMade by Pob")
print("Please select an option.\n")
print("1. Select a drive/folder to backup to")
print("2. Select files to backup & backup")
print("3. Update current backup")
print("4. Create new backup with current files\n")
while True:
    option=input(": ")
    if option=='1':
        selection.driveSelection()
    elif option=='2':
        print("Option 2")
    elif option=='3':
        print("Option 3")
    elif option=='4':
        print("Option 4")
    else:
        print("You have not selected a valid option...")
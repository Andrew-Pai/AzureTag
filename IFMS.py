import pyautogui, time, sys, os

Error = open("Error.txt","w")
Success= open("Success.txt","w")
Asset =[]
Room = {}
EquipmentField =();
RoomField =();
SortField = ();
counter=0;

print("Welcome to my automatic IFMS updater")
print("Included should be 2 CSV files: A Location file and an Asset file")
print("The location file should have the location of the user(2D-100) in column 1, and the name in column 2")
print("The asset file should have the asset number(AV01963) in column 1 and location of the asset(2D-100) in column 2")
print("\nPlease open IFMS and navigate to the Update Item page")

#user_input = input("\nWhat is the directory of the Location file?:")
user_input = "Location.csv"
if(os.path.isfile(user_input)):
    Location = open(user_input,"r")
    Location.readline()
    #user associated with room
    for line in Location.readlines():
        temp = line.split(',')
        Room[temp[0]]=temp[1][:-1]
else:
    print("File not found")
    sys.exit()

#user_input = input("\nWhat is the directory of the Asset file?:")
user_input="Items.csv"
if(os.path.isfile(user_input)):
    Item = open(user_input,"r")
    Item.readline()
    #asset # with associated room
    for line in Item.readlines():
        temp = line.split(',')
        Asset.append([[temp[0]],[temp[1][:-1]]])

else:
    print("File not found")
    sys.exit()

print("DO NOT TOUCH THE KEYBOARD OR MOUSE WHILE PROGRAM IS RUNNING")


for i, Code in enumerate(Asset):
    try:
        if(EquipmentField == ()):
            location = pyautogui.locateOnScreen('Equipment.PNG')
            center = pyautogui.center(location)
            EquipmentField = (center[0]+100,center[1])
        pyautogui.doubleClick(EquipmentField,button='left')
        pyautogui.hotkey('ctrl','a')
        pyautogui.typewrite(Code[0][0])
        pyautogui.typewrite(['enter'])
        time.sleep(0.15)
        im =pyautogui.screenshot()
        if(pyautogui.pixelMatchesColor(EquipmentField[0],EquipmentField[1],(234,241,246))):
            if(RoomField==()):
                location = pyautogui.locateOnScreen('Room.PNG')
                center = pyautogui.center(location)
                RoomField=(center[0]+100,center[1])
            pyautogui.hotkey('ctrl','a')
            pyautogui.typewrite(Room[Code[1][0]])
            pyautogui.doubleClick(RoomField,button='left')
            pyautogui.hotkey('ctrl','a')
            pyautogui.typewrite(Code[1][0])
            pyautogui.typewrite(['esc'])
            time.sleep(0.2)
            pyautogui.typewrite(['enter'])
            Success.write('{} {} {} {} {}{}'.format(Code[0][0],'was updated for',Room[Code[1][0]],'at',Code[1][0],'\n'))
            counter+=1
        else:
            print(Code[0][0], "Was not updated")
            Error.write('{} {}'.format(Code[0][0],'was not updated!!!\n'))
        #print (Code) #Asset number
        #print (Asset[1][i]) #Room number
        #print(Room[Asset[1][i]]) #Name of user
    except KeyError as k:
        print ("Key error: ", str(k))
        Error.write('{} {} {}{}'.format(str(k),"No user found for item:",Code[0][0],'\n'))
        pyautogui.typewrite("N/A")
        pyautogui.doubleClick(RoomField,button='left')
        pyautogui.hotkey('ctrl','a')
        pyautogui.typewrite(Code[1][0])
        pyautogui.typewrite(['esc'])
        time.sleep(0.2)
        pyautogui.typewrite(['enter'])
        Success.write('{} {} {}{}'.format(Code[0][0],'was updated for N/A at',Code[1][0],'\n'))
    except IndexError as i:
        print ("Index error: ", str(i))
    except TypeError as t:
        print("Error: Could not find IFMS window")
        print("Please open IFMS and navigate to the Update Item page")
        sys.exit()
    except KeyboardInterrupt as k:
        user_Input = input("Would you like to quit?(y/n):")
        if(user_Input == 'y'):
            sys.exit()
    except Exception as e:
        print ("other error: ", str(e))

Success.write('{} {}'.format(counter, "assets updated successfully"))

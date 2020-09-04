#------------------------------------------#
# Title: Assignment08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# KSorge-Toomey, 2020-Aug-31, added functions, CD class
# KSorge-Toomey, 2020-Sept-2, edited functions and CD class
# KSorge-Toomey, 2020-Sept-3, polished code
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        inventory:
    """
    # -- Fields -- #
    __cd_id = 0
    __cd_title = ''
    __cd_artist = ''
    
    # -- Constructor -- #
    def __init__(self, ID, title, artist):
        # --Attributes -- #
        self.cd_id = ID
        self.cd_title = title
        self.cd_artist = artist

    ## -- Properties -- #
    @property
    def cd_id(self):
        return self.__cd_id
    @property
    def cd_title(self):
        return self.__cd_title
    @property
    def cd_artist(self):
        return self.__cd_artist
    @cd_id.setter
    def cd_id(self, value):
        if str(value).isdigit():
            self.__cd_id = value
        else:
            raise Exception('You must enter a number!')
    @cd_title.setter
    def cd_title(self, value):
        self.__cd_title = value
    @cd_artist.setter
    def cd_artist(self, value):
        self.__cd_artist = value

    # -- Methods --#
    def add_to_inventory(self, lst_Inventory):
        lst_Inventory.append(self)


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)
    """

    @staticmethod
    def load_inventory(file_name, lst_Inventory):
        """Function to manage data ingestion from file to a list of CDs

        Reads the data from file identified by file_name into a
        (list of CDs) one line in the file represents one CD in list.

        Args:
            file_name (string): name of file used to read the data from
            lst_Inventory (list of CDs): list of objects that holds the data during runtime

        Returns:
            None.
        """
        lst_Inventory.clear()
        try:
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                objCD = CD(int(data[0]), data[1], data[2])
                objCD.add_to_inventory(lst_Inventory)
            objFile.close()
        except FileNotFoundError:
            print('The file could not be found')
        except EOFError:
            print('The file could not be loaded")')

    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """Function to save current entries in memory to file
        
        Args:
            file_name (string): name of file used to save data to
            lst_Inventory (list of CDs): list of onjects that holds the data during runtime
            
        Returns:
            None.
        """
        objFile = open(file_name, 'w')
        for cd in lst_Inventory:
          objFile.write('{},{},{}'.format(cd.cd_id, cd.cd_title, cd.cd_artist) + '\n')
        objFile.close()
        print('\nInventory saved to file.')


# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('\nMenu\n\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] Exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()
        return choice

    @staticmethod
    def show_inventory(lst_Inventory):
        """Displays current inventory table


        Args:
            lst_Inventory (list of CDs): list of objects that holds the data during runtime.

        Returns:
            None.

        """
        print('\n======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for objCD in lst_Inventory:
            print('{}\t{} (by:{})'.format(objCD.cd_id, objCD.cd_title, objCD.cd_artist))
        print('======================================')

    @staticmethod
    def user_entry(lst_Inventory):
        """Gets user input for CD entry
        
        Args:
            lst_Inventory (list of CDs): list of objects that hold the data during runtime
        
        Returns:
            None:
        """
        userCD_ID = input('Enter ID: ')
        userCD_TLE = input('What is the CD\'s title? ')
        userCD_ARTST = input('What is the Artist\'s name? ')
        try:
          objCD = CD(userCD_ID, userCD_TLE, userCD_ARTST)
          objCD.add_to_inventory(lst_Inventory)
        except Exception as e:
          print(e)
          
          
# -- Main Body of Script -- #

# Load data from file into a list of CD objects on script start
FileIO.load_inventory(strFileName, lstOfCDObjects)
IO.show_inventory(lstOfCDObjects)

while True: 
    # Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # Process menu selection
    # process exit first
    if strChoice == 'x':
        break
    # process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('Type \'yes\' to continue and reload from file. Otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('Reloading...')
            FileIO.load_inventory(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('Canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # process add a CD
    elif strChoice == 'a':
        # Ask user for new ID, CD Title and Artist and add to table
        IO.user_entry(lstOfCDObjects)
        # Display modified inventory to user
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # process save inventory to file
    elif strChoice == 's':
        # Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to text file? [y/n] ').strip().lower()
        # Process choice
        if strYesNo == 'y':
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            print('The file was NOT saved')
        continue  # start loop back at top.
    # catch-all should not be possible, as user choice gets vetted in IO, but to be safe:
    else:
        print('General Error')

menu = """

                              
                            Menu
 
                          
                             1 -> Phonebook
                             2 -> Messages
                             3 -> Chat
                             4 -> Call Register
                             5 -> Tones
                             6 -> Settings
                             7 -> Call Divert
                             8 -> Games
                             9 -> Calculator
                            10 -> Reminders
                            11 -> Clock
                            12 -> Profiles
                            13 -> SIM Services
"""

print(menu)
menu_page = int(input("Choose a menu option: "))

match menu_page:
    case 1:
        print("Phonebook")
        phone_book = int(input("Select Phonebook Option: "))
        match phone_book:
            case 1:
                print("Search")
            case 2:
                print("Service nos")
            case 3:
                print("Add name")
            case 4:
                print("Erase")
            case 5:
                print("Edit")
            case 6:
                print("Assign tone")
            case 7:
                print("Send b'card")
            case 8:
                print("Options")
            case 9:
                print("Speed dials")
            case 10:
                print("Voice tags")
            case _:
                print("Invalid phonebook selection")

    case 2:
        print("Messages")
        print("""
        1 -> Write messages
        2 -> Inbox
        3 -> Outbox
        4 -> Picture messages
        5 -> Templates
        6 -> Smileys
        7 -> Message settings
        8 -> Info service
        9 -> Voice mailbox number
        10 -> Service command editor
        """)

    case 3:
        print("Chat")

    case 4:
        print("Call Register")
        print("""
        1 -> Missed calls
        2 -> Received calls
        3 -> Dialled numbers
        4 -> Erase recent call lists
        5 -> Show call duration
        6 -> Show call costs
        7 -> Call cost settings
        8 -> Prepaid credit
        """)
        callRegister = int(input("Select a Call Register Option: "))
        match callRegister:
            case 1:
                print("Missed calls")
            case 2:
                print("Received calls")
            case 3:
                print("Dialled numbers")
            case 4:
                print("Erase recent call lists")
            case 5:
                print("Show call duration:")
                print("""
                1 -> Last call duration
                2 -> All calls' duration
                3 -> Received calls' duration
                4 -> Dialled calls' duration
                5 -> Clear timers
                """)
            case 6:
                print("Call costs:")
                print("""
                1 -> Last call cost
                2 -> All calls' cost
                3 -> Clear counters
                """)
            case 7:
                print("Call cost settings:")
                print("""
                1 -> Call cost limit
                2 -> Show costs in
                """)
            case 8:
                print("Prepaid credit")
            case _:
                print("Invalid selection")

    case 5:
        print("Tones")
        print("""
        1 -> Ringing Tone
        2 -> Ringing volume
        3 -> Incoming call alert
        4 -> Composer
        5 -> Message alert tones
        6 -> Keypad tones
        7 -> Warning and game tones
        8 -> Vibrating alert
        9 -> Screen saver
        """)

    case 6:
        print("Settings")
        print("""
        1 -> Call settings
        2 -> Phone settings
        3 -> Security settings
        4 -> Restore factory settings
        """)
        settings = int(input("Choose a Settings Option: "))
        match settings:
            case 1:
                print("Call settings:")
                print("""
                1 -> Automatic redial
                2 -> Speed dialling
                3 -> Call waiting options
                4 -> Own number sending
                5 -> Phone line in use
                6 -> Automatic answer
                """)
            case 2:
                print("Phone settings:")
                print("""
                1 -> Language
                2 -> Cell info display
                3 -> Welcome note
                4 -> Network selection
                5 -> Lights
                6 -> Confirm SIM service actions
                """)
            case 3:
                print("Security settings:")
                print("""
                1 -> PIN code request
                2 -> Call barring service
                3 -> Fixed dialling
                4 -> Closed user group
                5 -> Phone security
                6 -> Change access codes
                """)
            case 4:
                print("Restore factory settings")
            case _:
                print("Invalid Settings Selection")

    case 7:
        print("Call Divert")

    case 8:
        print("Games")

    case 9:
        print("Calculator")

    case 10:
        print("Reminders")

    case 11:
        print("Clock")
        print("""
        1 -> Alarm clock
        2 -> Clock settings
        3 -> Date setting
        4 -> Stopwatch
        5 -> Countdown timer
        6 -> Auto update of date and time
        """)

    case 12:
        print("Profiles")

    case 13:
        print("SIM Services")

    case _:
        print("Invalid selection")

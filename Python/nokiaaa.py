menu = """

                              
                            Menu

                          
                      i7       1 -> Phonebook
                             2 -> Messages
                             3 -> Chat
                             4 -> Call Register
                             5 -> Tones
                             6 -> Settings;
                             7 -> Call Divert
                             8 -> Games;=
                             9 -> Calculator
                            10 -> Reminders
                            11 -> Clock
                            12 -> Profiles
                            13 -> SIM Services
"""
print(menu)
menu_page = int(input("Choose a menu option: "))

match menu_page:  
	case 1 : 
		print("Phonebook")
	case 2 : 
		print("Messages")
	case 3 : 
		print("Chat")
	case 4 : 
		print("Tones")
	case 5 :
		print("Settings")
	case 6 : 
		print("Call Divert")
	case 7 : 
		print("Games")
	case 8 : 
		print("Calculator")
	case 9 :
		print("Reminders")
	case 10 :
		print("Clock")
	case 11 :
		print("Profiles")
	case 12 :
		print("SIM Services")
	case _ : 
		print(" ")
		match phone_book:
			case 1 : 
				print("""
	                        	Phonebook Menu:
	                        	1 -> Search
	                        	2 -> Service nos
	                        	3 -> Add name
	                        	4 -> Erase
	                        	5 -> Edit
	                        	6 -> Assign tone
	                        	7 -> Send b'card
	                        	8 -> Options
	                        	9 -> Speed dials
	                        	10 -> Voice tags
	                       	 """)


































                
case 3: 
	print("Chat")

case 4: 
	print("""
                        Call Register:
                        1 -> Missed calls
                        2 -> Received calls
                        3 -> Dialled numbers
                        4 -> Erase recent call lists
                        5 -> Show call duration
                        6 -> Show call costs
                        7 -> Call cost settings
                        8 -> Prepaid credit
                        """)
                
                match (callRegister):
                	case 1 : 
                		print("Missed calls")
                	case 2 :
                		print("Received calls")
                	case 3 :
                		print("Dialled numbers")
                	case 4 :
                		print("Erase recent call lists")
                	case 5 :
                		print("Show call duration:")
                		print("""
                		1 -> Last call duration
                                2 -> All calls' duration
                                3 -> Received calls' duration
                                4 -> Dialled calls'
                                5 -> Clear timers
                                """)
                                
 		case 6 :
 			print("Show call costs:")
 			print("""
 			1 -> Last call costs
                               2 -> All calls' cost
                               3 -> Clear counters
                                """)
		case 7 :
			print("Call cost settings:")
			print("""
			1 -> Call cost limit
                                2 -> Show costs in
                                """)
 		case 8 :
 			print("Prepaid credit")
 		case _ :
 			print("Invalid selection")

               
          
                    

case 5: 
	print("""
                        Tones:
                        1 -> Ringing Tone
                        2 -> Ringing volume
                        3 -> Incoming call alert
                        4 -> Composer
                        5 -> Message alert tones
                        6 -> Keypad tones
                        7 -> Warning and game tones
                        8 -> Vibrating alert
                        9 -> Screen saver
                        """);
          
case 6:
	print("""
                        Settings:
                        1 -> Call settings
                        2 -> Phone settings
                        3 -> Security settings
                        4 -> Restore factory settings
                        """)
                        switch (settings)
                        	case 1 :
                        		print("Call settings:") 
                        		print("""
	                             1 -> Automatic redial
	                             2 -> Speed dialling
	                             3 -> Call waiting options
	                             4 -> Own number sending
	                             5 -> Phone line in use
	                             6 -> Automatic answer
	                                """)
			case 2 :
				print("Phone settings:")
				print("""
				1 -> Language
                                 	2 -> Cell info display
                                	3 -> Welcome note
                                	4 -> Network selection
                                	5 -> Lights
                                	6 -> Confirm SIM service actions
                                	""") 
			case 3 :
                                	print("Security settings:")
                                	print("""
	                             1 -> PIN code request
	                             2 -> Call barring service
	                             3 -> Fixed dialling
	                             4 -> Closed user group
	                             5 -> Phone security
	                             6 -> Change access codes
	                                """)
			case 4 :
				print("Restore factory settings")
			case _ :
				

			


                       

                         
                                         
                   
                        
                    
                    
                   
                    case 4 -> print("Restore factory settings")
                    default -> print("Invalid Settings Option")
                }
                break;

            case 7: System.out.println("Call divert"); break;
            case 8: System.out.println("Games"); break;
            case 9: System.out.println("Calculator"); break;
            case 10: System.out.println("Reminders"); break;
            case 11: System.out.println("""
                        Clock:
                        1 -> Alarm clock
                        2 -> Clock settings
                        3 -> Date setting
                        4 -> Stopwatch

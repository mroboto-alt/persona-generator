import secrets, os, sys, random, time
import sqlite3 as sql
import pandas as pd
from pcodes import *
from names import *
from cities import * 

''' this program generates dummy personal information based on the most common or common names
    in 6 different count1ries or lingustic regions and dummy personal data for online purchases
    not requiring a real mailing address based on addresses in Toronto '''

def main():


    def password():

        master_pass = []

        alpha = 'abcdefghijklmnopqrstuvwxyz'
        upper = alpha.upper()
        special = ('!','@')

        numbers = []
        [numbers.append(str(random.randint(0,5))) for i in range(2)]

        switch = random.randint(1,2)

        for i in range(switch):
            for i in (alpha, upper, special, numbers):
                master_pass.append(secrets.choice(i))

        random.shuffle(master_pass)

        master_pass = ''.join(master_pass)

        print('\n===========================================')
        print('                 PASSWORD                    ')
        print('===========================================\n')
        print(f' {master_pass}                              ')
        print('\n===========================================')

        return master_pass


    def random_selection():

        state = ( (amr_fname, amr_lname), (ger_fname, ger_lname), (fra_fname, fra_lname), (ind_fname, ind_lname),
                    (span_fname, span_lname), (rus_fname, rus_lname) )

        national_name = random.choice(state)
        fname, lname = national_name   

        fname = random.choice(fname)
        lname = secrets.choice(lname)    
        full_name = fname + ' ' + lname
        full_name = full_name.lower()

        # CITY

        if amr_fname in national_name:
            city = secrets.choice(city1m)
            country = ', usa'

        elif ger_fname in national_name:
            city = secrets.choice(ger_city)
            country = ', germany'

        elif fra_fname in national_name:
            city = secrets.choice(fra_city)
            country = ', france'

        elif ind_fname in national_name:
            city = secrets.choice(ind_city)
            country = ', india'
        
        elif span_fname in national_name:
            city = secrets.choice(span_city)
            country = ', spain/americas'

        else:
            city = secrets.choice(rus_city)
            country = ', russia'
            if fname in wmn:
                lname = lname + 'a'
                full_name = fname + ' ' + lname

        city = city + country
        city = city.lower()

        # GENDER

        if fname in wmn:
            gender = 'female'

        else:
            gender = 'male'

        # AGE

        age = random.randint(18,75)

        time.sleep(0.25)
        os.system('clear')
        
        print('\n===========================================')
        print(f' NAME: {full_name}   ')
        print(f' GENDER: {gender}        ')
        print(f' AGE: {age}              ')
        print(f' CITY: {city}            ')
        print('===========================================')

        email = input('\nPlease enter email: ')
        site = input('Please enter site: ')
        vpn = input('Enter vpn if used: ')
        passwd = input('Generate a password [y/n]? ')

        db = sql.connect('profiles.db')
        db.execute(''' CREATE TABLE IF NOT EXISTS profile_db 
                            (
                            pid INTEGER PRIMARY KEY AUTOINCREMENT,
                            full_name VARCHAR(50),
                            gender VARCHAR(10),
                            age INTEGER,
                            city  VARCHAR(50),
                            email VARCHAR(50),
                            site VARCHAR(50),
                            pass VARCHAR(25),
                            vpn VARCHAR(25)
                            ); ''')
                            
        if passwd.lower() in ('y','yes','yeah'):
            master_pass = password()
            db.execute('INSERT INTO profile_db VALUES(NULL,?,?,?,?,?,?,?,?)', (full_name, gender, age, city, email, site, master_pass, vpn) )
        
        else:
            db.execute('INSERT INTO profile_db VALUES(NULL,?,?,?,?,?,?,?,?)', (full_name, gender, age, city, email, site, None, None) )
        
        verify = input('\nDo you want to save [y/n]? ')

        if verify.lower() in ('y','yes','yeah'):
            db.commit()
        
        db.close()

        choice_prompt = int(input('\n\n[0] exit [1] main menu: ') )

        if choice_prompt == 1:
            main()

        elif choice_prompt == 0:
            os.system('clear')
            sys.exit(0)


    def manual_selection(nation_prompt):
  
        if nation_prompt == 0:
            fname, lname = (amr_fname, amr_lname)
            city = secrets.choice(city1m)
            country = ', usa'

        elif nation_prompt == 1:
            fname, lname = (ger_fname, ger_lname)
            city = secrets.choice(ger_city)
            country = ', germany'

        elif nation_prompt == 2:
            fname, lname = (fra_fname, fra_lname)
            city = secrets.choice(fra_city)
            country = ', france'
        
        elif nation_prompt == 3:
            fname, lname = (ind_fname, ind_lname)
            city = secrets.choice(ind_city)
            country = ', india'

        elif nation_prompt == 4:
            fname, lname = (span_fname, span_lname)
            city = secrets.choice(span_city)
            country = ', spain/americas'  

        elif nation_prompt == 5:
            fname, lname = (rus_fname, rus_lname)
            city = secrets.choice(rus_city)
            country = ', russia' 

        fname = random.choice(fname)
        lname = secrets.choice(lname)    
        full_name = fname + ' ' + lname
        full_name = full_name.lower()

        if fname in wmn and nation_prompt == 5:
            lname = lname + 'a'
            full_name = fname + ' ' + lname               

        # CITY

        city = city + country
        city = city.lower()

        # GENDER

        if fname in wmn:
            gender = 'female'

        else:
            gender = 'male'

        # AGE

        age = random.randint(18,75)

        time.sleep(0.25)
        os.system('clear')
        
        print('\n===========================================')
        print(f' NAME: {full_name}   ')
        print(f' GENDER: {gender}        ')
        print(f' AGE: {age}              ')
        print(f' CITY: {city}            ')
        print('===========================================')

        email = input('\nPlease enter email: ')
        site = input('Please enter site: ')
        vpn = input('Enter vpn if used: ')
        passwd = input('Generate a password [y/n]? ')

        db = sql.connect('profiles.db')
        db.execute(''' CREATE TABLE IF NOT EXISTS profile_db 
                            (
                            pid INTEGER PRIMARY KEY AUTOINCREMENT,
                            full_name VARCHAR(50),
                            gender VARCHAR(10),
                            age INTEGER,
                            city  VARCHAR(50),
                            email VARCHAR(50),
                            site VARCHAR(50),
                            pass VARCHAR(25),
                            vpn VARCHAR(25)
                            ); ''')

        if passwd.lower() in ('y','yes','yeah'):
            master_pass = password()
            db.execute('INSERT INTO profile_db VALUES(NULL,?,?,?,?,?,?,?,?)', (full_name, gender, age, city, email, site, master_pass, vpn) )
        
        else:
            db.execute('INSERT INTO profile_db VALUES(NULL,?,?,?,?,?,?,?,?)', (full_name, gender, age, city, email, site, None, vpn) )


        verify = input('\nDo you want to save [y/n]? ')

        if verify.lower() in ('y','yes','yeah'):
            db.commit()
        
        db.close()


        choice_prompt = int(input('\n\n[0] exit [1] main menu: ') )

        if choice_prompt == 1:
            main()

        elif choice_prompt == 0:
            os.system('clear')
            sys.exit(0)



    def celebrity():

        full_name = random.choice(amr_celebs)             

        # CITY

        city = ('los angeles', 'new york')
        city = random.choice(city)

        # GENDER

        if full_name in ('betty white','julia roberts','taylor swift','megan fox','jenn lawrence','jenn garner'):
            gender = 'female'

        else:
            gender = 'male'

        # AGE

        age = random.randint(18,75)

        time.sleep(0.25)
        os.system('clear')
        
        print('\n===========================================')
        print(f' NAME: {full_name}   ')
        print(f' GENDER: {gender}        ')
        print(f' AGE: {age}              ')
        print(f' CITY: {city}            ')
        print('===========================================')

        email = input('\nPlease enter email: ')
        site = input('Please enter site: ')
        vpn = input('Enter vpn if used: ')
        passwd = input('Generate a password [y/n]? ')

        db = sql.connect('profiles.db')
        db.execute(''' CREATE TABLE IF NOT EXISTS profile_db 
                            (
                            pid INTEGER PRIMARY KEY AUTOINCREMENT,
                            full_name VARCHAR(50),
                            gender VARCHAR(10),
                            age INTEGER,
                            city  VARCHAR(50),
                            email VARCHAR(50),
                            site VARCHAR(50),
                            pass VARCHAR(25),
                            VPN varchar(25)
                            ); ''')

        if passwd.lower() in ('y','yes','yeah'):
            master_pass = password()
            db.execute('INSERT INTO profile_db VALUES(NULL,?,?,?,?,?,?,?,?)', (full_name, gender, age, city, email, site, master_pass, vpn) )
        
        else:
            db.execute('INSERT INTO profile_db VALUES(NULL,?,?,?,?,?,?,?,?)', (full_name, gender, age, city, email, site, None, vpn) )


        verify = input('\nDo you want to save [y/n]? ')

        if verify.lower() in ('y','yes','yeah'):
            db.commit()
        
        db.close()

        choice_prompt = int(input('\n\n[0] exit [1] main menu: ') )

        if choice_prompt == 1:
            main()

        elif choice_prompt == 0:
            os.system('clear')
            sys.exit(0)
    

    # MAIN MENU

    os.system('clear')
    print('\n============ PERSONA  GENERATOR ============')
    print('                                            ')
    print('+------------------------------------------+') 
    print('| [0]  Exit                                |')
    print('+------------------------------------------+')
    print('| [1]  Profile Info (US/GER/FRA/IND...)    |')
    print('|      (name, city, age)                   |')
    print('+------------------------------------------+')
    print('| [2]  Payment Info (CAN)                  |')
    print('|      (name, postal code, phone)          |')
    print('+------------------------------------------+')
    print('| [3]  Display profiles                    |')
    print('+------------------------------------------+')

    try: 
        init_choice = int(input('\nEnter choice (0-3): '))

    except ValueError:
        print('\nERROR: Enter a number between 0-3')
        time.sleep(1)
        os.system('clear')
        main()



    if init_choice == 0:

        os.system('clear')
        sys.exit(0)



    elif init_choice == 1:

        os.system('clear')
        print('\n============== NAME OPTIONS ===============')
        print('                                           ')
        print('+-----------------------------------------+') 
        print('| [0]  Manually select nationality        |')
        print('+-----------------------------------------+')
        print('| [1]  Randomly select nationality        |')
        print('+-----------------------------------------+')
        print('| [2]  American celebrity name            |')
        print('+-----------------------------------------+')
        print('| [3]  Main menu                          |')
        print('+-----------------------------------------+')


        state_select = int(input('\nEnter choice (0-2): '))


        if state_select == 0:
             
            os.system('clear')
            print('\n================ OPTIONS ==================')
            print('                                           ')
            print('+-----------------------------------------+') 
            print('| [0]  American                           |')
            print('+-----------------------------------------+')
            print('| [1]  German                             |')
            print('+-----------------------------------------+')
            print('| [2]  French                             |')
            print('+-----------------------------------------+')
            print('| [3]  Indian                             |')
            print('+-----------------------------------------+')
            print('| [4]  Hispanic (Spanish, Mexican, etc.)  |')
            print('+-----------------------------------------+')
            print('| [5]  Russian                            |')
            print('+-----------------------------------------+')
            print('| [6]  Main menu                          |')
            print('+-----------------------------------------+')

            nation_prompt = int(input('\nEnter choice (0-6): '))

            if nation_prompt in (0,1,2,3,4,5):
                manual_selection(nation_prompt)

            elif nation_prompt == 6:
                main()

        elif state_select == 1:
            random_selection()

        elif state_select == 2:
            celebrity()

        elif state_select == 3:
            main()

        
    elif init_choice == 2:


        def pay_menu():

            global phone_prompt

            os.system('clear')
            print('\n================ OPTIONS ==================')
            print('                                           ')
            print('+-----------------------------------------+') 
            print('| [0]  High frequency phone number        |')
            print('+-----------------------------------------+')
            print('| [1]  Random phone number                |')
            print('+-----------------------------------------+')

            try:
                phone_prompt = int(input('\nEnter choice (0-1): '))

            except:
                print('\nERROR: Choose 1 or 2')
                time.sleep(1.25)
                os.system('clear')
                pay_menu()

        pay_menu()


        if phone_prompt == 0:


            common_numbers = { 
                            1: ('Pizza Pizza','416-967-1111','M5J 2Y5'),
                            2: ('Toronto District School Board','416-397-3000','M2N 5N8'),
                            3: ('Toronto City Hall','416-392-2489','M5H 2N2'),
                            4: ('Mississauga City Hall','905-615-4311','L5B 3C1'),
                            5: ('Brampton City Hall','905-874-2000','L6Y 4R2'),
                            6: ('University of Toronto','416-978-2011','M5S 1A1'),
                            7: ('University/Bloor McDonalds','416-964-1583','M5S 1T8'),
                            8: ('Eaton Centre Apple store','647-258-0801','M5B 2H1'),
                            9: ('Pearson Airport','416-247-7678','L5P 1B2'),
                            10: ('TTC customer service','416-393-3030','M4S 1Z2'),
                            11: ('TTC customer information','416-393-4636','M4S 1Z2'),
                            12: ('GO Transit contact centre','416-869-3200','M5J 2W3'),
                            13: ('Yorkdale mall','416-789-3261','M6A 2T9'),
                            14: ('Square One mall','905-270-7771','L5B 2C9'),
                            15: ('Yonge/Bloor Chick-fil-A','365-601-0015','M4Y 2B6') 
                            }

            os.system('clear')
            print('\n================ NUMBERS ==================')
            print('                                           ')
            print('+-----------------------------------------+') 
            print(f'| [1]  {common_numbers[1][0]}                        |')
            print('+-----------------------------------------+')
            print(f'| [2]  {common_numbers[2][0]}      |')
            print('+-----------------------------------------+')
            print(f'| [3]  {common_numbers[3][0]}                  |')
            print('+-----------------------------------------+')
            print(f'| [4]  {common_numbers[4][0]}              |')
            print('+-----------------------------------------+')
            print(f'| [5]  {common_numbers[5][0]}                 |')
            print('+-----------------------------------------+')
            print(f'| [6]  {common_numbers[6][0]}              |')
            print('+-----------------------------------------+')
            print(f'| [7]  {common_numbers[7][0]}         |')
            print('+-----------------------------------------+')
            print(f'| [8]  {common_numbers[8][0]}           |')
            print('+-----------------------------------------+')
            print(f'| [9]  {common_numbers[9][0]}                    |')
            print('+-----------------------------------------+')
            print(f'| [10] {common_numbers[10][0]}               |')
            print('+-----------------------------------------+')
            print(f'| [11] {common_numbers[11][0]}           |')
            print('+-----------------------------------------+')
            print(f'| [12] {common_numbers[12][0]}          |')
            print('+-----------------------------------------+')
            print(f'| [13] {common_numbers[13][0]}                      |')
            print('+-----------------------------------------+')
            print(f'| [14] {common_numbers[14][0]}                    |')
            print('+-----------------------------------------+')
            print(f'| [15] {common_numbers[15][0]}            |')
            print('+-----------------------------------------+')
            
            try:
                index = int(input('\nEnter a choice (1-15): ')) 

            except ValueError:
                print('\nERROR: Enter a number between 1-15')
                time.sleep(1.25)
                os.system('clear')
                pay_menu()

            phone_num = common_numbers[index][1]


        elif phone_prompt == 1:

            # PHONE

            acode = ('416','647','437','905','289','365')
            acode = random.choice(acode)
            digits0 = str(random.randint(100,999))
            digits1 = str(random.randint(1000,9999))
            phone_num = acode + '-' + digits0 + '-' + digits1
        
        # NAME

        fname = random.choice(amr_fname)
        lname = secrets.choice(amr_lname)
        name = fname + ' ' + lname

        # POSTAL CODE

        if phone_prompt == 0:
            pcode = common_numbers[index][2]

        elif phone_prompt == 1:
            pcode = random.choice(codes)

        time.sleep(0.25)
        os.system('clear')
        
        print('\n===========================================')
        print(f'FULL NAME: {name}')
        print(f'POSTAL CODE: {pcode}')
        print(f'PHONE NUMBER: {phone_num}')
        print('===========================================\n')

        purchase = input('Purchase made: ')
        pay_meth = input('Purchase method: ')

        if phone_prompt == 0:
            location = common_numbers[index][0]

            db = sql.connect('profiles.db')
            db.execute('''CREATE TABLE IF NOT EXISTS payment 
                                    (
                                    pid INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT,
                                    pcode TEXT,
                                    location TEXT,
                                    phone TEXT,
                                    purchase TEXT,
                                    pay_meth TEXT
                                    ); ''')
            
            db.execute('''INSERT INTO payment VALUES(NULL,?,?,?,?,?,?);''', (name, pcode, location, phone_num, purchase, pay_meth) )

        elif phone_prompt == 1:
            db = sql.connect('profiles.db')
            db.execute('''CREATE TABLE IF NOT EXISTS payment 
                                    (
                                    pid INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT,
                                    pcode TEXT,
                                    location TEXT,
                                    phone TEXT,
                                    purchase TEXT,
                                    pay_meth TEXT
                                    ); ''')
            
            db.execute('''INSERT INTO payment VALUES(NULL,?,?,?,?,?,?);''', (name, pcode, None, phone_num, purchase, pay_meth) )


        verify = input('\nDo you want to save [y/n]? ')

        if verify.lower() in ('y','yes','yeah'):
            db.commit()

        db.close()

        choice_prompt = int(input('\n\n[0] exit [1] main menu: ') )

        if choice_prompt == 1:
            main()

        elif choice_prompt == 0:
            os.system('clear')
            sys.exit(0)



    else:

        def db_lookup():

            os.system('clear')
            print('=========== TABLES ===========')
            print('                              ')
            print('+----------------------------+')
            print('|     [1] Profile table      |')
            print('+----------------------------+')
            print('|     [2] Payment table      |')
            print('+----------------------------+')
            print('|     [3] Main menu          |')
            print('+----------------------------+')

            try:
                table_prompt = int(input('\nEnter choice (1-3): '))

            except ValueError:
                print('\nERROR: Enter a number between 1-3')
                time.sleep(1.25)
                os.system('clear')
                db_lookup()

            os.system('echo')
            time.sleep(0.25)
            os.system('clear')

            if table_prompt == 1:
                try: 
                    db = sql.connect('profiles.db')
                    query = pd.read_sql_query('SELECT * FROM profile_db;', db)
                    print(query)
                    db.close()
                except:
                    print('\nERROR: Table does not exit')
                    time.sleep(1.75)
                    os.system('clear')
                    main()

            elif table_prompt == 2:
                try:
                    db = sql.connect('profiles.db')
                    query = pd.read_sql_query('SELECT * FROM payment;', db)
                    print(query)
                    db.close()
                except:
                    print('\nERROR: Table does not exist')
                    time.sleep(1.75)
                    os.system('clear')
                    main()
            else:
                main()

            choice_prompt = int(input('\n\n[0] exit [1] main menu ') )

            if choice_prompt == 1:
                main()

            elif choice_prompt == 0:
                os.system('clear')
                sys.exit(0)
        
        db_lookup()

main()

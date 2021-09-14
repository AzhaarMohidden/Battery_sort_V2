#  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.
# | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
# | |   ______     | || |      __      | || |  _________   | || |  _________   | || |  _________   | || |  _______     | || |  ____  ____  | |
# | |  |_   _ \    | || |     /  \     | || | |  _   _  |  | || | |  _   _  |  | || | |_   ___  |  | || | |_   __ \    | || | |_  _||_  _| | |
# | |    | |_) |   | || |    / /\ \    | || | |_/ | | \_|  | || | |_/ | | \_|  | || |   | |_  \_|  | || |   | |__) |   | || |   \ \  / /   | |
# | |    |  __'.   | || |   / ____ \   | || |     | |      | || |     | |      | || |   |  _|  _   | || |   |  __ /    | || |    \ \/ /    | |
# | |   _| |__) |  | || | _/ /    \ \_ | || |    _| |_     | || |    _| |_     | || |  _| |___/ |  | || |  _| |  \ \_  | || |    _|  |_    | |
# | |  |_______/   | || ||____|  |____|| || |   |_____|    | || |   |_____|    | || | |_________|  | || | |____| |___| | || |   |______|   | |
# | |              | || |              | || |              | || |              | || |              | || |              | || |              | |
# | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
#  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'
#  .----------------.  .----------------.  .----------------.  .----------------.
# | .--------------. || .--------------. || .--------------. || .--------------. |
# | |    _______   | || |     ____     | || |  _______     | || |  _________   | |
# | |   /  ___  |  | || |   .'    `.   | || | |_   __ \    | || | |  _   _  |  | |
# | |  |  (__ \_|  | || |  /  .--.  \  | || |   | |__) |   | || | |_/ | | \_|  | |
# | |   '.___`-.   | || |  | |    | |  | || |   |  __ /    | || |     | |      | |
# | |  |`\____) |  | || |  \  `--'  /  | || |  _| |  \ \_  | || |    _| |_     | |
# | |  |_______.'  | || |   `.____.'   | || | |____| |___| | || |   |_____|    | |
# | |              | || |              | || |              | || |              | |
# | '--------------' || '--------------' || '--------------' || '--------------' |
#  '----------------'  '----------------'  '----------------'  '----------------'
#  .----------------.  .----------------.  .----------------.  .----------------.
# | .--------------. || .--------------. || .--------------. || .--------------. |
# | |  _______     | || |   ______     | || |      __      | || |  _________   | |
# | | |_   __ \    | || |  |_   _ \    | || |     /  \     | || | |  _   _  |  | |
# | |   | |__) |   | || |    | |_) |   | || |    / /\ \    | || | |_/ | | \_|  | |
# | |   |  __ /    | || |    |  __'.   | || |   / ____ \   | || |     | |      | |
# | |  _| |  \ \_  | || |   _| |__) |  | || | _/ /    \ \_ | || |    _| |_     | |
# | | |____| |___| | || |  |_______/   | || ||____|  |____|| || |   |_____|    | |
# | |              | || |              | || |              | || |              | |
# | '--------------' || '--------------' || '--------------' || '--------------' |
#  '----------------'  '----------------'  '----------------'  '----------------'
# repo: https://github.com/AzhaarMohidden/Battery_sort_V2.git
# date: 31.03.2021
# Prereq:
#     1. xlxswriter
#     2. pandas


import database as db
import ascii_boards as ab
import os
import time
from tqdm import tqdm
from datetime import datetime
from reader import Log_reader as lg_r
from Max_Error import Write_error as ME
# import open2

now = datetime.now()


if __name__ == '__main__':
    db.rem_tech4()
    db.get_serial()
    db.printer_ins()
    os.system("cls")
    ab.battery_sort()
    v = input("Press any key to continue..")
    os.system("cls")
    ab.battery_sort()

    while(1):
        ans = 0
        print("1. Show Current Arrangment.")
        print("2. Show Current Arrangment and Sorted Arrangments")
        print("3. Read Battery info.")
        print("4. Visual Read (Beta)")
        print("5. Exit Programe")
        p = str(input("Please Select one of the above: "))
        if (p == "1" or p == "2" or p == "3" or p == "4" or p == "5"):
            ans = int(p)
            print("Selected: "+ str(ans))
        if (ans == 1):
            os.system("cls")
            ab.battery_sort()
            db.current_arrangement_print()
            print("")
            print("DONE.")
            print("")
            print("")
            inserted_batteries_sorted = db.sorted_arrangement_print(0)
            db.sorted_arrangement_print(0)
            while(1):
                inserted_batteries_sorted = db.sorted_arrangement_print(0)
                ans3 = str(input("Show Range selection? (Y/N): "))
                if (ans3 == "y" or ans3 == "Y" or ans3 == "yes" or ans3 == "YES"):
                    os.system("cls")
                    ab.battery_sort()
                    up_lim = int(input("Please enter Upper Limit of SOC: "))
                    down_lim = int(input("Please enter Lower Limit of SOC: "))
                    db.range_print(up_lim, down_lim)
                    db.get_serial()
                    db.printer_ins()
                    db.current_arrangement_print(0)
                    break
                elif (ans3 == "n" or ans3 == "N" or ans3 == "no" or ans3 == "NO"):
                    print("")
                    os.system("cls")
                    ab.battery_sort()
                    break
                else:
                    print("Invalid selection..")

        elif (ans == 2):
            os.system("cls")
            ab.battery_sort()
            db.current_arrangement_print()
            print("")
            print("")
            print("")
            inserted_batteries_sorted = db.sorted_arrangement_print(1)
            print("")
            db.total_batteries(inserted_batteries_sorted)
            print("")
            print("DONE.")
            print("")
            print("")
            v = input("Press any key when sorting completed..")
            while(1):
                ans2 = str(input("Make Excel Files? (Y/N): "))
                if (ans2 == "y" or ans2 == "Y" or ans2 == "yes" or ans2 == "YES"):
                    os.system("cls")
                    ab.battery_sort()
                    inserted_batteries_sorted = db.sorted_arrangement_print(1)
                    db.position_print(inserted_batteries_sorted)
                    print("")
                    print("Created Excel File:- Positions..")
                    data = db.search()
                    date_time = now.strftime("%Y%m%d-%H.%M.%S")
                    ME.write_text_file(date_time, data)
                    print("Created Excel File:- Outputs..")
                    print("\n")
                    print("\n")
                    c = input("Press any key to go back..")
                    os.system("cls")
                    ab.battery_sort()
                    break
                elif (ans2 == "n" or ans2 == "N" or ans2 == "no" or ans2 == "NO"):
                    print("")
                    c = input("Press any key to go back..")
                    os.system("cls")
                    ab.battery_sort()
                    break
                else:
                    print("Invalid selection..")

        elif (ans == 5):
            print("Exiting Application")
            time.sleep(0.3)
            print("Saving and Closing")
            print("")
            with tqdm(total = 100) as pbar:
                for up in range(100):
                    time.sleep(0.01)
                    pbar.update(1)
            print("Done")
            print("")
            exit()
        elif (ans ==3):
            os.system("cls")
            ab.battery_sort()
            lg_r.info_read()
            print("")
            print("")
        elif (ans == 4):

            os.system("cls")
            os.system("python open2.py")
            # ab.battery_sort()
            # lg_r.info_read()
            # print("")
            # print("")
        else:
            print("Invalid Selection..")
            print("")
            print("")



    # db.current_arrangement_print()

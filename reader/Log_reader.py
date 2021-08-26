import os
import sys
# log_file = fn.list_dir(r'E:\Python\reader\Batterieverzeichnis')
# fname = "E://Python/reader/Batterieverzeichnis/009768.txt"

cwd = os.getcwd()

def f_select():
    serial = str(input("Please input the Battery serial (e.g:- 456) :- "))
    file = str(cwd) +"/reader/Batterieverzeichnis/009" + serial + ".txt"
    # file = "C://Azhaar_Data/Python/reader/Batterieverzeichnis/009" + serial + ".txt"
    return serial

def f_select_vis(serials):
    serial = str(serials)
    file = str(cwd) +"/reader/Batterieverzeichnis/009" + serial + ".txt"
    # file = "C://Azhaar_Data/Python/reader/Batterieverzeichnis/009" + serial + ".txt"
    return serial

def read_text(fname, directory_file ):
    # fullname= "C://Azhaar_Data/Python/reader/"+ directory_file + "/009" + fname + ".txt"
    fullname= str(cwd)+"/reader/"+ directory_file + "/009" + fname + ".txt"
    l = open(fullname, encoding="utf-8")
    file_array = l.read().split('\n')
    # print(file_array)
    # for i in file_array:
    #     print(str(file_array.index(i)) + "  " + i)
    File_length = str(len(file_array))
    prevline = len(file_array) - 3
    # legends = 0
    lastline = len(file_array) - 2

    # print(te[sm])
    prev_data = file_array[prevline].split(';')
    # leg_data = file_array[legends].split(';')
    last_data = file_array[lastline].split(';')
    for ll in range(len(last_data)):
        if (last_data[ll] == ""):
            last_data[ll] = "0"
    for ll in range(len(prev_data)):
        if (prev_data[ll] == ""):
            prev_data[ll] = "0"
    Bat_Serial = last_data[0]
    LastOperation =  prev_data[3] + " - " + last_data[3]
    LastOperationOn = last_data[1] + " @ " + last_data[2]
    MAX_Error = last_data[19] + "%"
    if(last_data[13] == ''):
        last_data[13] = "0"
    SOC = last_data[13]
    SOH = last_data[14] + "%"
    last_charge_unit = last_data[25]
    last_charge_position = last_data[26]
    # print("Raw Data********************************************")
    # for m in range(len(last_data)):
    #     print(str(m)+ " :- " + last_data[m])
    # # print(last_data)011
    # print("Raw Data********************************************")
    return Bat_Serial, LastOperation, LastOperationOn, MAX_Error, SOC, SOH, last_charge_unit, last_charge_position, File_length
def read_text1(fname, directory_file = "Batterieverzeichnis_new" ):
    fullname= str(cwd)+"/reader/"+ directory_file + "/009" + fname + ".txt"
    l = open(fullname, encoding="utf-8")
    file_array = l.read().split('\n')
    # print(file_array)
    # for i in file_array:
    #     print(str(file_array.index(i)) + "  " + i)
    File_length = str(len(file_array))
    prevline = len(file_array) - 3
    # legends = 0
    lastline = len(file_array) - 2

    # print(te[sm])
    prev_data = file_array[prevline].split(';')
    # leg_data = file_array[legends].split(';')
    last_data = file_array[lastline].split(';')
    for ll in range(len(last_data)):
        if (last_data[ll] == ""):
            last_data[ll] = "0"
    for ll in range(len(prev_data)):
        if (prev_data[ll] == ""):
            prev_data[ll] = "0"
    Bat_Serial = last_data[0]
    LastOperation =  prev_data[3] + " - " + last_data[3]
    LastOperationOn = last_data[1] + " @ " + last_data[2]
    MAX_Error = last_data[19] + "%"
    if(last_data[13] == ''):
        last_data[13] = "0"
    SOC = last_data[13]
    SOH = last_data[14] + "%"
    last_charge_unit = last_data[25]
    last_charge_position = last_data[26]
    # print("Raw Data********************************************")
    # for m in range(len(last_data)):
    #     print(str(m)+ " :- " + last_data[m])
    # # print(last_data)011
    # print("Raw Data********************************************")
    return Bat_Serial, LastOperation, LastOperationOn, MAX_Error, SOC, SOH, last_charge_unit, last_charge_position, File_length
def read_text1_vis(fname, directory_file = "Batterieverzeichnis_new" ):
    fullname= str(cwd)+"/reader/"+ directory_file + "/009" + fname + ".txt"
    l = open(fullname, encoding="utf-8")
    file_array = l.read().split('\n')
    # print(file_array)
    # for i in file_array:
    #     print(str(file_array.index(i)) + "  " + i)
    File_length = str(len(file_array))
    prevline = len(file_array) - 3
    # legends = 0
    lastline = len(file_array) - 2

    # print(te[sm])
    prev_data = file_array[prevline].split(';')
    # leg_data = file_array[legends].split(';')
    last_data = file_array[lastline].split(';')
    for ll in range(len(last_data)):
        if (last_data[ll] == ""):
            last_data[ll] = "0"
    for ll in range(len(prev_data)):
        if (prev_data[ll] == ""):
            prev_data[ll] = "0"
    Bat_Serial = last_data[0]
    # LastOperation =  prev_data[3] + " - " + last_data[3]
    # LastOperationOn = last_data[1] + " @ " + last_data[2]
    # MAX_Error = last_data[19] + "%"
    if(last_data[13] == ''):
        last_data[13] = "0"
    SOC = last_data[13]
    # SOH = last_data[14] + "%"
    # last_charge_unit = last_data[25]
    # last_charge_position = last_data[26]
    # print("Raw Data********************************************")
    # for m in range(len(last_data)):
    #     print(str(m)+ " :- " + last_data[m])
    # # print(last_data)011
    # print("Raw Data********************************************")
    return Bat_Serial, SOC
    # return Bat_Serial,LastOperationOn, MAX_Error, SOC, SOH, last_charge_unit, last_charge_position, File_length
    # print("Last Operation-------- " + prev_data[3] + " - " + last_data[3])
    # print("Last Operation on ---- " + last_data[1] + " @ " + last_data[2] )
    # print("SOC ------------------ " + last_data[13] + "%")
    # print("SOH ------------------ " + last_data[14] + "%")


def info_read():
    try:
        Fname = f_select()
        Batery_serial, Lstop, lastopdadte, Error, soc,soh,last_charge_unit,last_charge_position, File_length = read_text1(Fname)
        print("Serial: " + Batery_serial)
        print("lstop: " + Lstop)
        print("LsDate: " + lastopdadte)
        print("Error: " + Error)
        print("SOC: " + soc)
        print("SOH: " + soh)
        print("Last CHarge Unit: " + last_charge_unit)
        print("Last CHarge Pos: " + last_charge_position)
        print("Length of the file: " + File_length)
    except FileNotFoundError:
        print("")
        print("No battery with that serial: 009{Ser} Exists..".format(Ser = Fname))

def info_read_vis(b):
    # print("before")
    try:
        # print("Came")
        Fname = f_select_vis(b)
        Batery_serial, soc = read_text1_vis(Fname)
        # print("Serial: " + Batery_serial)
        # print("lstop: " + Lstop)
        # print("LsDate: " + lastopdadte)
        # print("Error: " + Error)
        # print("SOC: " + soc)
        # print("SOH: " + soh)
        # print("Last CHarge Unit: " + last_charge_unit)
        # print("Last CHarge Pos: " + last_charge_position)
        # print("Length of the file: " + File_length)
    except FileNotFoundError:
        print("")
        print("No battery with that serial: 009{Ser} Exists..".format(Ser = Fname))
    return Batery_serial, soc

# for i in log_file:
#     print("Serial:- " + i)
if __name__ == "__main__":
    Fname = f_select()
    Batery_serial, Lstop, lastopdadte, Error, soc,soh,last_charge_unit,last_charge_position, File_length = read_text1(Fname)
    print("Serial: " + Batery_serial)
    print("lstop: " + Lstop)
    print("LsDate: " + lastopdadte)
    print("Error: " + Error)
    print("SOC: " + soc)
    print("SOH: " + soh)
    print("Last CHarge Unit: " + last_charge_unit)
    print("Last CHarge Pos: " + last_charge_position)
    print("Length of the file: " + File_length)

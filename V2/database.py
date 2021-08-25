
import os
import print_visual
from reader import Filename as fn
from reader import Log_reader as lg_r
import sys
temp_data = [[0 for i in range(5)] for j in range(3)]
# Current_battery = [[Serial, lastChargeDate, SOC, SOH, MAX_Error, LastChargeUnit, LastChargePosition, FileLength]]
Current_battery = [[0 for i in range(8)] for j in range(342)]
Old_battery = [[0 for i in range(8)] for j in range(342)]
inserted_batteries = [[0 for i in range(8)] for j in range(126)]
inserted_batteries_sorted = [[0 for i in range(8)] for j in range(126)]


log_file1= ['009508.txt', '009509.txt', '009510.txt', '009511.txt', '009512.txt', '009513.txt', '009514.txt', '009515.txt', '009516.txt', '009517.txt', '009518.txt', '009519.txt', '009520.txt', '009521.txt', '009522.txt', '009523.txt', '009524.txt', '009525.txt', '009526.txt', '009527.txt', '009528.txt', '009529.txt', '009530.txt', '009531.txt', '009532.txt', '009533.txt', '009534.txt', '009535.txt', '009536.txt', '009537.txt', '009538.txt', '009539.txt', '009540.txt', '009541.txt', '009543.txt', '009544.txt', '009545.txt', '009546.txt', '009547.txt', '009548.txt', '009549.txt', '009550.txt', '009551.txt', '009552.txt', '009553.txt', '009554.txt', '009555.txt', '009556.txt', '009558.txt', '009560.txt', '009561.txt', '009562.txt', '009563.txt', '009564.txt', '009565.txt', '009566.txt', '009567.txt', '009568.txt', '009569.txt', '009570.txt', '009572.txt', '009573.txt', '009574.txt', '009575.txt', '009576.txt', '009577.txt', '009578.txt', '009579.txt', '009580.txt', '009581.txt', '009583.txt', '009584.txt', '009585.txt', '009586.txt', '009587.txt', '009588.txt', '009589.txt', '009590.txt', '009591.txt', '009592.txt', '009593.txt', '009594.txt', '009595.txt', '009596.txt', '009597.txt', '009598.txt', '009599.txt', '009600.txt', '009601.txt', '009602.txt', '009603.txt', '009604.txt', '009605.txt', '009606.txt', '009607.txt', '009608.txt', '009609.txt', '009610.txt', '009611.txt', '009612.txt', '009613.txt', '009614.txt', '009615.txt', '009616.txt', '009617.txt', '009618.txt', '009619.txt', '009621.txt', '009622.txt', '009623.txt', '009624.txt', '009625.txt', '009626.txt', '009627.txt', '009628.txt', '009630.txt', '009631.txt', '009632.txt', '009633.txt', '009634.txt', '009635.txt', '009636.txt', '009637.txt', '009638.txt', '009639.txt', '009640.txt', '009641.txt', '009642.txt', '009643.txt', '009644.txt', '009645.txt', '009646.txt', '009647.txt', '009648.txt', '009649.txt', '009650.txt', '009651.txt', '009652.txt', '009653.txt', '009654.txt', '009655.txt', '009656.txt', '009657.txt', '009658.txt', '009659.txt', '009660.txt', '009661.txt', '009662.txt', '009663.txt', '009664.txt', '009665.txt', '009666.txt', '009667.txt', '009668.txt', '009669.txt', '009670.txt', '009671.txt', '009672.txt', '009673.txt', '009674.txt', '009675.txt', '009676.txt', '009677.txt', '009678.txt', '009679.txt', '009680.txt', '009681.txt', '009682.txt', '009683.txt', '009684.txt', '009685.txt', '009686.txt', '009687.txt', '009688.txt', '009689.txt', '009690.txt', '009691.txt', '009692.txt', '009693.txt', '009694.txt', '009695.txt', '009696.txt', '009697.txt', '009698.txt', '009699.txt', '009700.txt', '009701.txt', '009702.txt', '009703.txt', '009704.txt', '009705.txt', '009706.txt', '009707.txt', '009708.txt', '009709.txt', '009710.txt', '009711.txt', '009712.txt', '009713.txt', '009714.txt', '009715.txt', '009716.txt', '009717.txt', '009718.txt', '009719.txt', '009720.txt', '009721.txt', '009722.txt', '009723.txt', '009724.txt', '009725.txt', '009726.txt', '009727.txt', '009728.txt', '009729.txt', '009730.txt', '009731.txt', '009732.txt', '009733.txt', '009734.txt', '009735.txt', '009736.txt', '009737.txt', '009738.txt', '009739.txt', '009740.txt', '009741.txt', '009742.txt', '009743.txt', '009744.txt', '009745.txt', '009746.txt', '009747.txt', '009748.txt', '009749.txt', '009750.txt', '009751.txt', '009752.txt', '009753.txt', '009754.txt', '009755.txt', '009756.txt', '009757.txt', '009758.txt', '009759.txt', '009760.txt', '009761.txt', '009762.txt', '009763.txt', '009764.txt', '009765.txt', '009766.txt', '009767.txt', '009768.txt', '009769.txt', '009770.txt', '009771.txt', '009772.txt', '009773.txt', '009774.txt', '009775.txt', '009776.txt', '009777.txt', '009778.txt', '009779.txt', '009780.txt', '009781.txt', '009782.txt', '009783.txt', '009784.txt', '009785.txt', '009786.txt', '009787.txt', '009788.txt', '009789.txt', '009790.txt', '009791.txt', '009792.txt', '009793.txt', '009794.txt', '009795.txt', '009796.txt', '009797.txt', '009798.txt', '009800.txt', '009801.txt', '009802.txt', '009803.txt', '009804.txt', '009805.txt', '009806.txt', '009807.txt', '009808.txt', '009809.txt', '009810.txt', '009811.txt', '009812.txt', '009813.txt', '009814.txt', '009815.txt', '009816.txt', '009817.txt', '009818.txt', '009819.txt', '009820.txt', '009821.txt', '009822.txt', '009823.txt', '009824.txt', '009825.txt', '009826.txt', '009827.txt', '009828.txt', '009829.txt', '009830.txt', '009831.txt', '009832.txt', '009833.txt', '009834.txt', '009835.txt', '009836.txt', '009837.txt', '009838.txt', '009839.txt', '009840.txt', '009841.txt', '009842.txt', '009843.txt', '009844.txt', '009845.txt', '009846.txt', '009847.txt', '009848.txt', '009849.txt', '009850.txt', '009851.txt', '009852.txt', '009853.txt', '009854.txt', '009855.txt', '009856.txt', '009857.txt']

log_file = fn.list_dir(r'E:\Python\reader\Batterieverzeichnis')
log_file_new = fn.list_dir(r'E:\Python\reader\Batterieverzeichnis_new')
# def ser():
#     for n in range(len(Serials)):
#         print(str(n)+ ": " + Serials[n])

def takeSecond(elem):
    return elem[2]

def serial_get():
    for f in range(len(log_file1)):
        extracted_serial_new = log_file1[f].replace(".txt",'').replace("009",'')
        extracted_serial_old = log_file1[f].replace(".txt",'').replace("009",'')
        # print(extracted_serial_new)
        # Current_battery[f][0] = extracted_serial_new
        # return Bat_Serial, LastOperation, LastOperationOn, MAX_Error, SOC, SOH, last_charge_unit, last_charge_position, File_length
        # Current_battery = [[Serial, lastChargeDate, SOC, SOH, MAX_Error, LastChargeUnit, LastChargePosition, FileLength]]
        Current_battery[f][0], temp_data[0][0], Current_battery[f][1], Current_battery[f][4], Current_battery[f][2], Current_battery[f][3], Current_battery[f][5],Current_battery[f][6], Current_battery[f][7] = lg_r.read_text(extracted_serial_new,"Batterieverzeichnis_new")
        Old_battery[f][0], temp_data[0][0], Old_battery[f][1], Old_battery[f][4], Old_battery[f][2], Old_battery[f][3], Old_battery[f][5],Old_battery[f][6], Old_battery[f][7] = lg_r.read_text(extracted_serial_old,"Batterieverzeichnis")
def printer():
    i = 0
    for pr in range(len(log_file1)):
        if Current_battery[pr][7] != Old_battery[pr][7]:
            # print(pr, end="")
            # print(Current_battery[pr])
            # print(pr, end="")
            # print(Old_battery[pr])
            inserted_batteries[i] = Current_battery[pr]
            i = i + 1
        # else:
            # print("No Change")
            # print(Current_battery[pr])

def current_arrangement_print():
        print("============================================================================== Current Arrangment ============================================================================================")
        print(" ")
        print_visual.fill_slots(inserted_batteries)
        for i in range(len(inserted_batteries)):
            if(inserted_batteries[i][0]!= 0):
                inserted_batteries_sorted[i] = inserted_batteries[i]
                inserted_batteries_sorted[i][2] = int(inserted_batteries[i][2].replace("%",""))
        inserted_batteries_sorted.sort(key=takeSecond, reverse=True)
        # print(inserted_batteries_sorted)  #Shows list
        # print(inserted_batteries)
        # v = inserted_batteries[0][2].replace("%","")
        # print(v)
        # print("+++++++++++SORTED LIST END+++++++++++")

def sorted_arrangement_print():
    print("============================================================================== Sorted Arrangment ============================================================================================")
    for i in range(len(inserted_batteries_sorted)):
        inserted_batteries_sorted[i][2] = str(inserted_batteries_sorted[i][2])
        inserted_batteries_sorted[i][2] = inserted_batteries_sorted[i][2].replace("","%")
        m = i + 1
        inserted_batteries_sorted[i][5] = (m//18)+1
        inserted_batteries_sorted[i][6] = (m%18)
    print(" ")
    print_visual.fill_slots(inserted_batteries_sorted)



if __name__ == '__main__':
    serial_get()
    # return Bat_Serial, LastOperationOn, MAX_Error, SOC, SOH, last_charge_unit, last_charge_position, File_length
    # Current_battery[0][0],Current_battery[0][1],Current_battery[0][2],Current_battery[0][3],Current_battery[0][4],Current_battery[0][5],Current_battery[0][6],Current_battery[0][7] = lg_r.read_text(str(768))
    # print(len(log_file1))
    # ser()
    # print(log_file)
    # print(Current_battery)
    printer()
    # print("printer() - Done***********************")
    # print("--------------------")
    # # inserted_batteries[125] = inserted_batteries[0]
    # print(inserted_batteries)
    # print("--------------------")
    # print("+++++++++++SORTED LIST START+++++++++++")

    current_arrangement_print()

    print(" ")
    sorted_arrangement_print()

    # print(log_file)


# print(log_file)
# fname = "E://Python/reader/Batterieverzeichnis/009768.txt"
# for bateries in range(len(Current_battery)):

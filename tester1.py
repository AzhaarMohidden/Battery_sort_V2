# import print_visual
# import random
#
# arr_temp = [[0 for i in range(2)] for j in range(18)]
# m = 23
# def counters():
#     for i in range(1,8,1):
#         print("tray: " + str(i))
#         for b in range(1, 19, 1):
#             print("Battery: " + str(b) + "unit: " + str(i))
#     v = m%18
#     w = (m // 18) +1
#     print(v)
#     print(w)
#
# def fill():
#     for batteries in range(18):
#         for n in range(2):
#             arr_temp[batteries][0] = str(random.randint(100, 900))
#             soc_t = random.randint(0, 100)
#             if (soc_t < 100 and soc_t > 9):
#                 arr_temp[batteries][1] = str(soc_t) + "%"
#             elif soc_t < 10:
#                 arr_temp[batteries][1] = " " + str(soc_t) + "%"
#             else:
#                 arr_temp[batteries][1] = str(soc_t)
#
# # fill()
# # print_visual.Output_multiple(2, arr_temp)
# counters()

from Max_Error import Write_error as ME
from datetime import datetime
from functools import cache
import time

array = [5 for i in range(250)]
name = ["A", "B", "C"]
data = [["a" for i in range(10)], ["b" for i in range(10)], ["c" for i in range(10)] ]

# log_file1= ['009508.txt', '009509.txt', '009510.txt', '009511.txt', '009512.txt', '009513.txt', '009514.txt', '009515.txt', '009516.txt', '009517.txt', '009518.txt', '009519.txt', '009520.txt', '009521.txt', '009522.txt', '009523.txt', '009524.txt', '009525.txt', '009526.txt', '009527.txt', '009528.txt', '009529.txt', '009530.txt', '009531.txt', '009532.txt', '009533.txt', '009534.txt', '009535.txt', '009536.txt', '009537.txt', '009538.txt', '009539.txt', '009540.txt', '009541.txt', '009543.txt', '009544.txt', '009545.txt', '009546.txt', '009547.txt', '009548.txt', '009549.txt', '009550.txt', '009551.txt', '009552.txt', '009553.txt', '009554.txt', '009555.txt', '009556.txt', '009558.txt', '009560.txt', '009561.txt', '009562.txt', '009563.txt', '009564.txt', '009565.txt', '009566.txt', '009567.txt', '009568.txt', '009569.txt', '009570.txt', '009572.txt', '009573.txt', '009574.txt', '009575.txt', '009576.txt', '009577.txt', '009578.txt', '009579.txt', '009580.txt', '009581.txt', '009583.txt', '009584.txt', '009585.txt', '009586.txt', '009587.txt', '009588.txt', '009589.txt', '009590.txt', '009591.txt', '009592.txt', '009593.txt', '009594.txt', '009595.txt', '009596.txt', '009597.txt', '009598.txt', '009599.txt', '009600.txt', '009601.txt', '009602.txt', '009603.txt', '009604.txt', '009605.txt', '009606.txt', '009607.txt', '009608.txt', '009609.txt', '009610.txt', '009611.txt', '009612.txt', '009613.txt', '009614.txt', '009615.txt', '009616.txt', '009617.txt', '009618.txt', '009619.txt', '009621.txt', '009622.txt', '009623.txt', '009624.txt', '009625.txt', '009626.txt', '009627.txt', '009628.txt', '009630.txt', '009631.txt', '009632.txt', '009633.txt', '009634.txt', '009635.txt', '009636.txt', '009637.txt', '009638.txt', '009639.txt', '009640.txt', '009641.txt', '009642.txt', '009643.txt', '009644.txt', '009645.txt', '009646.txt', '009647.txt', '009648.txt', '009649.txt', '009650.txt', '009651.txt', '009652.txt', '009653.txt', '009654.txt', '009655.txt', '009656.txt', '009657.txt', '009658.txt', '009659.txt', '009660.txt', '009661.txt', '009662.txt', '009663.txt', '009664.txt', '009665.txt', '009666.txt', '009667.txt', '009668.txt', '009669.txt', '009670.txt', '009671.txt', '009672.txt', '009673.txt', '009674.txt', '009675.txt', '009676.txt', '009677.txt', '009678.txt', '009679.txt', '009680.txt', '009681.txt', '009682.txt', '009683.txt', '009684.txt', '009685.txt', '009686.txt', '009687.txt', '009688.txt', '009689.txt', '009690.txt', '009691.txt', '009692.txt', '009693.txt', '009694.txt', '009695.txt', '009696.txt', '009697.txt', '009698.txt', '009699.txt', '009700.txt', '009701.txt', '009702.txt', '009703.txt', '009704.txt', '009705.txt', '009706.txt', '009707.txt', '009708.txt', '009709.txt', '009710.txt', '009711.txt', '009712.txt', '009713.txt', '009714.txt', '009715.txt', '009716.txt', '009717.txt', '009718.txt', '009719.txt', '009720.txt', '009721.txt', '009722.txt', '009723.txt', '009724.txt', '009725.txt', '009726.txt', '009727.txt', '009728.txt', '009729.txt', '009730.txt', '009731.txt', '009732.txt', '009733.txt', '009734.txt', '009735.txt', '009736.txt', '009737.txt', '009738.txt', '009739.txt', '009740.txt', '009741.txt', '009742.txt', '009743.txt', '009744.txt', '009745.txt', '009746.txt', '009747.txt', '009748.txt', '009749.txt', '009750.txt', '009751.txt', '009752.txt', '009753.txt', '009754.txt', '009755.txt', '009756.txt', '009757.txt', '009758.txt', '009759.txt', '009760.txt', '009761.txt', '009762.txt', '009763.txt', '009764.txt', '009765.txt', '009766.txt', '009767.txt', '009768.txt', '009769.txt', '009770.txt', '009771.txt', '009772.txt', '009773.txt', '009774.txt', '009775.txt', '009776.txt', '009777.txt', '009778.txt', '009779.txt', '009780.txt', '009781.txt', '009782.txt', '009783.txt', '009784.txt', '009785.txt', '009786.txt', '009787.txt', '009788.txt', '009789.txt', '009790.txt', '009791.txt', '009792.txt', '009793.txt', '009794.txt', '009795.txt', '009796.txt', '009797.txt', '009798.txt', '009800.txt', '009801.txt', '009802.txt', '009803.txt', '009804.txt', '009805.txt', '009806.txt', '009807.txt', '009808.txt', '009809.txt', '009810.txt', '009811.txt', '009812.txt', '009813.txt', '009814.txt', '009815.txt', '009816.txt', '009817.txt', '009818.txt', '009819.txt', '009820.txt', '009821.txt', '009822.txt', '009823.txt', '009824.txt', '009825.txt', '009826.txt', '009827.txt', '009828.txt', '009829.txt', '009830.txt', '009831.txt', '009832.txt', '009833.txt', '009834.txt', '009835.txt', '009836.txt', '009837.txt', '009838.txt', '009839.txt', '009840.txt', '009841.txt', '009842.txt', '009843.txt', '009844.txt', '009845.txt', '009846.txt', '009847.txt', '009848.txt', '009849.txt', '009850.txt', '009851.txt', '009852.txt', '009853.txt', '009854.txt', '009855.txt', '009856.txt', '009857.txt']
#
# available_batteries = ['9508', '9509', '9510', '9511', '9512', '9513', '9514', '9515', '9516', '9517', '9532', '9534', '9535', '9536', '9537', '9544', '9545', '9546', '9547', '9548', '9549', '9550', '9551', '9556', '9557', '9558', '9564', '9568', '9569', '9570', '9571', '9572', '9573', '9574', '9575', '9576', '9577', '9578', '9579', '9580', '9581', '9582', '9583', '9584', '9585', '9586', '9587', '9588', '9589', '9590', '9591', '9592', '9593', '9594', '9595', '9596', '9597', '9598', '9599', '9600', '9601', '9602', '9603', '9610', '9611', '9612', '9613', '9615', '9646', '9647', '9649', '9650', '9651', '9652', '9653', '9654', '9655', '9656', '9657', '9658', '9659', '9660', '9661', '9662', '9663', '9666', '9670', '9671', '9672', '9673', '9674', '9675', '9677', '9682', '9683', '9684', '9685', '9686', '9687', '9688', '9689', '9690', '9691', '9700', '9701', '9702', '9703', '9704', '9705', '9706', '9707', '9708', '9709', '9710', '9711', '9712', '9713', '9714', '9715', '9716', '9717', '9718', '9719', '9720', '9721', '9722', '9723', '9724', '9725', '9726', '9727', '9728', '9729', '9730', '9731', '9732', '9733', '9734', '9735', '9736', '9737', '9738', '9739', '9740', '9741', '9742', '9743', '9744', '9745', '9746', '9747', '9748', '9749', '9750', '9751', '9752', '9753', '9754', '9755', '9756', '9757', '9758', '9759', '9760', '9761', '9762', '9763', '9764', '9765', '9766', '9767', '9768', '9769', '9770', '9771', '9772', '9773', '9774', '9775', '9776', '9777', '9778', '9779', '9780', '9781', '9782', '9783', '9784', '9785', '9786', '9787', '9788', '9789', '9790', '9791', '9792', '9793', '9794', '9795', '9796', '9797', '9798', '9799', '9800', '9801', '9802', '9803', '9804', '9805', '9806', '9807', '9808', '9809', '9810', '9811', '9813', '9820', '9821', '9822', '9823', '9824', '9825', '9826', '9827', '9828', '9829', '9830', '9831', '9832', '9833', '9834', '9835', '9836', '9837', '9838', '9839', '9840', '9841', '9842', '9843', '9844', '9845', '9848', '9849', '9850', '9851', '9852', '9853', '9854', '9855']
#
# av_file = ["n" for i in range(250)]
#
#
#
#
#
#
# for m in range(len(av_file)):
#     av_file[m] = "00"+str(available_batteries[m])+".txt"
#
# # print(av_file)
# for m in range(len(available_batteries)):
#     available_batteries[m] ="00" +str(available_batteries[m])
#     available_batteries[m] =available_batteries[m].replace("009", "")
#
# print(available_batteries)



# ME.variable_writer(name, data)

# now = datetime.now()
# print(now)
#
# year = now.strftime("%Y")
# print(year)
# month = now.strftime("%Y")
# print(month)
# day = now.strftime("%Y")
# print(day)
# date_time = now.strftime("%Y%m%d-%H.%M.%S")
# print(date_time)

# @cache
# def fib(n):
#     if (n<=1):
#         return n
#     return fib(n-1) + fib(n-2)
#
# if __name__ == "__main__":
#     for i in range(500):
#         print(str(i) + ": " + str(fib(i))


# with tqdm(total = 100) as pbar:
#     for i in range(251):
#         time.sleep(0.0001)
#         pbar.update(0.4)

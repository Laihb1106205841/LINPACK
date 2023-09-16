import xlwt as xlwt

address = "D:/比赛/读取/"
name = "70603.out"
filename = address+name
outfile = open(filename, 'r', encoding='UTF-8')


i=0
x = 1  # 在第二行开始写
y = 0  # 在第一列开始写

xls = xlwt.Workbook(encoding='UTF-8')
sheet = xls.add_sheet(name+"graph")  # 生成excel的方法，声明excel
#print(outfile.read())


style11 = xlwt.easyxf(num_format_str='0.00E+00') # 科学记数法

for item in outfile:
    # steps = 376-252
    # if(i==26):
    #     sheet.write(0,1,item)

    if('WR' in item):
        #print(item)
        print(item[70:81])
        theline = item
        T_or_V = theline[0:8]
        N = theline[15:21]
        NB = theline[23:27]
        P = theline[31:32]
        Q = theline[37:38]
        Time = theline[51:58]
        Gflops = theline[70:80]

        Gflops = eval(Gflops)


        data = [T_or_V,N,NB,P,Q,Time,Gflops]

        for z in data:
            #sheet.write(0, 0, '拼音')  # 在第一行第一列单元格写"拼音"
            sheet.write(x, y, z)  # x代表行，y代表列

            y += 1
        sheet.write(x, y, int(Gflops), style11)
        y=0
        x+=1

             # 保存

    i += 1
xls.save(name+".xlsx")


    # if((i-252)%(steps)==0):
    #
    #     theline = item
    #     T_or_V = theline[0:8]
    #     N = theline[15:21]
    #     NB = theline[23:27]
    #     P = theline[31:32]
    #     Q = theline[37:38]
    #     Time = theline[51:58]
    #     Gflops = theline[70:81]
    #
    #     data = [T_or_V,N,NB,P,Q,Time,Gflops]
    #     print(data)
    #     for z in data:
    #         #sheet.write(0, 0, '拼音')  # 在第一行第一列单元格写"拼音"
    #         sheet.write(x, y, z)  # x代表行，y代表列
    #         y += 1
    #     y=0
    #     x+=1
    #
    #      # 保存
    #
    # i +=1
#xls.save(name+".xlsx")

outfile.close()






# In[ ]:

#寫入xlxs
def get_xlsxoutput(_kuse):
    from sklearn.cluster import KMeans
    import numpy as np
    import csv
    import codecs
    import struct
    import xlwt
    from xlsxwriter.workbook import Workbook
    X = np.array(_kuse)
    kmeans = KMeans(n_clusters=2, random_state=100).fit(_kuse)

    #print(_kuse)
    #print(kmeans.labels_)

    # 開啟輸出的 CSV 檔案
    with open('yourOutput.csv', 'w', newline='', encoding='utf-8') as csvFile:    
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvFile, delimiter=',',quotechar='|')
        writer.writerow(['image','class','color','names','labels'])
        for i in range(int(len(kmeans.labels_))):
            writer.writerow([_kuseUrl[i],kmeans.cluster_centers_[kmeans.labels_[i]],str(kmeans.labels_[i]),_kuseName[i],_kuseLabels[i]])
    #xlxs
    book = xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet = book.add_sheet('mysheet',cell_overwrite_ok=True)
    sheet.write(0,0,'image')
    sheet.write(0,1,'class')
    sheet.write(0,2,'color')
    sheet.write(0,3,'names')
    sheet.write(0,4,'labels')

    for i in range(int(len(_kuseUrl))):    
            sheet.write(i+1,0,_kuseUrl[i])
            sheet.write(i+1,1,str(kmeans.cluster_centers_[kmeans.labels_[i]]))
            sheet.write(i+1,2,str(kmeans.labels_[i]))
            sheet.write(i+1,3,str(_kuseName[i]))
            sheet.write(i+1,4,str(_kuseLabels[i]))
            #im=Image.open(os.path.join(_kuseUrl[i]))
            #im=im.resize((40, 71),Image.ANTIALIAS)
            #im.convert("RGB").save('violations.bmp')    
            #sheet.insert_bitmap('violations.bmp',i+1,5)
            
    book.save('test.xls')        
    plt.scatter(X[:,0],X[:,1],X[:,2], c=kmeans.labels_)
#get_xlsxoutput(_kuse)
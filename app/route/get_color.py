# In[ ]:

#顏色辨識邊緣偵測版
def get_edgecolor(_images):
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import numpy as np
    import cv2
    import collections, numpy
    from sklearn.cluster import KMeans
    _findColor=[]
    interval=25
    for k in range(0,500,interval):
        _findColor.append([])
        
        #原圖
        plt.subplot(1,4,1)
        _color=cv2.imread(_images[k])
        _color=cv2.resize(_color,(int(_color.shape[1]/8), int(_color.shape[0]/8)))
        _color = cv2.cvtColor(_color, cv2.COLOR_BGR2RGB)
        plt.imshow(_color)
        plt.axis('off')

        #邊緣偵測
        image = cv2.imread(_images[k])
        image=cv2.resize(image,(int(image.shape[1]/8), int(image.shape[0]/8)),interpolation = cv2.INTER_AREA)
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        kernel_size = 5
        blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size), 0)
        low_threshold = 1
        high_threshold = 200
        edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
        plt.subplot(1,4,2)
        plt.imshow(edges, cmap='Greys_r')
        plt.axis('off')

        #邊緣偵測疊在原圖上            
        _originTop=cv2.imread(_images[k])
        _originTop=cv2.resize(_originTop,(int(_originTop.shape[1]/8), int(_originTop.shape[0]/8)))
        _originTop=cv2.cvtColor(_originTop, cv2.COLOR_BGR2RGB)
        
        #原圖+邊緣偵測    
        for i in range (len(edges)):
            for j in range (len(edges[i])):
                if(edges[i][j]==0):
                    _color[i][j]=0
                else:
                    _findColor[int(k/interval)].append(_originTop[i][j].copy())
                    _originTop[i][j]=0
                    #_originTop[i][j-1]=0
                    #_originTop[i-1][j]=0
                    
        plt.subplot(1,4,3)    
        plt.imshow(_color)
        plt.axis('off')

        plt.subplot(1,4,4)    
        plt.imshow(_originTop)
        plt.axis('off')

        plt.show()
        
        #分辨顏色(這個先註解掉)
        #cul(int(k/interval))
#get_edgecolor(_images)

# In[ ]:

#顏色辨識一般分群版
def get_normalcolor(_images):
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    from PIL import Image
    import matplotlib.pyplot as plt
    import math
    import threading
    import time
    _kuse = []
    _kuseLabels = []
    _kuseName = []
    _kuseUrl = []
    _kuseRgb = []
    threadCou=1#執行序的數量
    rRate=1.2#RGB的縮放比例
    gRate=-0.4
    bRate=0.6
    k =8# number of clusters (K)
    start=0#迴圈參數
    end=len(_images)
    interval=1000
    fp = open("filename.txt", "w")# 開啟檔案
    fp.write('--------------------start-----------------------'+'\r\n')

    #做幾輪
    for i in range(start,end,interval):
        # read the image
        image = cv2.imread(_images[i])
        #圖片縮放
        image=cv2.resize(image,(int(image.shape[1]/16), int(image.shape[0]/16)),interpolation = cv2.INTER_AREA)
        # convert to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # reshape the image to a 2D array of pixels and 3 color values (RGB)
        pixel_values = image.reshape((-1, 3))
        # convert to float
        pixel_values = np.float32(pixel_values) 
        # define stopping criteria
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
        _, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 20, cv2.KMEANS_RANDOM_CENTERS)
        # convert back to 8 bit values
        centers = np.uint8(centers)
        # flatten the labels array
        labels = labels.flatten()
        # convert all pixels to the color of the centroids
        segmented_image = centers[labels.flatten()]
        # reshape back to the original image dimension
        segmented_image = segmented_image.reshape(image.shape)
        #maxrgb=max(centers[i][0],centers[i][1],centers[i][2])
        bigRed=0
        #去背
        for j in range(k):
            if(centers[j][0]>155 and centers[j][1]>130 and centers[j][2]>155):
                centers[j][0]=0
                centers[j][1]=0
                centers[j][2]=0
        #選花色
        for j in range(k):
            if((centers[j][0]*rRate)+(centers[j][1]*gRate)+(centers[j][2]*bRate)>(centers[bigRed][0]*rRate)+(centers[bigRed][1]*gRate)+(centers[bigRed][2]*bRate)):
                bigRed = j

        #for j in range(k):
            #print(centers)

        
        #顯示圖片(顏色/kmean後的圖/原圖)
        row=3
        plt.subplot(1,row,1+3*((i/interval)%(row/3)))
        plt.imshow([[(centers[bigRed][0] / 255, centers[bigRed][1] / 255, centers[bigRed][2] / 255)]])
        plt.axis('off')
        plt.subplot(1,row,2+3*((i/interval)%(row/3)))
        plt.imshow(segmented_image)
        plt.axis('off')
        plt.subplot(1,row,3+3*((i/interval)%(row/3)))
        img = Image.open(os.path.join(_images[i]))
        plt.imshow(img)
        plt.axis('off')
        
        _kuseRgb.append(segmented_image)
        
        
        #if(i/interval%(row)==(row/3-1)):
        plt.show()
        print(_images[i])
        _kuseUrl.append(_images[i])
        _kuse.append(centers[bigRed])
        _kuseLabels.append(_labels[i])
        _kuseName.append(_name[i])
        fp.write(_images[i]+'('+str(centers[bigRed][0])+','+str(centers[bigRed][1])+','+str(centers[bigRed][2])+')'+str(i)+'\r\n')
        #顯示數據
        #print(centers[bigRed])
        #print(centers)       
        #print(i*threadCou+num)
            
        # 寫入 This is a testing! 到檔案
    fp.write('==========================end=============================')
    fp.close()# 關閉檔案 
    return _kuse
#get_normalcolor(_images)

# In[ ]:

#Kmean工具
def cul(i):
    kmeans = KMeans(n_clusters=10, random_state=0).fit(np.array(_findColor[i]))
    #RGB的縮放比例
    rRate=2
    gRate=-1
    bRate=0.6
    bigRed=0
    #第一排k種顏色
    for j in range(len(kmeans.cluster_centers_)):
        plt.subplot(1,len(kmeans.cluster_centers_),j+1)
        plt.imshow([[(kmeans.cluster_centers_[j][0] / 255, kmeans.cluster_centers_[j][1] / 255,kmeans.cluster_centers_[j][2] / 255)]])
        plt.axis('off')
        if(kmeans.cluster_centers_[j][0]>150 and kmeans.cluster_centers_[j][1]>150 and kmeans.cluster_centers_[j][2]>150):
            kmeans.cluster_centers_[j][0]=0
            kmeans.cluster_centers_[j][1]=0
            kmeans.cluster_centers_[j][2]=0
        if((kmeans.cluster_centers_[j][0]*rRate)+(kmeans.cluster_centers_[j][1]*gRate)+(kmeans.cluster_centers_[j][2]*bRate)>(kmeans.cluster_centers_[bigRed][0]*rRate)+(kmeans.cluster_centers_[bigRed][1]*gRate)+(kmeans.cluster_centers_[bigRed][2]*bRate)):
            bigRed = j
    plt.show()

    #第二排挑出的顏色+原圖(resize)
    plt.subplot(1,len(kmeans.cluster_centers_),1)
    plt.imshow([[(kmeans.cluster_centers_[bigRed][0] / 255, kmeans.cluster_centers_[bigRed][1] / 255,kmeans.cluster_centers_[bigRed][2] / 255)]])
    plt.axis('off')
    
    plt.show()
    print (kmeans.cluster_centers_[bigRed].astype(int))
      
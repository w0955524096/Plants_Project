# In[ ]:

#依照csv檔案去抓取全部圖片並放進list
def get_picture():
    import numpy as np
    import cv2
    import matplotlib.pyplot as plt
    _images = []
    _labels = []
    _name = []
    cou = 0
    for subdir, dirs, files in tqdm(os.walk(DATASET_DIR)):
        for filename in files:
            cur_p = subdir + os.sep + filename
            corr_label = label_df[label_df['dirpath']==os.sep.join(cur_p.split(os.sep)[5:-1])]
            if corr_label.size!= 0 and filename.endswith('jpg'):
                _images.append(cur_p)
                _labels.append(corr_label['label'].values[0])
                _name.append(corr_label['target'].values[0])
get_picture()

# In[ ]:

#顯示有幾張圖片
def show_image():
    len(_images), len(_labels), len(_name)
    print(_images[0], _labels[0], _name[0])
show_image()
import cv2
from matplotlib import pyplot as plt

#menyimpan path untuk diproses di kode
path = ['dokSample/d0001.jpg', 'dokSample/d0003.jpg']

#untuk memberikan judul pada tampilan matplotlib
titles = ['0,255:biner','190,225:biner', '100,255:biner', '0,255:invers','190,225:invers','100,255:invers']

#dokumen citra dibuka dengan mode grayscale dan disimpan di list
img = [cv2.imread(image, 0) for image in path]

#nilai threshold dan maksimal yang akan digunakan (respectively)
nilai = [[0, 255], [190, 255], [100, 255]]

#tempat untuk menampung hasil thresholding
#threshold1 menyimpan hasil threshold dokumen citra 1
#threshold2 juga untuk citra ke-2
#index 0-2 menyimpan hasil threshold dengan teknik binary
#index 3-5 menyimpan hasil threshold dengan teknik invers
threshold1 = [0, 0, 0, 0, 0, 0]
threshold2 = [0, 0, 0, 0, 0, 0]

#threshold ke binary
for i in range(3):

    #proses citra ke-1
    ret, threshold1[i] = cv2.threshold(img[0], nilai[i][0], nilai[i][1], cv2.THRESH_BINARY)

    #proses citra ke-2
    ret, threshold2[i] = cv2.threshold(img[1], nilai[i][0], nilai[i][1], cv2.THRESH_BINARY)


#threshold ke invers
for i in range(3, 6):

    #proses citra ke-1
    ret, threshold1[i] = cv2.threshold(img[0], nilai[i-3][0], nilai[0][1], cv2.THRESH_BINARY_INV)

    #proses citra ke-2
    ret, threshold2[i] = cv2.threshold(img[1], nilai[i-3][0], nilai[0][1], cv2.THRESH_BINARY_INV)


#tampilkan hasil thresholding
#threshold citra ke-1
for i in range(0, 6):
    plt.subplot(1, 6, i+1), plt.imshow(threshold1[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

#threshold citra ke-2
for i in range(0, 6):
    plt.subplot(1, 6, i+1), plt.imshow(threshold2[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

#output dengan cara lain
'''for i, image in enumerate(threshold1):
    cv2.imshow('Gambar ke-'+str(i+1)+', d0001.jpg', image)
    cv2.waitKey(0)

for i, image in enumerate(threshold2):
    cv2.imshow('Gambar ke-'+str(i+1)+', d0003.jpg', image)
    cv2.waitKey(0)'''

i = cv2.imread("layer.jpg",0)
l = cv2.imread("stage.jpg",0)
l = l*10

dev = 51
L = cv2.GaussianBlur(l,(dev,dev),0)
Linv = invert(L)
Linv = (Linv-Linv.min())/Linv.max()


#plt.imshow(Linv*i,cmap='gray')

fig = plt.figure()
sp = fig.add_subplot(131)
sp2 = fig.add_subplot(132)
sp3 = fig.add_subplot(133)

sp.imshow(i,cmap='gray')
sp2.imshow(Linv*i,cmap='gray')
sp3.imshow(Linv*i+i,cmap='gray')

plt.show()

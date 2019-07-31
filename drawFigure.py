#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签 
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#画折线图
def drawZXT(x1, y1, x2, y2, xLabel, yLabel, titleName):
	plt.figure("ZXT")

	plt.plot(x1,y1,color='red',label='line1')
	plt.plot(x2,y2,color='blue',label='line2')
	
	plt.xlabel('%s'%xLabel, fontsize=16)
	plt.ylabel('%s'%yLabel, fontsize=16)
	plt.title('%s'%titleName, fontsize=16)
	plt.savefig('ZXT.png', dpi=75)

if __name__ == '__main__':
	#===>
	drawZXT([1,2,3],[3,1,2],[1,2,3],[1,2,3],"steps","loss","ZXT")
	#<===

#=============================参考
#https://www.jianshu.com/p/eb9ba6ee0772(matplotlib手册(7) - 折线图和曲线图)

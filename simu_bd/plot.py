import numpy as np
import pylab as pl

da1 = np.loadtxt('6724-0-v2.txt')
da2 = np.loadtxt('656-7-0.TXT')
da3 = np.loadtxt('6724-17-v2.txt')
#da4 = np.loadtxt('656-8-15.TXT')

pl.plot(da1[:,0],da1[:,1],'k',lw=2,label='cwl $\sim$ 659.0 nm')
#pl.plot([660.4, 660.4], [0,95.8])
#pl.plot([657.6, 657.6], [0,95.8])
#pl.plot([659, 659.], [0,95.8])
#pl.plot([655.5,662.5],[47.5,47.5])

#pl.plot(da2[:,0],da2[:,1],'g',lw=2)
pl.plot(da3[:,0],da3[:,1],'b',lw=2,label='cwl $\sim$ 656.5 nm')
#pl.plot(da4[:,0],da4[:,1],'r',lw=2)
#pl.plot([656.3, 656.3], [0,93.5])
#pl.plot([652.5,660.1],[46.5,46.5])
pl.xlim(630,700)
#pl.legend(loc=2)
#pl.text(632,70,'Designed band width is 6 nm', fontsize=15)
#pl.text(632,75,'designed band width is 5 nm')  
#pl.text(632,70,'real band width is 6.3 nm')                                   
#pl.text(632,60,'Transmittance: ~81.17%')                               
#pl.text(632,55,'designed band width is 7 nm')  
#pl.text(632,50,'real band width is 8 nm')                                   
pl.show()

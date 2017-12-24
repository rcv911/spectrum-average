from numpy import *
from matplotlib.pyplot import *
from numpy.fft import rfft

dt=0.004 # sample rate
N=1250 # length of record

mas1=loadtxt('one_subject_network_source_1.txt')
mas2=loadtxt('one_subject_network_source_2.txt')
mas3=loadtxt('one_subject_network_source_3.txt')
mas4=loadtxt('one_subject_network_source_4.txt')
mas1=mas1.reshape((84,N))
mas2=mas2.reshape((84,N))
mas3=mas3.reshape((84,N))
mas4=mas4.reshape((84,N))
masmean1=zeros((84,(N/2+1)))
masmean2=zeros((84,(N/2+1)))
masmean3=zeros((84,(N/2+1)))
masmean4=zeros((84,(N/2+1)))


#spectrum average
for el in range(84):
    masmean1[el]=abs(rfft(mas1[el,:]))/(len(mas1[el,:])/2)
    masmean2[el]=abs(rfft(mas2[el,:]))/(len(mas2[el,:])/2)
    masmean3[el]=abs(rfft(mas3[el,:]))/(len(mas3[el,:])/2)
    masmean4[el]=abs(rfft(mas4[el,:]))/(len(mas4[el,:])/2)
            
freq=linspace(0, 1/(2*dt), (len(mas1[0,:])/2) + 1)

cut = 250

#draw
figure('spectrum average EEG')
subplot(4,1,1)
ylabel('1 channel')
plot(freq[:cut], mean(masmean1,axis=0)[:cut])
grid()
subplot(4,1,2)
ylabel('2 channel')
plot(freq[:cut], mean(masmean2,axis=0)[:cut])
grid()
subplot(4,1,3)
ylabel('3 channel')
plot(freq[:cut], mean(masmean3,axis=0)[:cut])
grid()
subplot(4,1,4)
xlabel('f, Hz')
ylabel('4 channel')
plot(freq[:cut], mean(masmean4,axis=0)[:cut])
grid()
savefig('spectrum_average_eeg_data.png')
show()
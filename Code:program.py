import turtle
import numpy as np
import random as rd

M = 100
p = 0.3
vMobilTiapDetik0 = 0
N = 10
dt = 1
vMobilTiapDetikmax = 5
tmax = 100
t = 0

mobil = []  # list mobil
vMobilTiapDetik = [] # list kecepatan masing masing mobil tiap detik
vMobilTiapDetik = [vMobilTiapDetik0]*N # inisiasi vMobilTiapDetik0 tiap mobil = 0 
kepadatanMobilIntervalx80x90 = [] # kepadatan mobil pada selang x 80 & x90
tPosisiSemula = [] # waktu dari tiap mobil untuk kembali posisi semula
tPosisiSemula = [vMobilTiapDetik0]*N
nMobilLintasiKoordAwal = [] # banyak mobil melewati koordinatAwal
nMobilLintasiKoordAwal = [vMobilTiapDetik0]*N
warnaMobil = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue']
koordinatAwal = [] # koordinatAwal mobil

# membuat koordinatAwal
for a in range(10):
    koordinatAwal.append(rd.randint(-300,300))
koordinatAwal.sort()

turtle.Screen().setup(1000,300,0,0)
turtle.Screen().delay(1)
turtle.Screen().bgcolor("black")

# pengecekan jarak antar mobil
def jarakMobil() :
    if (k == N-1):
        if(mobil[k].xcor() > mobil[0].xcor()):
           d = abs(M - (mobil[k].xcor() - mobil[0].xcor()))
           
        else :
           d = abs(mobil[0].xcor() - mobil[k].xcor())
           
    else :
        if (mobil[k].xcor() < mobil[k+1].xcor()) :
            d = abs(mobil[k+1].xcor() - mobil[k].xcor())
           
        else:
            d = abs(M - (mobil[k+1].xcor() - mobil[k].xcor()))
            
    return d

# pertambahan kecepatan
def updatevMobilTiapDetik():
    vMobilTiapDetik[k] = min(vMobilTiapDetik[k]+1, vMobilTiapDetikmax)
    d = jarakMobil()
    vMobilTiapDetik[k] = min(vMobilTiapDetik[k], d-1)
    x = np.random.uniform(0,1)
    if (x >= p):
        vMobilTiapDetik[k] = max(0,vMobilTiapDetik[k]-1)
    return vMobilTiapDetik[k]

# membuat mobil
for j in range(10) :
    car = turtle.Turtle()
    car.shape("circle")
    mobil.append(car)
    
# set koordinatAwal mobil
for i in range (10) :
    mobil[i].color(warnaMobil[i])
    mobil[i].penup()
    mobil[i].goto(koordinatAwal[i],0)
    
# running
while t <= tmax:
    x = 0
    for k in range(N):
            
        mobil[k].forward(updatevMobilTiapDetik())
        mobil[k].speed(10)
        if (mobil[k].xcor() >= 500):
            mobil[k].ht()
            mobil[k].goto(-500,0)
            mobil[k].st()
            
        # menghitung waktu mobil melewati posisi semula
        if (koordinatAwal[k] >= mobil[k].xcor()):
            if (0 <= koordinatAwal[k] - mobil[k].xcor() <=50):
                tPosisiSemula[k] += t
                nMobilLintasiKoordAwal[k] += 1
        # menghitung pada selang x80 dan x 90
        if (((M/2) - 200) <= mobil[k].xcor() <= ((M/2)-100)):
            x+=1
    t+=1
    kepadatanMobilIntervalx80x90.append(x)

print("")
print("Kepadatan per satuan waktu pada waktu interval [x80,x90] =")
print(kepadatanMobilIntervalx80x90)
print("")  
for x in range(10):
    print('Waktu rata-rata kendaraan',x+1,'kembali ke posisi awalnya =',(tPosisiSemula[x]/nMobilLintasiKoordAwal[x]))
print("")
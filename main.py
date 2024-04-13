from PlotFunction import grafic
import matplotlib.pyplot as plt
from ReadExel import Exel

exel1 = Exel('C:\\Users\\Vlad\\Desktop\\ME12.xlsx')
#exel2 = Exel('C:\\Users\\Vlad\\Desktop\\SCFO\\EE-lab\\EE11.xlsx')



# Values from exel :

# ME :

U10 = exel1.extractColom(0, 2, 10)
I10 = exel1.extractColom(1, 2, 10)
P10 = exel1.extractColom(2, 2, 10)
U102 = exel1.extractColom(3, 2, 10)
cosf10 = exel1.extractColom(4, 2, 10)
P10prim = exel1.extractColom(5, 2, 10)

Usc = exel1.extractColom(0, 13, 25)[::-1]
Isc = exel1.extractColom(1, 13, 25)[::-1]
Psc = exel1.extractColom(2, 13, 25)[::-1]
cosfsc = exel1.extractColom(3, 13, 25)[::-1]

s = exel1.extractLine(27, 1, 38)
M = exel1.extractLine(28, 1, 2)
n = exel1.extractLine(29, 1, 38)

#EE :

F = [25,50,75,100]
Rcmas1 = [5.15E-05,5.75E-05,6.50E-05,8.40E-05][::-1]
Rcmas2 = [4.15E-05,4.75E-05,6.00E-05,8.00E-05][::-1]


plt.figure(1)

#plt.plot(Ie1, I1, 'go', markersize=3, label='Original points')


grafic(U10,I10,'b')

plt.axis([0, 420, 0, 6])
plt.title('I10 = f(U10)')
plt.xlabel('U10 [V]')
plt.ylabel('I10 [A]')
plt.grid()

plt.figure(2)

grafic(U10,P10,'b')

plt.axis([0, 420, 0, 440])
plt.title('P10 = f(U10)')
plt.xlabel('U10 [V]')
plt.ylabel('P10 [W]')
plt.grid()

plt.figure(3)

grafic(U10,cosf10,'b')

plt.axis([0, 420, 0, 0.3])
plt.title('cosf10 = f(U10)')
plt.xlabel('U10 [V]')
plt.ylabel('cosf10')
plt.grid()

plt.figure(4)

grafic(U102,P10,'b')
grafic(U102,P10prim,'r')

plt.axis([0, 161000, 0, 440])
plt.title('P10 = f(U10^2)')
plt.xlabel('U10^2 [V^2]')
plt.ylabel('P10 [W]')
plt.grid()

plt.figure(5)

grafic(Usc,Isc,'b')

plt.axis([0, 110, 0, 12])
plt.title('Isc = f(Usc)')
plt.xlabel('Usc [V]')
plt.ylabel('Isc [A]')
plt.grid()

plt.figure(6)

grafic(Usc,Psc,'b')

plt.axis([0, 110, 0, 900])
plt.title('Psc = f(Usc)')
plt.xlabel('Usc [V]')
plt.ylabel('Psc [W]')
plt.grid()


plt.figure(7)

grafic(Usc,cosfsc,'b')

plt.axis([0, 110, 0, 0.5])
plt.title('cosfsc = f(Usc)')
plt.xlabel('Usc [V]')
plt.ylabel('cosfsc')
plt.grid()

#EE

plt.figure(8)

grafic(F,Rcmas1,'b')
grafic(F,Rcmas2,'r')

plt.axis([0, 120, 0, 9.00E-05])
plt.title('Rcmas = f(F)')
plt.xlabel('F [N]')
plt.ylabel('Rcmas [Ω]')
plt.grid()

plt.show()


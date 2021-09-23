import matplotlib.pyplot as mtp

fig, ax= mtp.subplots()

mtp.title("clase")
mtp.xlabel("tiempo")
mtp.ylabel("Velocidad")

x=[1,2,3,4,5]
y=[]

for i in x:
    func=(4*i)+3
    y.append(func)


ax.plot(x,y)
ax.bar(x, [2,3,4,5,6])

mtp.grid()
mtp.show()
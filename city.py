import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.collections import PathCollection
from matplotlib.legend_handler import HandlerPathCollection, HandlerLine2D

X_shiraz = [-52]
Y_shiraz = [29]

X_tehran = [-51]
Y_tehran = [35]

X_karaj = [-50]
Y_karaj = [34]

X_isfahan = [-51]
Y_isfahan = [32]

X_yazd = [-54]
Y_yazd = [31]

X_tabriz = [-46]
Y_tabriz = [38]

X_mashhad = [-59]
Y_mashhad = [36]


plt.scatter(X_karaj,Y_karaj, color="darkblue", label="Karaj", s=2000)
plt.plot([-50,-50],[28,34],linestyle="dashed", color="darkblue")
plt.plot([-60,-50],[34,34],linestyle="dashed", color="darkblue")

plt.scatter(X_yazd,Y_yazd, color="blue", label="Yazd", s=800)
plt.plot([-54,-54],[28,31],linestyle="dashed", color="blue")
plt.plot([-60,-54],[31,31],linestyle="dashed", color="blue")

plt.scatter(X_tehran,Y_tehran, color="royalblue", label="Tehran", s=5000)
plt.plot([-51,-51],[28,35],linestyle="dashed", color="royalblue")
plt.plot([-60,-51],[35,35],linestyle="dashed", color="royalblue")

plt.scatter(X_shiraz,Y_shiraz, color="lightsteelblue", label="Shiraz", s=1000)
plt.plot([-52,-52],[28,29],linestyle="dashed", color="lightsteelblue")
plt.plot([-60,-52],[29,29],linestyle="dashed", color="lightsteelblue")

plt.scatter(X_isfahan,Y_isfahan, color="slateblue", label="Isfahan", s=3000)
plt.plot([-51,-51],[28,32],linestyle="dashed", color="slateblue")
plt.plot([-60,-51],[32,32],linestyle="dashed", color="slateblue")

plt.scatter(X_tabriz,Y_tabriz, color="mediumpurple", label="Tabriz", s=600)
plt.plot([-46,-46],[28,38],linestyle="dashed", color="mediumpurple")
plt.plot([-59,-46],[38,38],linestyle="dashed", color="mediumpurple")

plt.scatter(X_mashhad,Y_mashhad, color="darkorchid", label="Mashhad", s=3500)
plt.plot([-59,-59],[28,36],linestyle="dashed", color="darkorchid")
plt.plot([-60,-59],[36,36],linestyle="dashed", color="darkorchid")

plt.xlabel("East",fontsize = 20, color= 'midnightblue')
plt.ylabel("North",fontsize = 20, color= 'midnightblue')

plt.title("The geographical position of the big cities of Iran",fontsize = 25, y= 1.03)


plt.xticks(ticks=[-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59])
plt.yticks(ticks=[28,29,30,31,32,33,34,35,36,37,38,39])


def updatescatter(handle, orig):
    handle.update_from(orig)
    handle.set_sizes([64])

def updateline(handle, orig):
    handle.update_from(orig)
    handle.set_markersize(8)

plt.legend(handler_map={PathCollection : HandlerPathCollection(update_func=updatescatter),
                        plt.Line2D : HandlerLine2D(update_func = updateline)})
plt.show()

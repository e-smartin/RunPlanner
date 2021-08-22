import numpy as np
import matplotlib.pyplot as plt
def main():
    try :
        initialMark = float(input("Introduce your current distance:\n"))
        desiredMark = float(input("Introduce your desired distance:\n"))
    except: 
        print("Introduce valid parameters")
        exit(1)
    if initialMark <= 0:
        print("Your initial distance should be > 0, it is recommended that you run 7 days before introducing your initial distance")
        exit()
    if desiredMark <= initialMark :
        print("You already achieved that mark")
        exit()
    x = np.arange(365)
    y = 1.01**x * initialMark

    xcte = -1
    for i in range(len(y)):
        if y[i] >= desiredMark:
            xcte = i+1
            break

    if xcte == -1:
        print("You won't achieve it in less than 365 days")
    else:
        print(f"You'll achieve it in {xcte} days if you follow the next graph")
        np.savetxt('dailyplanning.txt', y[:xcte], fmt='%1.3f')
        xcut = np.zeros(x.size) + xcte
        ycut = np.zeros(x.size) + desiredMark
        plt.figure()
        plt.plot(x,y)
        plt.xlabel('days')
        plt.ylabel('distance')

        scale_fact = 10
        xmin, xmax = plt.xlim()
        ymin, ymax = plt.ylim()
        plt.xlim(0, xcte + scale_fact)
        plt.ylim(0, desiredMark + scale_fact)
        plt.plot(xcut,x)
        plt.plot(x,ycut)
        plt.show()


if __name__ == '__main__':
    main()

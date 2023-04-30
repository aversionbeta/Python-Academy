import matplotlib.pyplot as plt

def bar_chart():
    labels = ['A', 'B', 'C']
    values = [10, 20, 30]

    fig,ax = plt.subplot()
    ax.bar(labels,values)
    plt.show()

if __name__ == '__main__':
        bar_chart()


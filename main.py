from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importing dataframe
epl_df = pd.DataFrame(pd.read_csv("EPL_20_21.csv"))
new = epl_df.groupby(['Club']).sum()


# Generating and designing the graph

def generate_graph(x_data):
    sns.set(rc={'figure.figsize':(20,7.5), 'font.size': 20})
    plt.plot(x_data, marker = 'o', markerfacecolor = 'r', color = 'green')
    plt.title(f'Graph of Total {x_clicked.get()}',fontsize = 20)
    plt.xlabel('Teams',  fontsize=20)
    plt.ylabel(f'Number of {x_clicked.get()}', fontsize=20)
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=90, fontsize=18,style='oblique')
    plt.yticks(fontsize=18, style='oblique')
    plt.show()

# GUI
root = Tk()
root.geometry('400x400')

# Label
my_label = Label(text='Premier League 2020-21 Analysis', font=('Arial', 16, 'bold'))
my_label.pack(expand=1)
# my_label.place(x=100, y=100)

# x_values
x_clicked = StringVar()
x_clicked.set("Pick a Football Statistic")
x_values = ['Goals', 'Assists','Yellow_Cards', 'Red_Cards', 'Penalty_Goals', 'Passes_Attempted']
x_drop = OptionMenu(root, x_clicked, *x_values)
x_drop.pack()


def button_clicked():
    generate_graph(new[x_clicked.get()])
    #print(x_clicked.get())

button = Button(root, text="Generate Graph", command=button_clicked)
button.pack(expand=1)

root.mainloop()
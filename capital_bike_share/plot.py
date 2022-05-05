import matplotlib.cm as cm
import matplotlib.pyplot as plt

def scatterplot(df, x_dim, y_dim, x_size, y_size, category, xmin, xmax):
    x = df[x_dim]
    y = df[y_dim]
    fig, ax = plt.subplots(figsize=(x_size, y_size))
    
    #defining an array of colors  
    colors = ['#2300A8', '#00A658']  #assigns a color to each data point
    ax.scatter(x, y, alpha=0.70, c= df[category], cmap=cm.brg)
    ax.set_xlim(left=xmin, right=xmax)
  
    #adds a title and axes labels
    #ax.set_title('Distance vs Workout Duration')
    # ax.set_xlabel('Distance (Km)')
    # ax.set_ylabel('Workout Duration (min)')
  
    #removing top and right borders
    # ax.spines['top'].set_visible(False)
    # ax.spines['right'].set_visible(False)#adds major gridlines
    # ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)plt.show()

    plt.show()

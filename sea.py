import seaborn
import matplotlib.pyplot as plt

tips_data = seaborn.load_dataset('tips')
flights_data = seaborn.load_dataset('flights')

def barplott_tips():
    seaborn.barplot(data=tips_data, x='time', y='tip', hue='sex')
    plt.title("рахунок за час дня")
    plt.xlabel("час")
    plt.ylabel("рахунок")
    plt.show()
    
# barplott_tips()

def lineplot_titanic():
    seaborn.lineplot(data=flights_data, x='year', y='passengers')
    plt.title('Кількість пасажирів у літаках за роками')
    plt.xlabel('Роки')
    plt.ylabel('К-сть пасажирів')
    plt.legend()
    plt.show()
    
# lineplot_titanic()

def describe():
    print(tips_data['total_bill'].describe())
    
describe()
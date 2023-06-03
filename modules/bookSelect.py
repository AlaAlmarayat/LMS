# from modules.database import getTopGenres,insert
# from bookSearch import *
from matplotlib import pyplot as plt
import numpy as np

from modules.database import selectTopGenres
# from modules.database import selectTopGenres

# selectTopGenres(bookTransactionHistoryFilePath)    
bookTransactionHistoryFilePath='.\\files\\Book_Transaction_History.txt'


# --------------------------------bookSelectPage---------------------------------------- #
def bookSelectPage():
    """
    generate book recomendation page
    """
    global bookIdEntry,genreEntry,titleEntry,authorEntry,purchasePriceEntry,purchaseDateEntry
    # rootS = Tk()
    # rootS.title("Show Recommended Books")   
    # rootS.geometry("750x700+400+50")  
    # rootS.resizable(0, 0)       
    # background(rootS,"Add Book")
    
    logList = [
        ["1","1003", "Sci-fi", "Stars",  "author_1",  "available",  "1/8/2010" ,  "1/8/2010" ],
        ["2","1004", "Fantacy", "Aliens?",  "author_2",  "not available",  "1/8/2010" ,  "1/8/2010" ],
        ["3","1003", "Math", "Simple Math",  "author_3",  "available",  "1/8/2010" ,  "1/8/2010" ],
        ["4","1003", "English", "Eng 101",  "author_4",  "available",  "1/8/2010" ,  "1/8/2010" ],
        ["5","1003", "Novel", "Witcher",  "author_1",  "not available",  "1/8/2010" ,  "1/8/2010" ],
        ["10","1003", "Novel", "Witcher",  "author_1",  "available",  "1/8/2010" ,  "1/8/2010" ],
        ["100","1003", "Novel", "Witcher",  "author_1",  "available",  "1/8/2010" ,  "1/8/2010" ],
        ["9","1003", "Novel", "Witcher",  "author_1",  "available",  "1/8/2010" ,  "1/8/2010" ],
        ["88","1003", "Novel", "Witcher",  "author_1",  "available",  "1/8/2010" ,  "1/8/2010" ],
        ["44","1009", "English", "Eng 101",  "author_4",  "not available",  "1/8/2010" ,  "1/8/2010" ],
        ["99","1006", "Math", "Simple Math",  "author_3",  "not available",  "1/8/2010" ,  "1/8/2010" ],
        ["93","1007", "Math", "Simple Math",  "author_3",  "available",  "1/8/2010" ,  "1/8/2010" ],
    ]
    # data['Social_Media_Popularity'] = (data['num_user_for_reviews']/
    #                                data['num_voted_users'])*data['movie_facebook_likes']

    # lets also check the Top 10 Most Popular Movies on Social Media
    # x = logList.sort_values(by = 'ID', ascending = False).head(10).reset_index()
    print(logList)
    genreDictionary=selectTopGenres(bookTransactionHistoryFilePath)
    # -------------- bar chart
    # x = range(1,5)
    # y = range(1,5)
    # plt.bar(x, y, fill=True, hatch='/')
    # plt.show()

    # --------------- pie chart 

    # data = np.random.rand(5)
    # patches = plt.pie(data)
    # patches
    # hatches = ['o' if value==min(data) else 'O' if value==max(data) else '' for value in data]
    # patches = plt.pie(data)
    # for i in range(len(patches[0])):
    #     patches[0][i].set(hatch = hatches[i], fill=False)
    # plt.show()

    plt.rcdefaults()
    fig, ax = plt.subplots()
    # for key in list(genreDictionary.keys()):
    # #    print(key, ":", genreDictionary[key])
    #     people = (key)
    #     performance = genreDictionary[key]
    genreDictionarySorted = dict() 

    sortedList = sorted(genreDictionary.items(), key=lambda item: item[1], reverse=True)
    # sorted_tuples = sorted(dict1.items(), key=lambda item: item[1])
    print(sortedList)  # [(1, 1), (3, 4), (2, 9)]
    genreDictionarySorted = {key: value for key, value in sortedList}

    genre = list(genreDictionarySorted.keys())
    count = list(genreDictionarySorted.values())
    
     # Example data
    # people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
    y_pos = np.arange(len(genreDictionarySorted))
    # performance = 3 + 10 * np.random.rand(len(people))
    # error = np.random.rand(len(genreDictionary))
    # count.sort(reverse=True)

    ax.barh(y_pos, count,  align='center')
    ax.set_yticks(y_pos, labels=genre)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Popularity based on number of Rheckouts/Returns')
    ax.set_title('Most Popular Book Genre')

    np.random.seed(19680801)

    plt.show()

    # rootS.mainloop()
# --------------------------------bookSelectPage---------------------------------------- #


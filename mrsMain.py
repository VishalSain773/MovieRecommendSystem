import random;

lines = open('movies.csv', encoding = 'utf-8', errors ='ignore').read().split('\n')

# Creating a dictionary that maps each line and its id
movieData = []
for line in lines:
    movieData.append(line.split(','))

#Generate movieNameIdDictionary
movieNameList = {}
for line in movieData:
        movieNameList[line[0]]=line[1]

#Generate movieGenreIdDictionary
movieGenreList = {}
for line in movieData:
        movieGenreList[line[0]]=line[2]


#Function to get the list of 20 random numbers
def Rand(start, end, num): 
    res = [] 
  
    for j in range(num): 
        res.append(random.randint(start, end)) 
  
    return res

start = 0;
end = 200;
number = 20;

#create random nuber list to get the data from movieIdList
randomNumberIdsList = []
randomNumberIdsList = Rand(start, end, number)

movieNamesToShow = []
for list in randomNumberIdsList:
     for i in movieNameList.keys():
         if int(i) == int(list):
             movieNamesToShow.append(movieNameList[i]);


for idx, value in enumerate(movieNamesToShow):    
    print(idx+1,value)

movieSelected = int(input("Enter the movie number you want to rate :"))

print("You Selected the movie :", movieNamesToShow[movieSelected-1]);
print("How many stars you want to give to this movie? (1-5)")


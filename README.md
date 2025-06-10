# 9DataScienceRepo
Bonjour. This repository is going to contain all the work done in the data science topic in year 9 2025. Enjoy. (Note that any work that is only code will not be shown here, the task is in the code)

## Activities A
### Part 1

| Raw Data               | Data Type  | Information                                                   |
|------------------------|------------|---------------------------------------------------------------|
|5.8                     |Float       |Weather app, amount of rainfall in mm forecasted for today     |
|"S"                     |String      |Tier list of popular guitarists (in this case, probably Slash) |
|27°C                    |String      |Weather app, as forecasted temperature for tomorrow            |
|"Green"                 |String      |Survey data, a students favourite colour                       |
|True                    |Boolean     |Help part of an app, when a user asks if a product is available|
|40                      |Integer     |Average age of an Australian                                   |

### Part 2

Scenario 1: A school tracks student lateness  
1) Floats, most likely how many minutes late a student is per day  
2) It shows how good the student is, and whether the student should be punished for it or not
3) The student could be punished, either by detenetion or suspension if the number is high enough

Scenario 2: A fitness app tracking steps    
1) Integers, how many steps have been taken
2) It shows how active a person is per day
3) The person could choose to increase or decrease the amount of steps they do per day

### Part 3
![Dataflow Diagram of Youtube Analytics](/dataflow.png "Dataflow Diagram of Youtube Analytics")  

### Part 5

|Example                 |Source             |Why It's Collected                                                                                                 |Who Uses It                 |
|------------------------|-------------------|-------------------------------------------------------------------------------------------------------------------|----------------------------|
|Temperature             |Weather App        |To see how hot it will be, whether someone should wear light or warm clothes                                       |Public                      |
|Creek Levels            |Meteorology Website|To check if it might flood due to increasng river heights, to predict floods (weathermen)                          |Public, Weathermen          |
|Listening Habits        |Music App          |To predict what kind of music a person listens to, allowing for accurate music discovery                           |Prediction Software         |
|Watching Habits         |Youtube/Video App  |To see what a person is interested in, allowin for accurate predictions of what that person would want to listen to|Prediction Software         |
|Forecast                |Weather app        |To see if someone should stay inside because it's raining, or go outside because it's sunny                        |Public                      |
|Cookies                 |Websites           |To remember a user's details, allowing for a more personalised experience                                          |Websites                    |
|Age                     |Census             |To find things like the average age of an Australian, allowing for things more tailored to the population          |The Government              |


### Part 6
There are many benefits to analysing data. One major aspect is it can be used for predictions, like what the weather will be, when there'll be a natural disaster, or just for personalisation of apps. There isn't anything I didn't know was data, as I use a lot of data myself in my free time. If I could collect data in anything, it would be AI usage, as I'm curious as to who uses it and why.

## Activities C
### Part 1
There are 15 columns in the dataset. Of them, 3 of the most prominent is the ID, City, and Event columns. The ID column shows the identification number of the athlete, the City column shows what city they're from, and the Event column shows what event they participated in. The first 5 rows show the athletes with the lowest ID numbers, along with things like height and weight, what games they participated in, and the events they participated in.

### Part 2
According to the code, there are 196,594 male athletes compared to only 74,522 female athletes. The top 5 sports are Athletics, Gymnastics, Swimming, Shooting, and Cycling (in that order).

### Part 3
The average age of an athlete is 25. The youngest was just 10 years old, and the oldest was 97. There are no columns with missing values, although the mean ID was 68,246, despite the fact that you can only get 1 ID.

### Extension
URS was used by the USSR (Soviet Union) from 1900-1912, GDR was used for the German Democratic Republic (East Germany) for a period of time after WWII, and FRG was used for the Federal Republic of Germany at the same time.

### Reflection
I learnt the different abbreviations for countries and things like the age range and averages. There is nothing I found challenging about pandas, and I would love to look at analysing music data next.

## Filtering, Sorting, and Grouping
### Part 1
These filters give results for a particular category, such as only female athletes, or only athletes older than 35. The `.head()` function returns the first 5 rows. 

### Part 4
Athletics had the most female athletes, with 11666 athletes participating in it

### Reflection
The easiest filtering techniques were the basic ones, filtering by one category. The most difficult one was when you tried to sort something by 2 or 3 categories, like men by height and weight. I was surprised how many child athletes there were, I was only expecting 100 or 200 at most, by there were many more. This kind of analysis could help answering questions about what country is the greatest of them all (at least sports wise).

## Week 3 Part 2
### Referencing Parent and Sub-Directories
For this, I created 3 throwaway CSV files, `innie.csv`, `outtie.csv`, and `innie2.csv`. The purpose of these was to grab data from files outside of the directory, such as in the main while the script was in a folder, or from a file in a completely different folder that's in the same directory as the folder that contains the main script. The script I used, `script.py`, was housed in the `Week 3` folder with `innie.csv`, `outtie.csv` was in the main folder, and `innie2.csv` was in a different folder called `Week 2` (Note that the Week 2 folder does not contain any scripts/files from Activities B or C, it is just a placeholder name to use when pulling files from other folders). 

### Internal Data & Importing/Exporting Data Files
Internal data is useful, as when used in an app (for example), it can draw data from the app, then export it as a `.csv` file that can be viewed by humans, which can also be imported into other programs to manipulate that data and make predictions with it. 

## Week 4
### Part 1
The 3 columns with the most missing data is Medal, Height, and Weight. This happens in real-world Olympic data, as not everyone wins medals, and Height and Weight can either not be recorded, or be lost to time, as they are from previous Olympics that have no remaining records.

### Part 2
The code removed 206,853 rows from the dataset. The pros of dropping data is that it helps when you have to use the average of a dataset, and the missing values mess with the result, but the cons are that you miss data that could affect any data trying to be pulled from it, like for the dataset being used, it could ruin a dataset based on which country had the most gold medals.

### Part 3
Using `.median()` instead of `.mean()` means that the data will be replaced with the middle value, not the average.

### Part 5
Cleaning did improve the datset, as there were no inconistent or missing values. Questions on who has the youngest athletes or most gold medals can be answered more accurately.

### Reflection
The dirtiest column was medals, as a lot of athletes did not win anything. The best time to drop data was if there was no saving it, like when age or medals was missing, but height and weight were good ones to fix. Data  cleaning is very important, as it allows accurate predictions for things that need it, for example the weather.

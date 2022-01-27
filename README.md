# SPAN-BE-Coding-Test

This application takes game scores as input and creates a ranking table for a league.



1. The input is taken from a file and saved in a variable
###### Input Format:
```
Team Name <score>, Team Name <score>
Team Name <score>, Team Name <score>
Team Name <score>, Team Name <score>
...
```
3. The input is split by each new line
4. Each line is split by Team Name, Team Score
5. The points is calculated for each team.
``` 
TIE = 1 point 
WIN = 3 points 
LOSE = 0 points
```
6. The points is saved in a dictionary
7. The dictionary is formatted into strings and saved in a file.

###### Output Format:
```
1. Winning Team, <winning team points> pt(s)
2. Second Place, <points> pt(s)
3. Third Place, <points> pt(s)
...
```


If a team's points is tied, they bouth will have the same rank, but sorted in alphabetical order.

Plurals will be corrected.

###### Example:
```
1. Baboons, 2 pts
1. Monkeys, 2 pts
3. Apes, 1 pt
```



This python file consists of 4 functions:

```py
read_file() # Read game information
fix_spaces() # Format information, enable support for team names with spaces
points_calc() # Calculate team points
update_leagues() # Save the team's data
format_league() # Format the leagues
```


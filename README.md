# Football Manager 24 Analysis 
So following the conclusion of the 2023/2024 season and Jurgen Klopp's final season at Liverpool Football Club I thought why not create a project that simulates life after Klopp and whether I would be a suitable replacement for the outgoing manager. What better way to test my managerial skills than starting a new save on the popular game Football Manager 24 (FM24).  
In this new project I will resume the duties as Liverpool FC, due to the limitations in the game I'll be starting my managerial career in the 2023/2024 season.  
Following each season I'll analyse player data collated throughout the season and analyse areas of weakness in the squad to make informed decisions on players to Sell/Release and which areas of the pitch that require strengthening.  
In the first season of this save I will not be making any transfers in or out to try and capture the realism of the 23/24 season that has already concluded. This however, will only be possible for Liverpool FC transfers as the game will simulate all the other clubs in the world and whereby they will continue to make transfers in the January transfer window of the first season. Injuries in the first season will also not be able to refleft the real life senarios that played out in real life.  
FM allows you to copy and paste squad data from the "Squad" screen where you can specify the columns to be included. The copied columns can then be pasted into either a text file, html file or printed outright. In this project we will save all the data into a .html file and utilise Pandas and bs4 to parse the .html file into a usable dataframe to perform data analysis. The data collected includes 75 different statistics metrics that can all be used to make informed decisions on which players to keep the following season. (Each of the abbreviations will be described in a seperate file soon).  
Each of the players individual attributes will also be saved into a html file to conduct analysis on judging the ability of the current squad and new players to scout and sign. 
At the start of each of the season sections below I'll briefly summarise the team performance in all competition, important results that occured within the season, what formations were used - how successful they were, as well as what formations we were weak against. (This information can be found in the data tab within the game, I will try to include snapshots of each of these.)  
## Season 23/24
### Formation
For this save I decided to choose a 4-2-3-1 (2DM) formation taking inspiration from the Liverpool squad back in 08/09 season when the red's were managed by Rafa Benitez, with some minor modifications to the system. Rafa tended to use a more attacking left full back and a defensive right back. In this system to utilise the ability of Trent Alexander-Arnold I decided to utilise two attacking full backs, to balance the change in the right hand side of the pitch, I made the right sided Centre Defensive a more defensive role to allow Trent to roam forward.  
![4-2-3-1 (2DM) Used for the 2023/2024 Season!](images/starting_formation.PNG)
### January Transfer Window 
At the start of the January transfer window after pulling a 7 point gap at the top of the Premier League, the key objective of this window was to improve the squad depth within the midfield. A injury ravaged first 6 months where at one point there were 8 first team players unavailable, reinforcements were desperately needed.
#### Paulo Dybala
After scouting Europe Paulo Dybala popped up on the radar, the 30 Year old had a release clause of £10.5m which seems like a bargin price for todays market. This signing had very little analysis behind and was purely decided on by the price tag of the player. In terms of how he fits into the squad he would be utilised as a squad player who could slit into the number 10 position (AMC) or as a deputy striker. A good option to have as the first 6 months of this save has been ravaged by injuries across the squad. 
#### Xaver Schlager 
A 26 Year-old Defensive Midfielder, similar to Dybala, Schlager had little analysis into the decision to bring him to the club other than he also had a relatively low release clause. For Schlager his release clause was £30m, which again is a bargin for the age and the ability of the player. In terms of how he fits into the system, he would likely slot into the left of the two defensive midfielders alongside Mac Allister, meaning that unfortunately Endo will have to take up a squad role going forward.  
### Season Summary
#### Premier League
Starting the season strong going unbeaten until November with a 1-0 loss against Crystal Palace, in the lead up to January only dropping points in 4 matches, an injury ravaged squad was in desperate need on reinforcements, Paulo Dybala was bought in for £10.5m and Xaver Schlager for £30m the two signings brought in fresh energy to push on in the Premier League. More domination followed in January, Febuary and March. However, a sticky spell at the start of April saw us draw 3 games in a row allowing nearby teams to squeeze the pressure, closing the gap to only 2 points at one point. Following this small blimp more domination followd as we finished the season with 90 points (28W, 6D, 4L) bringing home the Premier League Title for the 20th time. 
#### Europa League
Running out comfortable winners in the Europa League finals with a 3-0 win against strong Atalanta team, We topped Group D, winning every game available to us, qualifying in the top spot with two games to spare allowed us to rotate the team for the dead weight fixtures and focus attention to the other competitions around us.  
The R16 saw us drawn against AEK Athens who were no match for us as we strolled through winning 5-0 after two legs, The quater finals saw us drawn against a strong AC Milan side and after a 3-2 away at the San Siro, We managed to turn the defecit at Anfield with a comfortable 4-0 win putting us through to the Semi-finals. Into the last four and drawn against another strong Itallian side in AS Roma, Paulo Dybala returning to Rome to face his former side, the first leg - at Anfield resulted in a rout, putting 6 past AS Roma with them only putting one past Alisson, a strong start to the Semi-Final reducing the pressure on the second leg, where a slightly weakend side was fielded. Dybala started the match and scored in the 16th minute against his former side, with the tie finishing 1-1 (7-1 Agg). And through to the final with a routine 3-0 win against Atalanta 
#### FA Cup
The FA Cup saw us stroll straight through to the final with little resistance with wins against Cardiff City, Everton and Fulham. A Wembley date against Manchester City saw a tight final with the scores finishing 1-1 after 90 minutes. Into the extra time following a closely contested match Mo Salah scored the winning goal with 4 minutes left on the clock bringing home the FA cup.
#### League Cup
The league cup saw us join the compertition in the 3rd round. Drawn against Fulham a tricky start to the competition awaited a nil-nil draw in regulation time meant a penalty shootout, where we narrowly won the contest. The 4th round saw us line up against Aston Villa another tricky ficture which we won narrowly again with a 2-1- victory away from home. Into the quater-finals and Portsmouth were next up, a mixture of youth and experience saw us waltz through to the Semi-Finals with a comfortable 3-0 win. The Semi-Final, two legs as the competition starts to get serious, drawn agains Manchester United, a trickly tie was expected but in reality it was nothing of the sort, a first leg at Anfield saw us thrash our North-West rivals 7-1 basically putting the tie to bed before the final wistle even sounded, the second leg came around and full rotation was on the cards, trust was put into the reserve players who narrowly lost out in a 1-0 defeat at Old Trafford putting us through to the Final with all of the damage coming in the first leg.  
The Final and the first bit of silverware available to us, saw us face Norwich City a championship club who defied all odds in the semi-final beating Premier League side Chelsea 3-2 over two legs. A team not to be underestimated, a strong XI was selected for the finals resulting in possibly the largest winning margin in the League Cup final. 6-0 and the League cup comes back to Liverpool. 
### Post-Season Analysis
#### Top Performers
#### Contract Renewals
Following the end of the season, there are three first squad players who's contracts are due in the summer: Joel Matip, Thiago and Adrian.  
There are another 3 players who's contracts expire in 2025 (Next Season): Caoimhin Kelleher, Virgil van Dijk and Mo Salah.
##### Joel Matip 
##### Thiago
##### Adrian
#### Transfer Strategy 
With the arrivals of Paulo Dybala and Xaver Schlager, the summer transfer window. A focus on slimming down the squad to comply with home-grown players both in the Premier League and the Champions League is the focus of this window. In terms of incoming signings youth players will always be welcome, but players brought in for the first team, home-grown status will be the primary focus in this transfer window. Post-season there is already interest from the Saudi Pro League for Mo Salah and Virgil van Dijk. Both players are in their 30s and while they are crucial players in the current squad, I expect there will be little I can do to convince both the players to stay.

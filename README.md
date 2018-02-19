### 1. Team

* Iiro Kumpulainen
* Alex Savia
* Tuomas Väisänen


### 2. Goal

Goal of the project is an online game store for JavaScript games.
The service has two types of users: players and developers. 
Developers can add their games to the service and set a price for it. 
Players can buy games on the platform and then play purchased games online.



### 3. Plans
We will implement all of the mandatory requirements and hopefully some of the extra features.
As of now the extra features we will implement if we have time are: Own game, 3rd party login and save/load and resolution feature.


#### 3.1. Priorities

We will prioritize doing the mandatory requirements listed in the project guide.
Once we have completed all of them we can move onto doing more features.
First we will complete basic player and developer functionalities then authentication and game/server interaction.

#### 3.2 Implementation
**Authentication**  
Authentication for the service is implemented using Django auth.   

**Basic player functionalities**  
Buy games:  
Purchasing games will be done using the course’s mockup payment service.  

Play games:  
The selected game is displayed in an iframe to the player.  

Find games:  
Finding games is made easy for the user by grouping the games by category.  

Security restrictions:  
We will ensure that the player is only allowed to play the games they’ve purchased. 
This is done by storing the purchased games for each user in the database and by comparing the django model to see if they allowed access.  

**Basic developer functionalities**  
Add game, set price and manage game:  
New games are added to the inventory by giving the price and a link to an URL of the game, which is an HTML file that is displayed in an iframe to the player.
The games can be managed on a separate page which allows removal and price changes.

Basic game inventory and sales statistics: 
The developers will be able to see how many of the developers' games have been bought and when. 
This is implemented by storing each purchase in the database.  

Security restrictions:  
We will ensure that developers are only allowed to modify/add/etc. their own games, developer can only add games to their own inventory, etc.
This is done by storing all the owned games for each developer in the database and by comparing the django model to see if they allowed access.  

**Game/service interaction**  
postMessage interaction:  
The game/service interaction is implemented using a simple message system with JSON data. 
Game and the game service communicate with window.postMessage. 
All the messages contain a messageType attribute, which are implemented as outlined in the project guide.

#### 3.3 Django models

We will have models for players, developers, games and purchases. 
The player and developer models will be extended from the existing Django user model. 
The players will have fields for their login information and relations to the games they have bought.
The developers will have fields for their login information and relations to the games they manage.
The games will have fields for their information and information related to their sales.
The purchases will have fields for the customer and the game that is being bought.

### 4. Process and Time Schedule

We will start doing the project at the beginning of next year.
We plan on working atleast 8 hours per week on the project and we will meet in-person atleast once a week every tuesday.
We plan to have the minimun requirements completed by 4.2.2018 and after that we'll start working on more features.

* Weeks 1-2: Work on Basic player functionalities and Basic developer functionalities
* Weeks 3-5: Working on other core functionality like Authentication and Game/service interaction
* Weeks 6-7: Extra features and Final report

#### 4.1 Work methods

We will use the git as a project management tool. 
We have a telegram group set-up for communication between team members and we are meeting face-to-face every tuesday.

### 5. Quality of work

**Quality of code:**  
We will ensure good code quality by focusing on reusability, modularity and good commenting in the code.  
In addition, we will be reviewing each other's code.

**User experience:**  
We aim to make the user interface intuitive and clean. We also plan to ask for input from people outside the project.  

**Meaningful testing:** 
We will test all features manually as we develop them. 
In addition, we will test that everything works properly once the feature is complete.
We will especially pay attention to testing the security of the software by attempting to circumvent the basic security, e.g. acquiring other user’s session/credentials, privilege escalation, injection attacks etc.

## FINAL SUMBMISSION

### Features we implemented
#### Mandatory requirements
**Authentication:**  
We didn't have any problems except having two different roles to register as so we implemented registering as a developer through the user profile page.
Otherwise we were successful with all other aspects of this feature so we would give ourselves 200 points.  
**Basic player functionalities:**  
We successfully implemented the payment service, security restrictions, game functionalities and categories for different games. 
Therefore, we would give ourselves 300 points.
**Basic developer functionalities:**  
Only minor problems we had were thinking where we should handle the security restrictions. After we resolved that we were successful in all other requirements
We implemented everything required well so we would give ourselves 200 points.  
**Game/service interaction:**  
We had no major problems implementing the game/service interaction for saving high scores as well as save/load features including messages from the service to the game.
The game/service interaction works well and satisfies all requirements. Thus, we would give ourselves 200 points for this.
#### Extra features
**Save/load and resolution feature:**  
Initially, we had some problems saving JavaScipt objects properly to the database.
Eventually, we found the solutions, and the game state can be saved to the server using a save button, and the game can be continued from the save using the load button.
As this works well and fulfills all requirements, we would give ourselves 100 points.
**3rd party login:**  
We didn't have any problems since the 3rd party Django app we used had good tutorials. Only minor problem was thinking how to de-link social media accounts and handle passwords.
We implemented multiple sites and all requirements so we would give ourselves 200 points.  
**RESTful API:**  
Only problem was that the requirements given were a bit vague so it was hard to know how exactly you wanted us to implement this feature.
Otherwise everything went well so we would give ourselves 100 points.  
**Own game:**  
We implemented a nice simple JavaScript game that communicates with the service for high scores, as well as saving and loading from a save.
We would give ourselves 100 points for this.
**Mobile Friendly:**  
Our web application is mobile friendly, as the top bars and game lists we made to dynamically adjust to varying game sizes.
However, mobile users might not be able to play some games, if the game developer has not created the game to be mobile friendly.
Other than that, our website is usable on mobile devices, and we would give ourselves 50 points for this.
**Social media sharing:**  
Problem was with twitter that you can't get images unless your URL is approved to use "cards" so we had to use a regular tweet that has data about the game but no picture.  
Otherwise the social media sharing feature works well so we would give ourselves 50 points.

### Division of work
Tuomas implemented authentication, developer features, 3rd party login, RESTful API and social media sharing.
Iiro implemented most basic player functionalities, payment service and own game as well as handled heroku deployment.
Alex implemented game list, game page, game/service interaction and templates.

We feel that the division of work was successful and everyone did approximately the same amount of work.
We also utilized pair programming for development at our weekly meetings.

### How to use
The web application is deployed at https://powerful-hamlet-41538.herokuapp.com/
Registering a new user requires email-authentication, but we use Django's Console Backend as advised in the project description.
Threfore, instead of creating a new account, you may use the following accounts to test the service:  
**Developers: (username, password)**  
**Users: (username, password)**  
The users can gain developer status through the profile page.
The games can be browsed and grouped by category using the top bar.
When logged in, the users may purchase games or play owned games from the game list.
Developers can add, modify and delete their games from the profile page.

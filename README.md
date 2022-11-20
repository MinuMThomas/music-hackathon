# Clue the Music!


![Mock-up of site]()


If you love music and games then this is the one for you! Test your listening skills and get as many points as possibly by guessing the song or instrument with as little help as you can. The less clues the more points you keep. Can you Clue the Music? 

Deployed website can be viewed [here]().

## Project Goals

'Clue the Music' has been developed as part of the Code Institute Hackathon Hero: A music themed game creation challenge. This is a Django based project with a sqlite database, alongside HTML, CSS and JavaScript. We worked together to create something fun for people to play! 

## UX Design

## Strategy Plane

### Site Owner Goals


### Demograghic
- Everyone with an interest or love for music
- All ages and demographics


### User Stories
As a player:
- I want to be able to understand the aim of the game easily.
- I want to easily navigate through the site.
- I expect exciting, attractive and user friendly design.
- I want to be able to login into my account, so that I can see my previous scores.
- I want to hear an audio clip when I click the play button.
- I want to be able to submit an answer.
- I want to be able to reveal clues to help me guess the answer.
- I want to be able to read about the developers of the game.
- I want to be able to see my final score once the game is over.

## Scope Plane

### **Existing Features**
- Game is styled in a fun, exciting and user friendly way
- Game name is displayed and intro message
- Easy navigation around the site allows for a positive user experience
- Home page displays 'Login' and 'How to Play' buttons
- Question mark button opens a modal, which explains the aim of the game to the player
- Login functionality allows users to login to play the game
- Once users logged in, 'Start Game' button displayed, which allows users to play the game
- Logout option displayed on hamburger menu
- Play button for each question to play music
- Clue buttons allow player to reveal a clue to help them guess the answer
- At the end of the game, after 10 questions, the players score is diplayed
- Exit/ Home button displayed so players can leave the game at any time

### **Features Left to Implement**
- Logged in users are able to view a history of their score
- Leaderboard displayed of the top 10 scores from all players
- Clock countdown displayed per question to add a pressure element to the game
- Additional levels added to allow players to play easy, medium or hard to test their musical ears.


## Structure Plane 

### Database

## Skeleton Plane

### Wireframes

## Surface Plane

### Colour Scheme

### Images
The landing page image and graphics of the guitar and musical score are in keeping with the music theme and provide an eye-catching design for the user. 

There were selected from...

### Typography
'Rubik Distressed' was chosen as the title font on the landing page. It is a fun font, that is inviting for the user. 'Poppins' was chosen as the font for the rest of the site, as it is an easy-to-read font, making sure it is clear for the user. Both fonts were chosen using [Google Fonts](https://fonts.google.com/).

## Technologies

### Languages
- HTML
- CSS3
- JavaScript
- Python

### Frameworks and Libraries

- [Am I Responsive?](http://ami.responsivedesign.is/) was used to create the mock ups.
- Git was used for version control ad to push code to GitHub.
- [GitHub](https://github.com/) was used to store the repository.
- [GitPod](https://www.gitpod.io/) was used as the IDE to develop the project.
- [Google Fonts](https://fonts.google.com/) were used to select fonts for the site.
- [Heroku](https://www.heroku.com/) used to deploy the site.

## Challenges

## Testing

## Deployment

### Creation
* Following logging into my GitHub account, I created the repository from Code Institute's Gitpod Template. Selected 'Use this template', filled in repository name and created repository.

### Forking
* Sign into your GitHub account and go to this [repository](). 
* In the top right there are several options, including 'fork'. Select this to fork the repository.

### Cloning
* Sign into your GitHub account and go to this [repository](). In addition to the cloning steps you will need to follow steps for setting up AWS, Stripe and Heroku.
* Clone using command line
    - Select button 'Code' next to Gitpod button and copy the URL
    - In your workspace terminal type 'git clone' followed by the URL and press enter
* Clone using Desktop GitHub
    - If you select this, it will guide you through the necessary steps

For more information on troubleshooting see the GitHub documentation [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#about-cloning-a-repository).



### Heroku Deployment
* Firstly login into your [Heroku](https://id.heroku.com/login) account.
* Select 'New' and then 'Create New App', give it a name and select closest region and click 'Create App'.
* In Resources under Add-ons select 'Heroku Postgres'

* Once the app is created, go to settings and reveal Confif Vars and add the following:
    * Note: the DATABASE_URL was already populated, USE_AWS is set to True and the AWS_SECRET_KEY was generated using the Django Secret Key Generator. 

* Go to 'Deploy' and select 'Heroku Git'. Currently Heroku has stopped automatic deploys with GitHub
* Once deployed commits need to be manually pushed to both GitHub and Heroku. Using the command git push heroku main will push to Heroku
* You will need to migrate and create a superuser. Migrations can be done with the previous steps with 'heroku run' infront. E.g heroku run python3 manage.py makemigrations.




## Credits

### Content
- README structure and basic layout used from [Surf the Wave](https://github.com/anyahush/surf-the-wave).


### Code Content
- [Stack Overflow](https://stackoverflow.com/questions/22766719/stop-audio-after-x-seconds-in-js) used in JavaScript to play audio files
- [Stack Overflow](https://stackoverflow.com/questions/27474321/how-to-shuffle-list-in-django-views-py) used in shuffling songs





### Images


## Acknowledegments




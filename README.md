# Clue the Music!

![Mock-up of site]()

If you love music and games then this is the one for you! Test your listening skills and get as many points as possibly by guessing the song or instrument with as little help as you can. The less clues the more points you keep. Can you Clue the Music? 

Deployed website can be viewed [here]().

## Project Goals


## UX Design

## Strategy Plane

### Site Owner Goals


### Demograghic
- Everyone with an interest or love for music
- All ages and demographics


### User Stories

## Scope Plane

### **Existing Features**


### **Features Left to Implement**

## Structure Plane 

### Database

## Skeleton Plane

### Wireframes

## Surface Plane

### Colour Scheme

### Images

### Typography

## Technologies

### Languages
- HTML
- CSS3
- JavaScript
- Python

### Frameworks and Libraries

- [Am I Responsive?](http://ami.responsivedesign.is/) was used to create the mock ups.
- [Font Awesome](https://fontawesome.com/) was used for button icons.
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




### Images


## Acknowledegments




# ML-TTT

A Machine Learning game of TicTacToe using python, django, a little javascript, css, html and postgres.

## Introduction

This project started out life during week 9 of the Maker's Academy coding bootcamp. The initial repo can be found [here](https://github.com/SimonTanner/machine-learning). This was the first week we were given the opportunity to come up with some ideas for a project that would last a little less than a week. Brimming with optimism and the desire to learn, we decided to attempt to write a game that would allow you to play against a Machine Learning player. Our initial research into the field of ML led us to choose python as it seems to be the language most widely used and suited to ML. This also lead us to choose Django as framework for creating the web application. This posed a problem for us all since prior to that I was the only one who'd used python and none of us had ever used Django, but we were eager to learn and experiment.

Whilst we didn't get all that far in the space of a week, I did get an idea of how to approach creating the code that would allow the "machine player" to learn how to play and hopefully improve over time, after a few days reading about the subject. What became apparent to me was that it needed to be able to build a decision tree which stored a value for the likelihood of a particular choice leading to a win. This tree would start with a state set of all the possible options and have an associated value which would be added to in the case of a win. It was hoped that over time this data structure would show peaks for the best choices which would become more and more accurate the more it played.

## Hurdles

After Maker's I decided I wanted to use this project as a way to learn some django. That said learning a new framework is not without its challenges...

The first problem I encountered was how do I get the Machine Player which is running on the server to send the information to the user when it's taken its turn. The answer was a little bit of javascript added to the page which automatically reloads the page when it's the MP's turn.

Ok that problem solved and I thought time to try and deploy it to heroku and actually get it to run on a server. This lead to problem no. 2. Having never attempted to deploy a django/python app I became very aware of how much more complicated this was was than when using nodejs or ruby. I'd never heard of a procfile or gunicorn, both of which were required to get the app up and running. Once I'd worked out how to do this I pushed to heroku. No luck. It took a day of trying everything I could think of and some serious googling, but still the build kept failing... I started to get a feeling that the initial folder structure might be to blame and indeed it was. So I started a new repo (this one) with what I thought would be the correct structure, and finally a build actually succeeded!

So I finally got it up and running on heroku! But then came the next obstacle. I'd started playing a game but then when I selected a choice it was as though the game had a mind of its own. It definitely was not working how it was when I ran the server locally. This was when I realised that multi-process environments and multiple servers mean you don't just reconnect to the instance of a game class that you previously initialised, instead you might get connected to a server which has no idea of the game you just started, every time you make a request. After a lot of research I realised I needed a way to store these instances. Caching them in the memory using memcache meant I could do this! Finally I thought I'd found the solution.

I was wrong, in part. I had found the right path, but the size of the data needed by the MP, way exceeded the limit on the server. This created the next hurdle: converting the MP class to use a database to store the decision tree data. So I created my models, using the default sqlite3 that django creates for you, created a new class to handle accessing the data and writing it, ran it locally and everything worked. Until I tried pushing to heroku. At this point I learnt that heroku doesn't support sqlite :(... Luckily it does support postgres and after a little configuration I set up the app to use this.

Finally, it actually worked! Now time to make the MP better...

To play the current version of ML-TTT please click [here](https://ml-ttt.herokuapp.com/)

## Next Step

Implementing a way of training the MP through the website so users can compare the MP when it hasn't played many games compared to when it has.

Testing different models to explore how changing values, such as how much you add to value associated with an option after a win, affects how well that player performs and how quickly it learns.

## Testing

To run the functional tests you have to be in the root folder and simply enter python manage.py test into the command shell.

To run the unit tests again from the root folder enter python manage.py test --pattern="*_test.py"
This will run all tests with _test.py in their name.

Small Batch Artisanal Bots: Let's Make Friends
==============================================

* https://us.pycon.org/2016/schedule/presentation/2175/
* Elizabeth Uselton
* @lizuselton

Bots can be as simple or complex as you want. Great for beginners.

Things making bots taught her:
* APIs
* OAuth
* Virtual Machines
* AWS
* Scheduled background jobs

What kinds of bots? Jokes! Chat! Twitter! 

Paragons of Botdom
------------------
Some great bots:
* @StealthMountain
* @viralhulk
* @oliviataters
* @HinkyPinkyQs and @hinkyPinkyAs
* @erowidrecruiter
* @congressedits

OAuth
-----
Your secret handshake with Twitter:
* consumer key and secret
* access token and secret

Use the REST API - expand into the streaming API later, maybe.

The Web UI Part
---------------
Create an account for your bot: https://apps.twitter.com

Use a Twitter library, or just call the API yourself. Whatever sounds more fun.

`tweepy`: good docs and lots of examples

Data!
-----
Sweet data sets:
* civic data
 * pros
  * lots of data
  * its open
 * cons
  * can be poorly formatted
  * poorly maintaned
 * like a bargain bin
 * https://data.seattle.gov
* scraping
 * the internet is your data set
 * pros
  * any data can be yours
  * can get new data automatically
 * cons
  * a little more work
  * websites can change
  * some people don't like it
 * `mechanize`: can complete forms
 * `BeautifulSoup`
* corpora
 * pros
  * ready made
  * you can add to the community by making your own
 * cons
  * this isn't always one for what you want
  * hard to find a central location
 * Amazon Datasets
 * Darius Kazemi
 * Project Gutenberg
 * Natural Language Toolkit...
* NLTK
 * can help your bot almost speak english
 * tokenize and tag text
 * includes some sample corpora
 * has:
  * sentiment analysis
  * pronunciation keys
  * synonyms
  * deep, weird linguistics stuff
  * tools for building your own corpora
 * Markov chains
  * probabilities of a word following another word
* Twitter
 * pros:
  * so much data
  * already integrating with Twitter, anyway
  * in bite sized chunks perfect for tweeting
 * cons:
  * people on the internet are terrible
  * keep a blacklist of words!

Running your Bot
----------------
AWS EC2 micro
* free for a year
* minimal setup
* learn to use a VM

Easiest way to run your script is a cronjob.

Bot Etiquette
-------------
* Don't harass people
* don't advertise
* cause more joy than annoyance
 * opt in, not opt out
* show off with #botALLY

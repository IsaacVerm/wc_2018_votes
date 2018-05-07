# run with python3 manage.py shell
from votes.models import Game
import csv
import os

path =  "/home/ec2-user/environment/wc_2018_votes/votes/data/" # Set path of new directory here
os.chdir(path) # changes the directory

with open('fixtures.csv') as csvfile:
     reader = csv.DictReader(csvfile, delimiter=';')
     for row in reader:
          game = Game(round = row['round'], date = row['date'], home_team = row['home_team'], away_team = row['away_team'])
          game.save()

from django.db import models

# Create your models here.
import datetime
YEAR_CHOICES = [(r,r) for r in range(2000, datetime.date.today().year+1)]

class Matches(models.Model):
    id = models.AutoField(primary_key=True)
    season = models.IntegerField(choices=YEAR_CHOICES)
    city =  models.CharField(max_length=200)
    date = models.DateField()
    team1 = models.CharField(max_length=200)
    team2 = models.CharField(max_length=200)
    toss_winner = models.CharField(max_length=200)
    toss_decision = models.CharField(max_length=200)
    result = models.CharField(max_length=200)
    dl_applied =  models.BooleanField()
    winner = models.CharField(max_length=200)
    win_by_runs = models.IntegerField()
    win_by_wickets = models.IntegerField()
    player_of_match = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    umpire1 = models.CharField(max_length=200)
    umpire2 = models.CharField(max_length=200)
    umpire3 = models.CharField(max_length=200)


class Deliveries(models.Model):
    id = models.AutoField(primary_key=True)
    match_id = models.ForeignKey(Matches,on_delete=models.CASCADE)
    inning =  models.IntegerField()
    batting_team = models.CharField(max_length=200)
    bowling_team = models.CharField(max_length=200)
    over = models.IntegerField()
    ball = models.IntegerField()
    batsman = models.CharField(max_length=200)
    non_striker = models.CharField(max_length=200)
    bowler =  models.CharField(max_length=200)
    is_super_over = models.BooleanField()
    wide_runs = models.IntegerField()
    bye_runs = models.IntegerField()
    legbye_runs = models.IntegerField()
    noball_runs = models.IntegerField()
    penalty_runs = models.IntegerField()
    batsman_runs = models.IntegerField()
    extra_runs = models.IntegerField()
    total_runs =  models.IntegerField()
    player_dismissed = models.CharField(max_length=200)
    dismissal_kind = models.CharField(max_length=200)
    fielder = models.CharField(max_length=200)

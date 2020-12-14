from django.shortcuts import render

# Create your views here.
from django.conf import settings
import logging
from django.http import HttpResponse
from django.shortcuts import (render, redirect)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
import pandas as pd
from app.models import Deliveries,Matches
from django.db.models import Count,Sum

def home_view(request):
    return render(request,'data.html')

def load_data(request):
    deliveries = pd.read_csv("../static/deliveries.csv")
    print(deliveries)
# Make a row iterator (this will go row by row)
    iter_data = deliveries.iterrows()
    insert_data=[]
    if len(Deliveries.objects.all())==0:
        objs = [

        Deliveries(

        match_id = row['match_id'],
        inning =  row['inning'],
        batting_team = row['batting_team'],
        bowling_team = row['bowling_team'],
        over = row['over'],
        ball = row['ball'],
        batsman = row['batsman'],
        non_striker = row['non_striker'],
        bowler =  row['bowler'],
        is_super_over = row['is_super_over'],
        wide_runs = row['wide_runs'],
        bye_runs = row['bye_runs'],
        legbye_runs = row['legbye_runs'],
        noball_runs = row['noball_runs'],
        penalty_runs = row['penalty_runs'],
        batsman_runs = row['batsman_runs'],
        extra_runs = row['extra_runs'],
        total_runs =  row['total_runs'],
        player_dismissed = row['player_dismissed'],
        dismissal_kind = row['dismissal_kind'],
        fielder = row['fielder']

        )

        for index, row in iter_data

        ]
        
            
        Deliveries.objects.bulk_create(objs)
    #print(map(lambda i,data : Deliveries.save**dict(data)),iter_data))
    matches = pd.read_csv("../static/matches.csv")
# Make a row iterator (this will go row by row)
    iter_data2 = matches.iterrows()
    if len(Matches.objects.all())==0:
        objs = [

        Matches(

        season = row['season'],
        city =  row['city'],
        date = row['date'],
        team1 = row['team1'],
        team2 = row['team2'],
        toss_winner = row['toss_winner'],
        toss_decision = row['toss_decision'],
        result = row['result'],
        dl_applied =  row['dl_applied'],
        winner = row['winner'],
        win_by_runs = row['win_by_runs'],
        win_by_wickets = row['win_by_wickets'],
        player_of_match = row['player_of_match'],
        venue = row['venue'],
        umpire1 = row['umpire1'],
        umpire2 = row['umpire2'],
        umpire3 = row['umpire3']

        )

        for index, row in iter_data2

        ]
        
            
        Matches.objects.bulk_create(objs)
    return render(request,'data.html')

def get_data(request):
    year=request.GET['year']
    print(year)
    top_teams=Matches.objects.filter(season=int(year)).values_list('winner').annotate(truck_count=Count('winner')).order_by('-truck_count')[0:4]
    toss_winner=Matches.objects.filter(season=int(year)).values_list('toss_winner').annotate(truck_count=Count('toss_winner')).order_by('-truck_count')[0]
    top_player=Matches.objects.values_list('player_of_match').annotate(truck_count=Count('player_of_match')).order_by('-truck_count')[0]
    top_team=Matches.objects.values_list('winner').annotate(truck_count=Count('winner')).order_by('-truck_count')[0]
    top_team_win_location=Matches.objects.filter(winner=top_team[0]).values_list('venue').annotate(truck_count=Count('venue')).order_by('-truck_count')[0]
    toss_winner_teams_count=len(Matches.objects.values_list('toss_winner').annotate(count=Count('toss_winner')))
    toss_winner_bat_count=len(Matches.objects.filter(toss_decision="bat").values_list('toss_winner').annotate(count=Count('toss_winner')))
    percent_bat_toss=(toss_winner_bat_count/toss_winner_teams_count)*100
    most_location=Matches.objects.filter(season=int(year)).values_list('venue').annotate(truck_count=Count('venue')).order_by('-truck_count')[0]
    team_high_margin = Matches.objects.filter(season=int(year)).order_by('win_by_runs')[0].winner
    team_high_wickets = Matches.objects.filter(season=int(year)).order_by('win_by_wickets')[0].winner
    bowler_gave_away_runs = Deliveries.objects.filter(match_id_id__season=int(year)).values_list('batsman').annotate(total=Sum('batsman_runs'))[0]
    no_catches_most = Deliveries.objects.filter(match_id_id__season=int(year),dismissal_kind='caught').values_list('fielder').annotate(total=Count('dismissal_kind'))[0]
    matches=Deliveries.objects.all()
    print(no_catches_most)
    return render(request,'data.html',{'year':year,'top_teams':top_teams,"toss_winner":toss_winner,"top_player":top_player,"top_team":top_team,"top_team_win_location":top_team_win_location,"percent_bat_toss":percent_bat_toss,"most_location":most_location,'team_high_margin':team_high_margin,
    'team_high_wickets':team_high_wickets,'bowler_gave_away_runs':bowler_gave_away_runs,'no_catches_most':no_catches_most})
    
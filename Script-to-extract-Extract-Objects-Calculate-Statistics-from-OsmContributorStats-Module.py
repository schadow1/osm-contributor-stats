#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
#========================================================================="
# https://github.com/schadow1/osm-contributor-stats/blob/master/Script-to-run-OsmContributorStats-Module-Extract-Objects-Calculate-Statistics.py
# Jared Cortez, 05-2016
# Example running version 0.2 of OsmContributorStats
# OSM Contributors History Statistics, for a specific bbox zone and date range (e.g Philippines)
#========================================================================="
#========================================================================="
"""
import os, datetime
from filter import open_csv
# replace below with the directory where both OsmApi.py and OsmContributorStats.py are stored
os.chdir('c:\OsmContributorStats\\')
import OsmApi
# Instantiation classe OsmApi
osmApi = OsmApi.OsmApi(debug=False)
import OsmContributorStats
# Instantiation classe OsmContributorStats
ContributorStats = OsmContributorStats.OsmContributorStats(rep='/home/jed/Desktop/osm-contributor-stats',lang="en",debug=False)
dir(ContributorStats)

start = datetime.datetime.now()
#===============================================================================
# users :  array of contributor ID's or Name by team - if no users, all users in the bbox will be selected
users=[None]*2
users[0] = [""]
users[1] = [""]

"""
Example with nicknames
users=[None]*2
users[0] = ["abc","def","gjol"]
users[1] = ["zyx","avb Yul"]
"""
#prefix+from_date+"-"+to_date+"_changeset_hist_list.txt comparison file
#prefix+from_date+"-"+to_date+".csv csv
prefix = "#ProjectNOAH"
from_date = "yyyy-mm-dd"
to_date = "yyyy-mm-dd"
output_file = "*.csv"
input_file = prefix+from_date+"-"+to_date+".csv"
comparison_file = prefix+from_date+"-"+to_date+"_changeset_hist_list.txt"

# Example - Lome, Togo
# The examples below defines a Bbox covering Lome, Togo. The period covered si from 2013-06-26 to 2013-06-27.
  
# Step 1 - Extract History Data  - Extraire les données historiques
ContributorStats.API6_Collect_Changesets(team_from=0,team_to=0,from_date=from_date,
    to_date=to_date,
    min_lon=116,max_lon=128,min_lat=4,max_lat=22,
    prefix="#ProjectNOAH",users=users)

# Step 2 - Statistics from data stored locally	- Statistiques produite à partir des données enregistrées localement
ContributorStats.Changesets_Contributor_Statistics(team_from=0,team_to=0,from_date=from_date,
    to_date=to_date,
    min_lon=116.0,max_lon=128.0,min_lat=4.0,max_lat=22.0,
    prefix="#ProjectNOAH",users=users)


print "\n-----------------------------------------------------"
open_csv(output_file,input_file,comparison_file)

ContributorStats.__del__()
del OsmContributorStats

import sys
sys.exit('\n=== Travail complété ===')

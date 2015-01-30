#!/usr/bin/python
#
# orgit (by Joe Siwiak) 
#
# This program is non-free software; This program is licensed under a 
# Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 
# International License for more details.
# You should have received a copy of the Creative Commons 
# Attribution-NonCommercial-NoDerivatives 4.0 International 
# License along with this program; if not, visit:
# http://creativecommons.org/licenses/by-nc-nd/4.0/
#
#   Copyright 2014 Blue Hat Innovations <kf4jas@gmail.com>
#

import argparse, pprint, os

import repotdepot, sys

__author__ = 'Joseph Siwiak'

parser = argparse.ArgumentParser(description='This is a demo script Joe.')
parser.add_argument('action', action="store",help='install, setup, create, promote, backup, learn, search')
parser.add_argument('item', action="store", help='repo_dir, backup_mount, search_string')
parser.add_argument('-d','--debug', action='store_true', help='Debug the shit',required=False)
parser.add_argument('-c','--client', nargs=1, help='Client Folder in the Work Folder',required=False)
parser.add_argument('-p','--ppath', nargs=1, help='Change the which folder the system gets promoted to (work, learn, fun) default: local',required=False)

args = parser.parse_args()

## Remove trailing '/' from directory if there
if args.item[::-1][0] == '/':
	args.item = args.item[:-1]
	#print args.item


## Sets up the folders to either your user directory or a defined one later. 
if args.action == 'setup':
	if args.item == 'install':
		setupe = repotdepot.setupEnv()
		setupe.createALLDirs()
	else:
		print "So ... you need to use the 'orgit setup install' command"
		#udir = '/'+args.item
		#setupe = repotdepot.setupEnv(args.item)
		#setupe.createALLDirs()

## Creates the repo in the rsch direcory
elif args.action == 'create':
	research = repotdepot.depotcrtl('rsch')
	research.create(args.item,['README.md','LICENSE','notes.md'])

## Moves and Stores whatever file name to the appropriate folder by extension
elif args.action == 'store':
	research = repotdepot.depotcrtl('rsch')
	research.storefile(args.item)
	
## Promotes the repo from rsch to local (or work or learn or w.e. if the -p option is made) as well as saving it in an encrypted store
elif args.action == 'promote':
	research = repotdepot.depotcrtl('rsch')
	if not args.ppath:
		research.promote(args.item,"local")
	elif "work" in args.ppath:
		userdir = research.getuserdir()
		workingdir = userdir+"work"
		if not args.client:
			for f in os.listdir(workingdir):
				print f
			client = raw_input("Which Client folder? ")
		else:
			client = args.client[0]
		clientdir = workingdir+"/"+client
		if not os.path.exists(clientdir):
			os.makedirs(clientdir)
		locwork = "work/"+client
		research.promote(args.item,locwork)
	elif 'learn' in args.ppath:
		research.promote(args.item,"learn")
	else:
		print args.ppath,"does not exist"
## Runs Backup procedure based on the promoted folder (local, work, w.e.)
elif args.action == 'backup':
	research = repotdepot.depotcrtl('rsch')
	research.massivepush([args.item])

## Searches through the name of the repo as well as the README.md first line (title) and third line (description) 	
elif args.action == 'search':
	o = []
	research = repotdepot.searchrepos(args.item)
	if research.walk_dirs() != None:
		o = research.walk_dirs()
	print research.showsearch(o)
else:
	print "Not something i'm going to do."




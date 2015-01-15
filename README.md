orgit
=========
This is a little tool I built to create and organize my code and daily life in a linux box in git hub repos

## Install

```
git clone orgit
cd orgit
sudo make install
```

## Usage

```
orgit <action> <item>
```


The Urban Dictionary defines an orgit as:
orgit. n. A midget that has been dipped in a vat of fake tanning solution. Derived from the words orange midget. 

"Orgits don't take up space in tanning salons ..."


### Actions (item)
* create
  `orgit create <repo name>`
  This is used to create a new repo in the rsch folder
* promote
  `orgit promote <repo name>`
  this is used to promote the rsch repo to local
  you can use the -p switch to change the working dir to something else (like work or learn or fun)
* setup
  this allows you to either 
  `orgit setup install # for $USER directory`
  or 
  `orgit setup <pick userdir>`
* backup <userdir>
  `orgit backup <userdir>`
  this allows you to push your repos from which ever 
  
### More to come
still need to come up with the search, the index

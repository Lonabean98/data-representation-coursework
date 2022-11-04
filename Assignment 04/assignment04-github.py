from github import Github
from config import config as cfg
import requests

# define the github key from config so we don't have to keep it in this file
apikey = cfg["githubkey"]

# using the access token
g = Github(apikey)

# Get and print repos beloing to the user of this github key
#for repo in g.get_user().get_repos():
#    print(repo.name)

# Get and clone the Assignment 4 repo
repo = g.get_repo("Lonabean98/Assignment-04")
#print(repo.clone_url)

# Get contents of the text file and store in a variable
fileInfo = repo.get_contents("test.txt")

# Download and print the url of this text file
urlOfFile = fileInfo.download_url
#print (urlOfFile)

# Send a get request to this url and store in variable.
response = requests.get(urlOfFile)

# Get the text contents of the file and print 
contentOfFile = response.text
#print (contentOfFile)

# Replace all instances of string "Andrew" with "Lonan"
newContents = contentOfFile.replace('Andrew', 'Lonan')
#print (newContents)

# Update the contents of the file with text file path, commit message and  new content 
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog", newContents, fileInfo.sha)

print (gitHubResponse)

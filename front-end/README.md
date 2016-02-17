JumboCode Spring 2016 Front End


How to Setup the Server:

1. Install Python 3/Pip if you haven't
2. Pull the repo from the server (git pull)
3. Install and create a virtual env (sudo pip install virtual env)
3b. cd into the repo and create a virtual environment (virtualenv -p python3 env)
4. Start your virtualenv (source env/bin/activate)
5. Install dependencies (pip install -r requirements.txt)
6. Run the server: (python manage.py runserver)
7. Visit your webserver: http://localhost:8000/

Notes: If it tells you to migrate, run (python manage.py migrate). This commits your database changes

During Development:
1. Create a remote branch for development (this helps with merging stuff)
1b. Go to github, under branch, create your own name as your development branch
1c. When you're committing, commit to your own branch; when your changes are ready to go, merge your development branch with master (there may be merge conflicts)
2. Create a local branch that keeps track of the remote branch (git fetch; git checkout "YOURNAMESAMEASTHEBRANCHYOUMADE")
3. In your new local branch (You can see what branch you're on with git branch); pull the changes from master with (git pull origin master), there may be merge conflicts. If there were new commits from master, run git push to sync up your local development branch with the server development branch
4. Do work. (commit and stuff)
5. When done and ready to commit to master, push everything to the server development branch; merge your own development branch with master, push your local master branch 
5b. (git branch) make sure you're on your developmental branch
5c. (git push origin YOURNAME) if necessary
5d. 



Tips
1. Run (git status) all the time
2. Commit often, there's always ways to go back 
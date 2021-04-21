# News Analytics

## Technologies
- Python
- Flask
- PostgreSQL
- Redis
- NLTK
- NewspaperAPI

## What News Analytics does
Use the Newspaper API to scrape news article via URL
Use PostgreSQL to store results
Use Redis to Cache
Use NLTK for text analysis

## Using PostgreSQL on Heroku with Python/Flask
1. Create a new app on Heroku
2. Go to Resources, Add-ons, search Heroku Postgres - Use the Hobby Dev since it's free
3. Once Postgres shows as a resource of the app, click the resource and navigate to Settings
4. Click on View Credentials and found the URI link to the database
5. Connect to the remote database using the psql command (PostgreSQL must be installed locally) psql "URI Link"
6. Use PostreSQL syntax to create a new table in the database
7. Use SQLAlchemy to then interact with the table to insert, delete, find, etc

## Training Models
Use bank of true/fake news articles and use Scikit learn to create a model to identify fake news articles
Use pickle to then serialize and deserialize to use with Flask
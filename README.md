# Census Data on State Migration - Web API

This API provides U.S. migration data between states, drawing from yearly census data from years 2010-2019. 
For this application, I have targeted populations who migrated to the state of North Carolina.

## Setup

Step 1. Install dependencies:

```
pip install -r requirements.txt
```

Step 2. Create and run Django migrations
```
python manage.py makemigrations
python manage.py migrate
```

Step 3. Import data from census CSVs
```
python manage.py importdata
```

Step 4. Start local server:
```
$ python manage.py runserver
```

Step 5. Navigate to desired API endpoint:
```
/previous_state/<id>/
/previous_state/<id>/<year>/
/previous_division/<id>/
/previous_division/<id>/<year>/
```

Note that the 'id' parameters for the endpoints listed above correspond to the following values in the 
'census_classification.csv' file in the project directory:
- For the 'previous_state' endpoints, the 'id' parameter will be the chosen state's abbreviation in column 3.
- For the 'previous_division' endpoints, the 'id' parameter will be the chosen state's 'parent_id' in column 5.
- For all endpoints, the 'year' parameter must be within the range of 2010-2019 (four digits, ex: 2010, 2011, etc.).

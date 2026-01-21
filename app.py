
## Install required OS packages##

sudo apt update
sudo apt install python3-full python3-venv -y

## Create a virtual environment##

python3 -m venv venv


## Activate the virtual environment##

source venv/bin/activate

## Install Python dependencies##

pip install sqlalchemy pymysql

## test file(test_db.py)#

from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://<user>:<password>@<rds-endpoint>:3306/myflixdb"
)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM movies"))
    for row in result:
        print(row)

## execute
python test_db.py






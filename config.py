DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DATABASE_URI_FORMAT = "{db_type}://{user}:{password}@{host}/{db_name}"

# Define the database - we are working with
env = os.environ.get('BOT_ENV')
if env == "dev":
    REDIS_HOST = "localhost"
    REDIS_PORT = "6379"
    DB_HOST = "localhost"
    DB_USER = "roopak"
    DB_PASS = "hello"
    DB_NAME = "testdb"
    SQLALCHEMY_DATABASE_URI = DATABASE_URI_FORMAT.format(db_type="mysql", user=DB_USER, password=DB_PASS,
                                                         host=DB_HOST, db_name=DB_NAME)
    print SQLALCHEMY_DATABASE_URI
else:
    REDIS_HOST = "localhost"
    REDIS_PORT = "6379"
    DB_HOST = "localhost"
    DB_USER = "roopak"
    DB_PASS = "hello"
    DB_NAME = "testdb"
    SQLALCHEMY_DATABASE_URI = DATABASE_URI_FORMAT.format(db_type="mysql", user=DB_USER, password=DB_PASS,
                                                         host=DB_HOST, db_name=DB_NAME)
    print SQLALCHEMY_DATABASE_URI

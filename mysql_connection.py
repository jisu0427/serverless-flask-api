import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(host = 'database-1.ckgggmo40ahf.us-east-2.rds.amazonaws.com', 
            database = 'Movie', 
            user = 'movie_user',
            password = '2105'
    )
    return connection
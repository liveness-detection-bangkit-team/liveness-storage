import sqlite3
from datetime import datetime, timedelta

# Create a database to store rate limits
def create_db():
    conn = sqlite3.connect('rate_limit.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rate_limits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip_address TEXT NOT NULL,
            user_id TEXT NOT NULL,
            request_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Function to check if an IP address is rate limited
def is_rate_limited(ip_address, limit=5, period=60):
    conn = sqlite3.connect('rate_limit.db')  # Connect to the database
    cursor = conn.cursor()
    
    # Calculate the time window
    time_window_start = datetime.now() - timedelta(seconds=period)
    
    # Count the number of requests in the time window
    cursor.execute('''
        SELECT COUNT(*) FROM rate_limits 
        WHERE ip_address = ? AND request_time > ?
    ''', (ip_address, time_window_start))
    
    request_count = cursor.fetchone()[0]  # Fetch the count of requests
    
    # If the request count exceeds the limit, return True
    if request_count >= limit:
        conn.close()  # Close the connection
        return True
    
    # Otherwise, log the request
    cursor.execute('''
        INSERT INTO rate_limits (ip_address, user_id) VALUES (?, ?)
    ''', (ip_address, "default_user"))  # Assuming "default_user" as a placeholder for user_id
    
    conn.commit()  # Commit the changes
    conn.close()   # Close the connection
    return False
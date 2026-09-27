import sqlite3

DB = "bot.db"

def setup_database():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        discord_id TEXT UNIQUE NOT NULL,
        twitch_id TEXT UNIQUE,
        youtube_id TEXT UNIQUE
    )
    """)

    conn.commit()
    conn.close()

"""if __name__ == "__main__":
    setup_database()
    print("Database ready")"""
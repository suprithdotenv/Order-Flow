from sqlalchemy import text

from app.database.session import engine



try:

    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

        print("Database connected!")
        print("Result",result.scalar())



except Exception as e:
    print("Database not connected!")
    print(e)








from data import get_db_session
from data.sql_alchemy.tables.tables import User

if __name__ == '__main__':
    session = get_db_session()
    alex = User(chat_id="chat_id", first_name="Alex", age=23, sex="M",
         sex_preference="W", profile_message="babu xochu", town="Warszawa", country="Polska", is_active=True)
    session.add(alex)
    session.commit()
    session.close()

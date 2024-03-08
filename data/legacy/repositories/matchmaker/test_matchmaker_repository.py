import os
import unittest
import asyncio

from data.legacy.database.db_control import DatabaseConnection
from data.legacy.repositories.matchmaker.matchmaker_repository import MatchmakerRepository
from dotenv import load_dotenv
load_dotenv()
HOST, DATABASE, USER, PASSWORD = os.getenv("HOST"), os.getenv("DATABASE"), os.getenv("USER"), os.getenv("PASSWORD")


# temporary solution
class TestMatchmakerRepository(unittest.TestCase):

    def setUp(self):
        # Mock the database connection for testing
        self.mock_conn = DatabaseConnection(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
        self.mock_superior_id = 12

    def test_like_suggestion(self):
        # Test the like_suggestion method
        repository = MatchmakerRepository(self.mock_conn.connection)
        suggestion = asyncio.run(repository.next_suggestion(superior_id=self.mock_superior_id))
        print(suggestion)


if __name__ == '__main__':
    unittest.main()

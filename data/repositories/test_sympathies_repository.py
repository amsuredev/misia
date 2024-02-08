import os
import unittest
from unittest.mock import Mock, patch

from data.database.db_control import DatabaseConnection
from data.repositories.sympathies_repository import SympathiesRepository
from dotenv import load_dotenv
load_dotenv()
HOST, DATABASE, USER, PASSWORD = os.getenv("HOST"), os.getenv("DATABASE"), os.getenv("USER"), os.getenv("PASSWORD")

class TestSympathiesRepository(unittest.TestCase):

    def setUp(self):
        # Mock the database connection for testing
        self.mock_conn = DatabaseConnection(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
        self.mock_superior_id = 11

    def test_like_suggestion(self):
        # Test the like_suggestion method
        repository = SympathiesRepository(self.mock_conn.connection)
        suggestion = repository.next_suggestion(superior_id = self.mock_superior_id)
        a = 5


if __name__ == '__main__':
    unittest.main()

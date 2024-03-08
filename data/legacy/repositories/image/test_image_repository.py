import unittest

from dotenv import load_dotenv

from data.legacy.database.db_control import DatabaseConnection
from data.legacy.repositories.image.image_repository import ImageRepository
import os

load_dotenv()
HOST, DATABASE, USER, PASSWORD = os.getenv("HOST"), os.getenv("DATABASE"), os.getenv("USER"), os.getenv("PASSWORD")


class TestImageRepository(unittest.TestCase):
    def setUp(self):
        self.mock_conn = DatabaseConnection(host=HOST, database=DATABASE, user=USER, password=PASSWORD)

    def test_image(self):
        repository = ImageRepository(self.mock_conn)

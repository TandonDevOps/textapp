from unittest import TestCase

from text_menu.text_menu import main, SUCCESS, TEST_MENU, BAD_CHOICE
from text_menu.text_menu import is_valid_choice, CONTINUE, EXIT


class TextMenuTest(TestCase):
    def test_is_valid_choice(self):
        self.assertTrue(is_valid_choice(CONTINUE, TEST_MENU))
        self.assertTrue(is_valid_choice(EXIT, TEST_MENU))
        self.assertFalse(is_valid_choice(BAD_CHOICE, TEST_MENU))

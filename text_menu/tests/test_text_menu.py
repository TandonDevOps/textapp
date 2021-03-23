from unittest import TestCase, skip

from text_menu.text_menu.text_menu import main, SUCCESS, TEST_MENU, BAD_CHOICE
from text_menu.text_menu.text_menu import is_valid_choice, CONTINUE, EXIT, menu_repr
from text_menu.text_menu.text_menu import MAIN_MENU, exec_choice, main
from text_menu.text_menu.text_menu import data_repr, TEST_DATA, DATA_SET
from text_menu.text_menu.text_menu import run_form, TEST_FORM, TITLE


class TextMenuTest(TestCase):
    def test_main(self):
        self.assertEqual(main(), SUCCESS)

    def test_exec_choice(self):
        self.assertEqual(exec_choice(EXIT, TEST_MENU), False)

    def test_is_valid_choice(self):
        self.assertTrue(is_valid_choice(CONTINUE, TEST_MENU))
        self.assertTrue(is_valid_choice(EXIT, TEST_MENU))
        self.assertFalse(is_valid_choice(BAD_CHOICE, TEST_MENU))

    @skip("This test is stalling for input: must debug.")
    def test_run_formr(self):
        self.assertIn(TITLE, run_form(TEST_FORM))

    def test_menu_repr(self):
        self.assertIn(MAIN_MENU, menu_repr(TEST_MENU))

    def test_data_repr(self):
        self.assertIn(DATA_SET, data_repr(TEST_DATA))

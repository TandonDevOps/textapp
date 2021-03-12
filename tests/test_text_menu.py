from unittest import TestCase

from text_menu.text_menu import main, SUCCESS


class TextMenuTest(TestCase):
    def test_main(self):
        self.assertTrue(main() == SUCCESS)

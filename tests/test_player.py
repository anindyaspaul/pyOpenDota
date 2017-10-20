import logging
import unittest

import sys

from datetime import datetime

from opendota.player import Player

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


class PlayerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.account_id = 243478749
        cls.player = Player(cls.account_id)

    def test_init(self):
        self.assertIsInstance(self.player, Player)

    def test_account_id(self):
        logger.debug("account_id: %s", self.player.account_id)
        self.assertIsInstance(self.player.account_id, int)

    def test_persona_name(self):
        logger.debug("persona_name: %s", self.player.persona_name)
        self.assertIsInstance(self.player.persona_name, str)

    def test_name(self):
        logger.debug("name: %s", self.player.name)
        try:
            self.assertIsInstance(self.player.name, str)
        except AssertionError as e:
            self.assertIsNone(self.player.name)

    def test_cheese(self):
        logger.debug("cheese: %s", self.player.cheese)
        self.assertIsInstance(self.player.cheese, int)

    def test_steam_id(self):
        logger.debug("steam_id: %s", self.player.steam_id)
        self.assertIsInstance(self.player.steam_id, str)

    def test_avatar(self):
        logger.debug("avatar: %s", self.player.avatar)
        self.assertIsInstance(self.player.avatar, str)

    def test_avatar_medium(self):
        logger.debug("avatar_medium: %s", self.player.avatar_medium)
        self.assertIsInstance(self.player.avatar_medium, str)

    def test_avatar_full(self):
        logger.debug("avatar_full: %s", self.player.avatar_full)
        self.assertIsInstance(self.player.avatar_full, str)

    def test_profile_url(self):
        logger.debug("profile_url: %s", self.player.profile_url)
        self.assertIsInstance(self.player.profile_url, str)

    def test_last_login(self):
        logger.debug("last_login: %s", self.player.last_login)
        self.assertIsInstance(self.player.last_login, datetime)

    def test_loc_country_code(self):
        logger.debug("loc_country_code: %s", self.player.loc_country_code)
        self.assertIsInstance(self.player.loc_country_code, str)

    def test_tracked_until(self):
        logger.debug("tracked_until: %s", self.player.tracked_until)
        self.assertIsInstance(self.player.tracked_until, datetime)

    def test_solo_competitive_rank(self):
        logger.debug("solo_competitive_rank: %s", self.player.solo_competitive_rank)
        self.assertIsInstance(self.player.solo_competitive_rank, int)

    def test_competitive_rank(self):
        logger.debug("competitive_rank: %s", self.player.competitive_rank)
        self.assertIsInstance(self.player.competitive_rank, int)

    def test_mmr_estimate(self):
        logger.debug("mmr_estimate: %s", self.player.mmr_estimate)
        self.assertIsInstance(self.player.mmr_estimate, int)

if __name__ == "__main__":
    unittest.main()
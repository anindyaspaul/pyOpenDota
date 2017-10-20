import json
import logging
import requests
from datetime import datetime, timezone

from . import config


logger = logging.getLogger(__name__)


class Player(object):

    BASE_URL = "https://api.opendota.com/api/players/"

    def __init__(self, account_id):
        logger.info("Getting player data for account id: %s", account_id)

        url = Player.BASE_URL + str(account_id)
        logger.debug("url: %s", url)

        response = requests.get(url, timeout=config.TIMEOUT)
        response.raise_for_status()

        data = response.json()

        self.__account_id = data.get("profile").get("account_id", None)
        self.__persona_name = data.get("profile").get("personaname", None)
        self.__name = data.get("profile").get("name", None)
        self.__cheese = data.get("profile").get("cheese", None)
        self.__steam_id = data.get("profile").get("steamid", None)
        self.__avatar = data.get("profile").get("avatar", None)
        self.__avatar_medium = data.get("profile").get("avatarmedium", None)
        self.__avatar_full = data.get("profile").get("avatarfull", None)
        self.__profile_url = data.get("profile").get("profileurl", None)
        self.__last_login = data.get("profile").get("last_login", None)
        if self.__last_login is not None:
            # Store last_login as datetime
            self.__last_login = datetime.strptime(self.__last_login, "%Y-%m-%dT%H:%M:%S.%fZ")
        self.__loc_country_code = data.get("profile").get("loccountrycode", None)

        self.__tracked_until = data.get("tracked_until", None)
        if self.__tracked_until is not None:
            # Store tracked_until as datetime
            self.__tracked_until = datetime.fromtimestamp(float(self.__tracked_until))

        self.__solo_competitive_rank = data.get("solo_competitive_rank", None)
        self.__competitive_rank = data.get("competitive_rank", None)
        self.__mmr_estimate = data.get("mmr_estimate").get("estimate", None)

    @property
    def account_id(self):
        return self.__account_id

    @property
    def persona_name(self):
        return self.__persona_name

    @property
    def name(self):
        return self.__name

    @property
    def cheese(self):
        return self.__cheese

    @property
    def steam_id(self):
        return self.__steam_id

    @property
    def avatar(self):
        return self.__avatar

    @property
    def avatar_medium(self):
        return self.__avatar_medium

    @property
    def avatar_full(self):
        return self.__avatar_full

    @property
    def profile_url(self):
        return self.__profile_url

    @property
    def last_login(self):
        return self.__last_login

    @property
    def loc_country_code(self):
        return self.__loc_country_code

    @property
    def tracked_until(self):
        return self.__tracked_until

    @property
    def solo_competitive_rank(self):
        return self.__solo_competitive_rank
    
    @property
    def competitive_rank(self):
        return self.__competitive_rank
    
    @property
    def mmr_estimate(self):
        return self.__mmr_estimate
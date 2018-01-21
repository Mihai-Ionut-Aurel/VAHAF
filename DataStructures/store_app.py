import json


class StoreAppData:
    def __init__(self,id):
        self.__id = id
        self.__name = None
        self.__url = None
        self.__release_date = None
        self.__ratings_count = 0
        self.__rating = 0
        self.__ratings_count_curr = 0
        self.__ratings_curr_ver = 0
        self.__languages = None
        self.__supported_devices = None
        self.__genre= None

    # Properties
    @property
    def name(self):
        return self.__url

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, val):
        self.__url = val

    @property
    def release_date(self):
        return self.__release_date

    @release_date.setter
    def release_date(self, val):
        self.__release_date = val

    @property
    def ratings_count(self):
        return self.__ratings_count

    @ratings_count.setter
    def ratings_count(self, val):
        self.__ratings_count = val

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, val):
        self.__rating = val

    @property
    def ratings_count_curr(self):
        return self.__ratings_count_curr

    @ratings_count_curr.setter
    def ratings_count_curr(self, val):
        self.__ratings_count_curr = val

    @property
    def ratings_curr_ver(self):
        return self.__ratings_curr_ver

    @ratings_curr_ver.setter
    def ratings_curr_ver(self, val):
        self.__ratings_curr_ver = val

    @property
    def languages(self):
        return self.__languages

    @languages.setter
    def languages(self, val):
        self.__languages = val

    @property
    def supported_devices(self):
        return self.__supported_devices

    @supported_devices.setter
    def supported_devices(self, val):
        self.__supported_devices = val

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, val):
        self.__genre = val

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return str(self.__dict__)

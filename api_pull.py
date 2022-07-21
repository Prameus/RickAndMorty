import requests


class RickAndMorty:

    def all_ricks(self):
        response = requests.get(
            'https://rickandmortyapi.com/api/character/?name=rick')
        request = response.json()
        ricks = request['results']
        print(ricks)
        return ricks

    def all_mortys(self):
        response = requests.get(
            'https://rickandmortyapi.com/api/character/?name=morty')
        request = response.json()
        mortys = request['results']
        return mortys

    def all_summers(self):
        response = requests.get(
            'https://rickandmortyapi.com/api/character/?name=summer')
        request = response.json()
        summers = request['results']
        return summers

    def all_bird_persons(self):
        response = requests.get(
            'https://rickandmortyapi.com/api/character/?name=birdperson')
        request = response.json()
        birdperson = request['results']
        return birdperson

    def all_rick_chapters(self):
        ricks = self.all_ricks()
        episodes = []
        for i in ricks:
            episodes.append(i['episode'])
        return episodes

    def all_morty_chapters(self):
        mortys = self.all_mortys()
        episodes = []
        for i in mortys:
            episodes.append(i['episode'])
        return episodes

    def all_summer_chapters(self):
        summer = self.all_summers()
        episodes = []
        for i in summer:
            episodes.append(i['episode'])
        return episodes

    def all_birdPerson_chapters(self):
        bird_person = self.all_bird_persons()
        episodes = []
        for i in bird_person:
            episodes.append(i['episode'])
        return episodes


rickAndMorty = RickAndMorty()

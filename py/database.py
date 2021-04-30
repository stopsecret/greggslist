
class database():
    db = {
        "save_name":"",
        "sellers":{},
        "listings":{},
    }

    def __init__(self, save_name):
        self.db[save_name] = save_name
        self.load()

    def load(self):
        pass

    def save(self):
        pass

    def add_update_seller(self, seller):
        self.db['sellers'][seller.email] = seller

    def add_update_listing(self, listing):
        self.db['listings'][listing.id] = listing

    def get_seller(self, email):
        if email in self.db['sellers']:
            return self.db['sellers'][email]
        return None

    def get_listing(self, id):
        if id in self.db['listings']:
            return self.db['listings'][id]
        return None

    def remove_seller(self, email):
        self.db['sellers'].pop(email, None)

    def remove_listing(self, id):
        self.db['listings'].pop(id, None)
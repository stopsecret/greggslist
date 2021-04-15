
class listing():
    title=""
    description = ""
    sellerId = ""
    photos = []

    def __init__(self, title, description, sellerId, photos):
        self.title = title
        self.description = description
        self.sellerId = sellerId
        self.photos = photos


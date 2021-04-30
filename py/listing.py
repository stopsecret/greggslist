
class listing():
    id=0
    title=""
    description = ""
    sellerId = ""
    photos = []
    inquiries = 0
    views = 0

    def __init__(self, id, title, description, sellerId, photos, inquiries, views):
        self.id = id
        self.title = title
        self.description = description
        self.sellerId = sellerId
        self.photos = photos
        self.inquiries = inquiries
        self.views = views


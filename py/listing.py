
class listing():
    title=""
    description = ""
    sellerId = ""
    photos = []
    inquiries = 0
    views = 0

    def __init__(self, title, description, sellerId, photos, inquiries, views):
        self.title = title
        self.description = description
        self.sellerId = sellerId
        self.photos = photos
        self.inquiries = inquiries
        self.views = views


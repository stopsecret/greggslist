
class seller():
	name = ""
	email = ""
	password = ""
	ratings = []
	send_text = False
	phone_carrier = ""
	phone_number = ""

	def __init__(self, name, email, password, ratings, send_text, phone_carrier, phone_number):
		self.name = name
		self.email = email
		self.password = password
		self.ratings = ratings
		self.send_text = send_text
		self.phone_carrier = phone_carrier
		self.phone_number = phone_number
import re
import bcrypt

MAX_TEXT_LENGTH = 64
MIN_PASSWORD_LENGTH = 6
MOST_COMMON_PASSWORDS = []
PASSWORD_REQUIRED_SPECIAL = "!@#$%^&*()[]{},.<>/?"
PASSWORD_REQUIRED_NUMBER = "1234567890"

with open("py/resources/most_common_passwords.txt", "r") as f:
	MOST_COMMON_PASSWORDS = f.read().split()
	
class seller():
	name = ""
	email = ""
	password = ""
	ratings = {}

	def __init__(self, name, email, password, ratings):
		self.basic_text_validation(name, "Name")
		self.basic_text_validation(email, "Email")
		self.basic_text_validation(password, "Password")
		self.email_validation(email)
		self.password_validation(password)
		self.name = name
		self.email = email
		self.password = self.get_hashed_password(password)
		self.ratings = ratings
	
	def get_rating(self):
		return sum([self.ratings[key] for key in self.ratings])/len(self.ratings)

	def add_update_rating(self, user, rating):
		self.ratings[user] = rating

	def basic_text_validation(self, field, fieldName):
		if not field:
			raise Exception(f'{fieldName} cannot be null or blank')
		elif len(field) > MAX_TEXT_LENGTH:
			raise Exception(f'{fieldName} must be less than {MAX_TEXT_LENGTH} characters')

	def email_validation(self, email):
		email_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
		if not re.search(email_regex, email):
			raise Exception(f'Email "{email}" is not a valid email address')

	def password_validation(self, password):
		if len(password) < MIN_PASSWORD_LENGTH:
			raise Exception(f'Password "{password}" must be at least {MIN_PASSWORD_LENGTH} characters long')
		has_special = False
		has_number = False
		for special in PASSWORD_REQUIRED_SPECIAL:
			if special in password:
				has_special = True
		for number in PASSWORD_REQUIRED_NUMBER:
			if number in password:
				has_number = True
		if not has_special:
			raise Exception(f'Password "{password}" must have at least 1 of the following special characters: {PASSWORD_REQUIRED_SPECIAL}')
		if not has_number:
			raise Exception(f'Password "{password}" must have at least 1 number')
		
			
		for common_password in MOST_COMMON_PASSWORDS:
			if common_password.lower() in password.lower():
				raise Exception(f'Password "{password}" is not valid, as it is too common')
		
	def get_hashed_password(self, password):
		return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

	def check_password(self, password, hashed_password):
		return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
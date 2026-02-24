from requests import Session

class KimiQuotes:
	def __init__(self) -> None:
		self.api = "https://kimiquotes.herokuapp.com"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}

	def get_all_quotes(self) -> dict:
		return self.session.get(f"{self.api}/quotes").json()

	def get_all_quotes_by_year(self, year: int) -> dict:
		return self.session.get(f"{self.api}/quotes/{year}").json()

	def get_all_unstamped_quotes(self) -> dict:
		return self.session.get(f"{self.api}/quotes/unstamped").json()

	def quote_by_id(self, quote_id: int) -> dict:
		return self.session.get(f"{self.api}/quote/{quote_id}").json()

	def get_random_quote(self) -> dict:
		return self.session.get(f"{self.api}/quote").json()

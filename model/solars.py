from universe import *
bad = '\'()"'

def get_solar(solar_id):
	"""Returns the solar system object by its id"""
	for c in bad:
		if c in solar_id:
			return 'Error: injected sql'
	con = connect()
	con.use('rev1')
	query = """select name, value
	from planets
	where sid='%s'
	""" % solar_id
	planets = con.get_more(query)
	return planets

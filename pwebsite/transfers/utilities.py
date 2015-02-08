# Utility class

def fix_spurscommunity_url(html):
	html = html.replace('index.php?', 'http://www.spurscommunity.co.uk/index.php?')
	return html

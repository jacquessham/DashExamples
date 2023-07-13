# Universal Viz Arg
def check_text(metadata):
	if 'text' in metadata:
		return metadata['text']
	return None

# Universal Viz Arg
def check_textposition(metadata):
	if 'textposition' in metadata:
		return metadata['textposition']
	elif 'text_position' in metadata:
		return metadata['text_position']
	return None

# Universal Viz Arg
def check_textfont(metadata):
	if 'textfont' in metadata:
		return metadata['textfont']
	if 'text_font' in metadata:
		return metadata['text_font']
	return None

# Bar, Boxplot Arg
def check_barcolour(metadata):
	# Allow user to spell English and American English and use of _
	if 'barcolour' in metadata:
		return metadata['barcolour']
	elif 'bar_colour' in metadata:
		return metadata['bar_colour']
	elif 'barcolor' in metadata:
		return metadata['barcolor']	
	elif 'bar_color' in metadata:
		return metadata['bar_color']	
	return None

# Boxplot Arg
def check_boxmean(metadata):
	if 'boxmean' in metadata:
		return metadata['boxmean']
	return None
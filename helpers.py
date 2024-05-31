def formatstr(template, **kwargs):
	return eval(f"f'''{template}'''")

import os
def get_directory_size(directory):
	"""Returns the `directory` size in bytes."""
	total = 0
	try:
		# print("[+] Getting the size of", directory)
		for entry in os.scandir(directory):
			if entry.is_file():
				# if it's a file, use stat() function
				total += entry.stat().st_size
			elif entry.is_dir():
				# if it's a directory, recursively call this function
				total += get_directory_size(entry.path)
	except NotADirectoryError:
		# if `directory` isn't a directory, get the file size then
		return os.path.getsize(directory)
	except PermissionError:
		# if for whatever reason we can't open the folder, return 0
		return 0
	return total

def get_size_format(b, factor=1024, suffix="B"):
	"""
	Scale bytes to its proper byte format
	e.g:
		1253656 => '1.20MB'
		1253656678 => '1.17GB'
	"""
	for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
		if b < factor:
			return f"{b:.2f}{unit}{suffix}"
		b /= factor
	return f"{b:.2f}Y{suffix}"
	return b



# directory = 'C:\\'
directory = r'C:\Users'
directory = r'C:\Users\s-abutler'
directory = r'C:\Users\s-abutler\BIM 360'
# directory = 'C:\ProgramData\Autodesk'
# directory = 'C:\ProgramData\Autodesk\CDX'
# directory = 'C:\ProgramData\Autodesk\CDX\SymLinks'
out = []
for filename in os.listdir(directory):
	# print(filename)
	gds = get_directory_size(os.path.join(directory,filename))
	gsf = get_size_format(get_directory_size(os.path.join(directory,filename)))
	# print(filename,gsf)
	out.append({"size":gds, "name":filename , "f":gsf})

out = sorted(out, key = lambda i: i['size'])
for o in out:
	print(o["name"],o["f"])

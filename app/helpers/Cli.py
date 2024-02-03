class CLIHelper (object):
	def table(self, names, data):
		# column lengths
		column_lengths = []
		for name in names:
			name_length = len(name)
			if name_length < 3:
				name_length = 3
				
			# we will need it later for the column size
			column_lengths.append(name_length)
		
		# names row
		print("| ", end = "")
		for name in names:
			column_length = column_lengths[names.index(name)]
			print(f"{name:{column_length}}", end = " | ")
		print()
		  
		# separator row
		print("| ", end = "")
		for name in names:
			column_length = column_lengths[names.index(name)]
			print("-" * column_length, end = " | ")
		print()
		
		# data rows
		for row in data:
			print("| ", end = "")
			for column in row:
				column_length = column_lengths[row.index(column)]
				print(f"{column:{column_length}}", end = " | ")
			print()

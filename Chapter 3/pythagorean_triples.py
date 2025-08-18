for adjacent in range(1, 20):
	for opposites in range(adjacent, 20):
		for hypothenus in range(opposites, 20):
			if adjacents ** 2 + opposites ** 2 == hypothenus ** 2:
				print(adjacent, opposites, hypothenus)
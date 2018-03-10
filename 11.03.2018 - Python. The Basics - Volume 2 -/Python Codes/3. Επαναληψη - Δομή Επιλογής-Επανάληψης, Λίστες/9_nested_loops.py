rich = False
dead = False
grind = 0

while not rich and not dead:
	print("get rich or die tryin'")
	for attempt in range(10):
		print("it's all about the grind")
		grind += 10
	
	if grind > 80:
		rich = True
		
# Σε τι κατάσταση βρίσκομαι μετά το πρόγραμμα;
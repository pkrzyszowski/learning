#3. Napisać kod transformujący podany słownik:
#	{
#		1: 'Poniedziałek',
#		2: 'Wtorek',
#		3: 'Środa',
#		4: 'Czwartek',
#		5: 'Piątek',
#		6: 'Sobota',
#		7: 'Niedziela',
#	}
#	do postaci:
#	{
#		'Poniedziałek': 1,
#		'Środa': 3,
#		'Piątek': 5,
#		'Niedziela': 7,
#	}
#	Zamiana klucza z wartością i zostawienie tylko dni nieparzystych

week = 	{
		1: 'Poniedziałek',
		2: 'Wtorek',
		3: 'Środa',
		4: 'Czwartek',
		5: 'Piątek',
		6: 'Sobota',
		7: 'Niedziela',
	}

"""First"""
short_week = {i: x for x,i in week.items() if x%2!=0}
print(short_week)

"""Second"""
keys = list(week.keys())
for k in keys:
    if k % 2 == 1:
        week[week[k]] = k
    del week[k]
print(week)
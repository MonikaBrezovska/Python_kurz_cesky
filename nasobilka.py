"""
nasobilka.py
Vypis na monitor malou nasobilku cisel 1-10.
Nasobilku formatuj vzhledove do tabulky.

1	2	3	4	5	6	7	8	9	10
2	4	6	8	10	12	14	16	18	20
...
10	20	30	40	50	60	70	80	90	100
"""

for i in range(1, 11):
	for j in range(1, 11):
		print(f"{i * j:>4}", end = "")
	print()


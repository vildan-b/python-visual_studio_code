medicine = "parol"
dosaj = "5"
duration = "2,5"

instruction= '{} - take {} kere {}'.format(medicine, dosaj, duration)
print(instruction)

instruction= '{2} - take {0} kere {1}'.format(medicine, dosaj, duration)
print(instruction)

instruction= '{medicine} - take {dosaj} kere {duration}'.format(medicine='kedi', dosaj=19, duration=2)
print(instruction)
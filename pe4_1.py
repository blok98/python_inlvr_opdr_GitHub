cijferICOR=6.0
cijferPROG=7.0
cijferCSN=6.0
gemiddelde=round(((cijferICOR+cijferPROG+cijferCSN)/3),1)
beloning=(round(cijferICOR+cijferPROG+cijferCSN)*30)
overzicht='Mijn resultaten zullen mij een gemiddelde van ' + str(gemiddelde) + ' leveren, waarvoor ik een beloning krijg van €' + str(beloning)
print(overzicht)

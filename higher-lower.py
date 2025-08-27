import random

countries_area = [
    {"country": "Russia", "surface": 17098200},
    {"country": "Canada", "surface": 9984670},
    {"country": "United States", "surface": 9833520},
    {"country": "China", "surface": 9596960},
    {"country": "Brazil", "surface": 8515770},
    {"country": "Australia", "surface": 7692020},
    {"country": "India", "surface": 3287260},
    {"country": "Argentina", "surface": 2780400},
    {"country": "Kazakhstan", "surface": 2724900},
    {"country": "Algeria", "surface": 2381740},
    {"country": "DR Congo", "surface": 2344860},
    {"country": "Greenland", "surface": 2166090},
    {"country": "Saudi Arabia", "surface": 2149690},
    {"country": "Mexico", "surface": 1964380},
    {"country": "Indonesia", "surface": 1910930},
    {"country": "Sudan", "surface": 1861480},
    {"country": "Libya", "surface": 1759540},
    {"country": "Iran", "surface": 1648200},
    {"country": "Mongolia", "surface": 1564110},
    {"country": "Peru", "surface": 1285220},
    {"country": "Chad", "surface": 1284000},
    {"country": "Niger", "surface": 1267000},
    {"country": "Angola", "surface": 1246700},
    {"country": "Mali", "surface": 1240190},
    {"country": "South Africa", "surface": 1221040},
    {"country": "Colombia", "surface": 1141750},
    {"country": "Ethiopia", "surface": 1104300},
    {"country": "Bolivia", "surface": 1098580},
    {"country": "Mauritania", "surface": 1030700},
    {"country": "Egypt", "surface": 1002450},
    {"country": "Tanzania", "surface": 945087},
    {"country": "Nigeria", "surface": 923768},
    {"country": "Venezuela", "surface": 912050},
    {"country": "Namibia", "surface": 825615},
    {"country": "Mozambique", "surface": 801590},
    {"country": "Pakistan", "surface": 796095},
    {"country": "Turkey", "surface": 783562},
    {"country": "Chile", "surface": 756102},
    {"country": "Zambia", "surface": 752618},
    {"country": "Myanmar", "surface": 676578},
    {"country": "Afghanistan", "surface": 652230},
    {"country": "South Sudan", "surface": 619745},
    {"country": "France", "surface": 551695},
    {"country": "Somalia", "surface": 637657},
    {"country": "Central African Republic", "surface": 622984},
    {"country": "Ukraine", "surface": 603550},
    {"country": "Madagascar", "surface": 587041},
    {"country": "Botswana", "surface": 581730},
    {"country": "Kenya", "surface": 580367},
    {"country": "Yemen", "surface": 527968},
    {"country": "Thailand", "surface": 513120},
    {"country": "Spain", "surface": 505992},
    {"country": "Turkmenistan", "surface": 488100},
    {"country": "Cameroon", "surface": 475442},
    {"country": "Papua New Guinea", "surface": 462840},
    {"country": "Sweden", "surface": 450295},
    {"country": "Uzbekistan", "surface": 447400},
    {"country": "Morocco", "surface": 446550},
    {"country": "Iraq", "surface": 438317},
    {"country": "Paraguay", "surface": 406752},
    {"country": "Zimbabwe", "surface": 390757},
    {"country": "Japan", "surface": 377975},
    {"country": "Germany", "surface": 357022},
    {"country": "Republic of Congo", "surface": 342000},
    {"country": "Finland", "surface": 338455},
    {"country": "Vietnam", "surface": 331212},
    {"country": "Malaysia", "surface": 330803},
    {"country": "Norway", "surface": 323802},
    {"country": "Ivory Coast", "surface": 322463},
    {"country": "Poland", "surface": 312696},
    {"country": "Oman", "surface": 309500},
    {"country": "Italy", "surface": 301340},
    {"country": "Philippines", "surface": 300000},
    {"country": "Ecuador", "surface": 276841},
    {"country": "Burkina Faso", "surface": 272967},
    {"country": "New Zealand", "surface": 268838},
    {"country": "Gabon", "surface": 267668},
    {"country": "Guinea", "surface": 245857},
    {"country": "United Kingdom", "surface": 243610},
    {"country": "Uganda", "surface": 241038},
    {"country": "Ghana", "surface": 238533},
    {"country": "Romania", "surface": 238397},
    {"country": "Laos", "surface": 236800},
    {"country": "Guyana", "surface": 214969},
    {"country": "Belarus", "surface": 207600},
    {"country": "Kyrgyzstan", "surface": 199951},
    {"country": "Senegal", "surface": 196722},
    {"country": "Syria", "surface": 185180},
    {"country": "Cambodia", "surface": 181035},
    {"country": "Uruguay", "surface": 176215},
    {"country": "Tunisia", "surface": 163610},
    {"country": "Suriname", "surface": 163820},
    {"country": "Bangladesh", "surface": 148460},
    {"country": "Nepal", "surface": 147516},
    {"country": "Tajikistan", "surface": 143100},
    {"country": "Greece", "surface": 131957},
    {"country": "Nicaragua", "surface": 130373},
    {"country": "North Korea", "surface": 120540},
    {"country": "South Korea", "surface": 100210}
]


print("🎲 Welcome to Higher/Lower: Country Surface Edition! 🌍")
print("Instructions:")
print("1. You will be shown a country and its surface area.")
print("2. A second country will be shown, and you must guess if its surface area is higher or lower than the first.")
print("3. Type 'h' if you think the next country's surface is Higher.")
print("4. Type 'l' if you think it is Lower.")
print("5. If you guess correctly, you continue. If not, the game ends.")
print("6. Try to get the highest streak possible! 💪")

continue_game = True
score = 0
first_country = random.choice(countries_area)
countries_area.remove(first_country)
second_country = random.choice(countries_area)
countries_area.remove(second_country)
while(continue_game):
    first_country = second_country
    second_country = random.choice(countries_area)
    countries_area.remove(second_country)
    print("")
    print(first_country["country"] + ":  " + str(first_country["surface"]) + " km²")
    print(second_country["country"] + ": higher or lower?")
    
    answer = input()
    if (answer == "h" and first_country["surface"] < second_country["surface"]) or (answer == "l" and first_country["surface"] > second_country["surface"]):
        score += 1
    elif (answer == "h" and first_country["surface"] > second_country["surface"]) or (answer == "l" and first_country["surface"] < second_country["surface"]):
        print("Wrong answer :|")
        print(f"Final score: {score}")
        break
    else:
        answer = input()



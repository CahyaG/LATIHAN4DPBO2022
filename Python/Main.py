from Ship import Ship
from Airplane import Airplane
from Driver import Driver

# membuat object driver
d1 = Driver(12223123, "Atep", "Laki-Laki", 12333312, "PT. Sejahtera", "Employee", 99488, "29-12-2022", "Airplane")
d2 = Driver(44122221, "Bira", "Perempuan", 32333312, "PT. Satu Dua", "Employee", 12221, "01-01-2025", "Airplane")
d3 = Driver(44213123, "Ujang", "Laki-Laki", 551232, "PT. Rrai", "Employee", 55122, "21-06-2022", "Ship")
d4 = Driver(55123123, "Yesnt", "Perempuan", 55521112, "Lololo Inc.", "Employee", 87665, "30-09-2023", "Ship")
d5 = Driver(88223123, "Iki", "Laki-Laki", 7727631, "Chillis Inc", "Employee", 222311, "12-12-2023", "Airplane")
d6 = Driver(55512332, "Lili", "Perempuan", 6663331, "Chillis Inc", "Employee", 33121, "12-09-2028", "Airplane")

# membuat object ship. nahkoda diambil dari object driver yang telah dibuat sebelumnya
s1 = Ship("Diesel", 122, 3, "Cruise", "Germany", d3)
s2 = Ship("Solar", 233, 5, "Cargo", "Indonesia", d4)
# semua ship dijadikan List agar mempermudah proses print
ship = [s1, s2]

# membuat object airplane. pilot dan copilot diambil dari object driver yang telah dibuat sebelumnya
a1 = Airplane("Diesel", 100, 1, "Commercial", 40, d1, d2)
a2 = Airplane("Diesel", 350, 4, "Commercial", 52.5, d5, d1)
a3 = Airplane("Natural Gas", 150, 12, "Commercial", 35.5, d5, d6)
# semua airplane dijadikan List agar mempermudah proses print
airplane = [a1, a2, a3]

# proses print Ship
i = 1
for s in ship:
    print("Ship {}".format(i))
    print("========================================")
    s.printShipDetail()
    print("========================================")
    i+=1

# proses print Airplane
i = 1
for a in airplane:
    print("Airplane {}".format(i))
    print("========================================")
    a.printAirplaneDetail()
    print("========================================")
    i+=1
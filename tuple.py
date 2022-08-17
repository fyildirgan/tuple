# Tuple(Demet)
#   Değiştirilemez.
#   Sıralıdır.
#   Kapsayıcıdır.

t = ("john", "mark",1, 2)
print(type(t))
print(t[0])
print(t[0:3])
#   Değiştirilemez özelliği
#t[0] = 99
#print(t[0])
# 11 ve 12 satılarda yapılan işlem tuple'ın değiştirilemezlik özelliğine bir örnektir.
# Çıktı aldığımızda karşımızı "tuple" object does not support item assignment hatası alırız.
# İlla bir değişiklik yapmak istiyorsak aşağıdaki gibi listelememiz gerekir.
t = list(t)
t[0] = 99
print(t[0])
# Tuple listelere benzer ama bize daha güvenli çalışmamızı sağlar.

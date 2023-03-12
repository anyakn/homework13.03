import ru_local as ru

v = 38241*24
s0 = 16637000000
vrw = 299792458
days = int(input())
smil = s0-v*days
skm = smil*1.61
sau = int(skm/149600000)
delay = round(vrw/(3*10**8)/1000*60*60, 2)
print(smil, ru.smil_past)
print(skm, ru.skm_past)
print(sau, ru.sau_past)
print(delay, ru.delay_wc_h)

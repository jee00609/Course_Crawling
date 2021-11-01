# main에서 시도코드를 인자로 받아서
# 해당 시도코드에 해당하는 시군구코드 리스트를 리턴하는 함수
  

seoul_guGun = [
  680,
  740,
  305,
  500,
  620,
  215,
  530,
  545,
  350,
  320,
  230,
  590,
  440,
  410,
  650,
  200,
  290,
  710,
  470,
  560,
  170,
  380,
  110,
  140,
  260
]

busan_guGun = [
  440,
  410,
  710,
  290,
  170,
  260,
  230,
  320,
  530,
  380,
  140,
  500,
  470,
  200,
  110,
  350
]

daegu_guGun = [
  200,
  290,
  710,
  140,
  230,
  170,
  260,
  110
]

incheon_guGun = [
  710,
  245,
  170,
  200,
  140,
  237,
  2606,
  185,
  720,
  110
]

gwangju_guGun = [
  200,
  155,
  110,
  170,
  140
]

daejeon_guGun = [
  230,
  110,
  170,
  200,
  140
]

ulsan_guGun = [
  140,
  170,
  200,
  710,
  110
]

sejong_guGun = [
  110
]

gyeonggi_guGun = [
  820,
  281,
  283,
  285,
  287,
  290,
  210,
  610,
  310,
  410,
  570,
  360,
  250,
  197,
  199,
  195,
  135,
  131,
  133,
  113,
  117,
  111,
  115,
  390,
  270,
  273,
  271,
  550,
  173,
  171,
  630,
  830,
  730,
  670,
  800,
  370,
  460,
  463,
  465,
  461,
  430,
  150,
  500,
  480,
  220,
  810,
  650,
  450,
  590
]

gangwon_guGun = [
  150,
  820,
  170,
  230,
  210,
  800,
  830,
  750,
  130,
  810,
  770,
  180,
  110,
  190,
  760,
  720,
  790,
  730
]

chungcheong_buk_guGun = [
  760,
  800,
  720,
  740,
  730,
  770,
  150,
  745,
  750,
  710,
  111,
  112,
  114,
  113,
  130
]

chungcheong_nam_guGun = [
  250,
  150,
  710,
  230,
  830,
  270,
  180,
  760,
  210,
  770,
  200,
  730,
  810,
  130,
  131,
  133,
  790,
  825,
  800
]

jeolla_buk_guGun = [
  790,
  130,
  210,
  190,
  730,
  800,
  770,
  710,
  140,
  750,
  740,
  113,
  111,
  180,
  720
]

jeolla_nam_guGun = [
  810,
  770,
  720,
  230,
  730,
  170,
  710,
  110,
  840,
  780,
  150,
  710,
  130,
  870,
  830,
  890,
  880,
  800,
  900,
  860,
  820,
  790
]

gyeongsang_buk_guGun = [
  290,
  130,
  830,
  190,
  720,
  150,
  280,
  920,
  250,
  840,
  170,
  770,
  760,
  210,
  230,
  900,
  940,
  930,
  730,
  820,
  750,
  850,
  111,
  113
]

gyeongsang_nam_guGun = [
  310,
  880,
  820,
  250,
  840,
  160,
  270,
  240,
  860,
  332,
  330,
  720,
  170,
  190,
  740,
  110,
  125,
  127,
  123,
  121,
  129,
  220,
  850,
  730,
  870,
  890
]

jeju_guGun = [
  130,
  110
]


def returnGuGunCodeList(sidoCode):
  
  if sidoCode == 11:
    return seoul_guGun

  elif sidoCode == 26:
    return busan_guGun
  
  elif sidoCode == 27:
    return daegu_guGun
  
  elif sidoCode == 28:
    return incheon_guGun
  
  elif sidoCode == 29:
    return gangwon_guGun
  
  elif sidoCode == 30:
    return daejeon_guGun
  
  elif sidoCode == 31:
    return ulsan_guGun
  
  elif sidoCode == 36:
    return sejong_guGun
  
  elif sidoCode == 41:
    return gyeonggi_guGun
  
  elif sidoCode == 42:
    return gangwon_guGun
  
  elif sidoCode == 43:
    return chungcheong_buk_guGun
  
  elif sidoCode == 44:
    return chungcheong_nam_guGun
  
  elif sidoCode == 45:
    return jeolla_buk_guGun
  
  elif sidoCode == 46:
    return jeolla_nam_guGun
  
  elif sidoCode == 47:
    return gyeongsang_buk_guGun
  
  elif sidoCode == 48:
    return gyeongsang_nam_guGun
  
  elif sidoCode == 50:
    return jeju_guGun
    
  else : return []
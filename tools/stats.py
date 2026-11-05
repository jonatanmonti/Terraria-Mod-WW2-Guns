# class: (tier, type, dmg, useTime, kb, vel, crit, spread, ammoSave, pellets, pierce, scope, auto, sound)
P,B,S,SMG,LMG,HMG,SG,AT,AR = 'Pistol','Bolt','Semi','SMG','LMG','HMG','Shotgun','AT','Assault'
STATS = {
 'LugerP08':      (1,P,  12,16,2.0, 9,  4,0,  0,  1,0,False,False,'pistol'),
 'MP40':          (4,SMG,11, 7,1.0, 9,  0,6,  0,  1,0,False,True,'smg'),
 'Kar98k':        (3,B,  38,40,5.0,12, 10,0,  0,  1,0,False,False,'rifle'),
 'Gewehr43':      (5,S,  34,18,4.0,12,  6,1,  0,  1,0,False,False,'rifle'),
 'StG44':         (7,AR, 28, 8,2.5,11,  4,4,  0,  1,0,False,True,'smg'),
 'MG42':          (8,HMG,30, 4,1.5,12,  0,6, .5,  1,0,False,True,'mg'),
 'BerettaM1934':  (1,P,  10,14,1.5, 8,  4,0,  0,  1,0,False,False,'pistol'),
 'CarcanoM9138':  (2,B,  30,38,4.5,11,  8,0,  0,  1,0,False,False,'rifle'),
 'MAB38':         (4,SMG,12, 8,1.5,10,  0,4,  0,  1,0,False,True,'smg'),
 'FNAB43':        (5,SMG,18, 7,1.5,10,  0,6,  0,  1,0,False,True,'smg'),
 'Breda30':       (5,LMG,22,10,2.0,11,  0,5,.25,  1,0,False,True,'mg'),
 'BredaM37':      (7,HMG,34, 9,2.5,12,  0,3,.33,  1,0,False,True,'mg'),
 'NambuType14':   (1,P,  11,17,1.5, 8,  4,0,  0,  1,0,False,False,'pistol'),
 'ArisakaType99': (3,B,  36,40,5.0,12, 10,0,  0,  1,0,False,False,'rifle'),
 'Type97Sniper':  (6,B,  95,45,6.0,16, 20,0,  0,  1,1,True, False,'sniper'),
 'Type100SMG':    (4,SMG,11, 7,1.0, 9,  0,7,  0,  1,0,False,True,'smg'),
 'Type96LMG':     (6,LMG,26, 8,2.0,11,  0,4,.33,  1,0,False,True,'mg'),
 'Type92HMG':     (8,HMG,40, 9,3.0,13,  0,3,.33,  1,0,False,True,'mg'),
 'ColtM1911':     (2,P,  17,16,3.0, 9,  4,0,  0,  1,0,False,False,'pistol'),
 'M1Garand':      (4,S,  28,14,4.0,12,  6,1,  0,  1,0,False,False,'rifle'),
 'M1Carbine':     (3,S,  18,12,2.5,11,  4,1,  0,  1,0,False,False,'rifle'),
 'ThompsonM1928': (5,SMG,20, 6,1.5,10,  0,7,  0,  1,0,False,True,'smg'),
 'BrowningBAR':   (6,LMG,34,10,3.0,12,  2,3, .2,  1,0,False,True,'mg'),
 'M1897TrenchGun':(5,SG, 20,40,5.0, 9,  0,14, 0,  5,0,False,False,'shotgun'),
 'WebleyMkVI':    (2,P,  22,22,4.0, 9,  6,0,  0,  1,0,False,False,'pistol'),
 'LeeEnfieldNo4': (3,B,  34,30,4.5,12,  8,0,  0,  1,0,False,False,'rifle'),
 'StenMkII':      (3,SMG, 9, 7,1.0, 8,  0,8,  0,  1,0,False,True,'smg'),
 'Bren':          (6,LMG,30, 9,2.5,12,  2,3,.25,  1,0,False,True,'mg'),
 'DeLisleCarbine':(5,B,  40,30,3.0,12, 15,0,  0,  1,0,False,False,'silenced'),
 'BoysATRifle':   (8,AT,160,50,9.0,18, 10,0,  0,  1,4,False,False,'sniper'),
 'TokarevTT33':   (1,P,  13,15,2.0, 9,  4,0,  0,  1,0,False,False,'pistol'),
 'MosinNagant':   (2,B,  32,42,5.0,12,  8,0,  0,  1,0,False,False,'rifle'),
 'SVT40':         (5,S,  32,16,4.0,12,  6,1,  0,  1,0,False,False,'rifle'),
 'PPSh41':        (6,SMG,18, 4,1.0,10,  0,8,  0,  1,0,False,True,'smg'),
 'PPS43':         (4,SMG,12, 7,1.0, 9,  0,6,  0,  1,0,False,True,'smg'),
 'DP27':          (7,LMG,32, 9,2.5,12,  2,4,.25,  1,0,False,True,'mg'),
 'MAS1935':       (1,P,  11,15,1.5, 8,  4,0,  0,  1,0,False,False,'pistol'),
 'MAS36':         (3,B,  35,36,4.5,12,  8,0,  0,  1,0,False,False,'rifle'),
 'Lebel1886':     (2,B,  30,40,5.0,11,  6,0,  0,  1,0,False,False,'rifle'),
 'MAS38':         (3,SMG, 9, 7,1.0, 8,  0,6,  0,  1,0,False,True,'smg'),
 'FM2429':        (5,LMG,24,10,2.0,11,  0,4, .2,  1,0,False,True,'mg'),
 'HotchkissM1914':(7,HMG,36,10,3.0,12,  0,3,.33,  1,0,False,True,'mg'),
}
# tier -> (ingredients, tile, rarity, buy gold)
TIERS = {
 1: ([('G:IronBar',10),('V:Wood',5)], 'TileID.Anvils', 'ItemRarityID.White', 1),
 2: ([('C:SilverBar',12),('V:Wood',8)], 'TileID.Anvils', 'ItemRarityID.Blue', 3),
 3: ([('C:EvilBar',12),('G:IronBar',6)], 'TileID.Anvils', 'ItemRarityID.Green', 6),
 4: ([('I:MeteoriteBar',12),('I:HellstoneBar',6)], 'TileID.Anvils', 'ItemRarityID.Orange', 10),
 5: ([('C:CobaltBar',12),('I:IllegalGunParts',1)], 'TileID.Anvils', 'ItemRarityID.LightRed', 18),
 6: ([('C:MythrilBar',12),('I:SoulofNight',6)], 'TileID.MythrilAnvil', 'ItemRarityID.Pink', 28),
 7: ([('C:AdamantiteBar',14),('I:SoulofNight',8),('I:IllegalGunParts',1)], 'TileID.MythrilAnvil', 'ItemRarityID.LightPurple', 40),
 8: ([('I:HallowedBar',15),('I:SoulofMight',10)], 'TileID.MythrilAnvil', 'ItemRarityID.Lime', 60),
}
SOUNDS = {
 'pistol': 'SoundID.Item41', 'smg': 'SoundID.Item11', 'rifle': 'SoundID.Item40',
 'mg': 'SoundID.Item11', 'sniper': 'SoundID.Item40', 'shotgun': 'SoundID.Item36',
 'silenced': 'SoundID.Item11 with { Volume = 0.35f, Pitch = -0.4f }',
}
SHOP = {  # Arms Dealer
 'LugerP08':None,'BerettaM1934':None,'NambuType14':None,'TokarevTT33':None,'MAS1935':None,
 'ColtM1911':'Condition.DownedEyeOfCthulhu','WebleyMkVI':'Condition.DownedEyeOfCthulhu',
 'ThompsonM1928':'Condition.Hardmode','M1897TrenchGun':'Condition.Hardmode',
}
DROPS = [  # (npc, item, chance denominator)
 ('NPCID.SkeletonCommando','BoysATRifle',10),
 ('NPCID.SkeletonSniper','Type97Sniper',8),
 ('NPCID.TacticalSkeleton','MG42',12),
 ('NPCID.PirateDeadeye','ThompsonM1928',20),
]
TYPE_ES = {P:'Pistola',B:'Rifle de cerrojo',S:'Rifle semiautomático',SMG:'Subfusil',LMG:'Ametralladora ligera',
           HMG:'Ametralladora',SG:'Escopeta de corredera',AT:'Fusil antitanque',AR:'Fusil de asalto'}
TYPE_EN = {P:'Pistol',B:'Bolt-action rifle',S:'Semi-automatic rifle',SMG:'Submachine gun',LMG:'Light machine gun',
           HMG:'Machine gun',SG:'Pump-action shotgun',AT:'Anti-tank rifle',AR:'Assault rifle'}
COUNTRY_ES = {'Germany':'Alemania','Italy':'Italia','Japan':'Japón','USA':'Estados Unidos','UK':'Reino Unido','USSR':'Unión Soviética','France':'Francia'}
COUNTRY_EN = {'Germany':'Germany','Italy':'Italy','Japan':'Japan','USA':'United States','UK':'United Kingdom','USSR':'Soviet Union','France':'France'}

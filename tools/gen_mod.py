import os, shutil
from roster import ROSTER
from stats import *
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
items_dir = f'{OUT}/Content/Items'
shutil.rmtree(items_dir, ignore_errors=True)

def ing(code, n):
    k, v = code.split(':')
    if k == 'G': return f'recipe.AddRecipeGroup(RecipeGroupID.{v}, {n});'
    if k == 'V': return f'recipe.AddRecipeGroup(RecipeGroupID.{v}, {n});'
    if k == 'C': return f'recipe.AddRecipeGroup("WW2Guns:{v}", {n});'
    return f'recipe.AddIngredient(ItemID.{v}, {n});'

def f(x): return f'{x}f'

loc_en, loc_es = [], []
for cls, name, country, fn in ROSTER:
    img = fn().render()
    d = f'{items_dir}/{country}'; os.makedirs(d, exist_ok=True)
    img.save(f'{d}/{cls}.png')
    tier,typ,dmg,ut,kb,vel,crit,spread,save,pellets,pierce,scope,auto,snd = STATS[cls]
    ings, tile, rare, gold = TIERS[tier]
    w, h = img.size
    hold = 2 if w < 32 else -round((w - 28) * 0.3)
    muzzle = max(12, round(w * 0.75))
    recipe = '\n            '.join(ing(c, n) for c, n in ings)
    code = f'''using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.{country}
{{
    // {name} - {COUNTRY_EN[country]} ({TYPE_EN[typ]})
    public class {cls} : WW2Gun
    {{
        private static readonly GunData data = new GunData
        {{
            Damage = {dmg},
            UseTime = {ut},
            Knockback = {f(kb)},
            Velocity = {f(vel)},
            Crit = {crit},
            Spread = {f(spread)},
            AmmoSaveChance = {f(save)},
            Pellets = {pellets},
            ExtraPierce = {pierce},
            Scope = {str(scope).lower()},
            AutoReuse = {str(auto).lower()},
            Rarity = {rare},
            BuyPriceGold = {gold},
            Width = {w},
            Height = {h},
            HoldoutX = {f(hold)},
            MuzzleOffset = {f(muzzle)},
        }};

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => {SOUNDS[snd]};

        public override void AddRecipes()
        {{
            Recipe recipe = CreateRecipe();
            {recipe}
            recipe.AddTile({tile});
            recipe.Register();
        }}
    }}
}}
'''
    open(f'{d}/{cls}.cs', 'w').write(code)
    extra_en, extra_es = [], []
    if save: extra_en.append(f'{int(save*100)}% chance not to consume ammo'); extra_es.append(f'{int(save*100)}% de probabilidad de no gastar munición')
    if pellets > 1: extra_en.append(f'Fires {pellets} pellets'); extra_es.append(f'Dispara {pellets} perdigones')
    if pierce: extra_en.append(f'Bullets pierce {pierce} extra enemies'); extra_es.append(f'Las balas atraviesan {pierce} enemigo(s) extra')
    if scope: extra_en.append('Right click to zoom out'); extra_es.append('Clic derecho para hacer zoom')
    if snd == 'silenced': extra_en.append('Integrated suppressor'); extra_es.append('Silenciador integrado')
    tt_en = '\\n'.join([f'{COUNTRY_EN[country]} - {TYPE_EN[typ]}'] + extra_en + ['Uses bullets'])
    tt_es = '\\n'.join([f'{COUNTRY_ES[country]} - {TYPE_ES[typ]}'] + extra_es + ['Usa balas'])
    loc_en.append(f'\t\t{cls}: {{\n\t\t\tDisplayName: "{name}"\n\t\t\tTooltip: "{tt_en}"\n\t\t}}\n')
    loc_es.append(f'\t\t{cls}: {{\n\t\t\tDisplayName: "{name}"\n\t\t\tTooltip: "{tt_es}"\n\t\t}}\n')

os.makedirs(f'{OUT}/Localization', exist_ok=True)
groups_en = {'SilverBar':'Any Silver Bar','EvilBar':'Any Demonite or Crimtane Bar','CobaltBar':'Any Cobalt Bar','MythrilBar':'Any Mythril Bar','AdamantiteBar':'Any Adamantite Bar'}
groups_es = {'SilverBar':'Cualquier lingote de plata','EvilBar':'Cualquier lingote de demonita o carmesí','CobaltBar':'Cualquier lingote de cobalto','MythrilBar':'Cualquier lingote de mithril','AdamantiteBar':'Cualquier lingote de adamantita'}
for lang, items, groups in (('en-US', loc_en, groups_en), ('es-ES', loc_es, groups_es)):
    g = ''.join(f'\t\t{k}: {v}\n' for k, v in groups.items())
    open(f'{OUT}/Localization/{lang}_Mods.WW2Guns.hjson', 'w').write(
        'Mods: {\n\tWW2Guns: {\n\t\tItems: {\n' + ''.join('\t' + l.replace('\n\t', '\n\t\t') for l in items) +
        '\t\t}\n\n\t\tRecipeGroups: {\n' + g.replace('\t\t', '\t\t\t') + '\t\t}\n\t}\n}\n')

# shop + drops
shop = '\n'.join(
    f'                shop.Add(ModContent.ItemType<global::WW2Guns.Content.Items.{next(c for c in ROSTER if c[0]==k)[2]}.{k}>(){", " + v if v else ""});'
    for k, v in SHOP.items())
drops = '\n'.join(
    f'            if (npc.type == {n})\n                npcLoot.Add(ItemDropRule.Common(ModContent.ItemType<global::WW2Guns.Content.Items.{next(c for c in ROSTER if c[0]==k)[2]}.{k}>(), {c}));'
    for n, k, c in DROPS)
open(f'{OUT}/Common/WW2GlobalNPC.cs', 'w').write(f'''using Terraria;
using Terraria.GameContent.ItemDropRules;
using Terraria.ID;
using Terraria.ModLoader;

namespace WW2Guns.Common
{{
    // Arms Dealer sells the sidearms (and a couple of Hardmode guns); some Dungeon enemies drop rare guns.
    public class WW2GlobalNPC : GlobalNPC
    {{
        public override void ModifyShop(NPCShop shop)
        {{
            if (shop.NpcType == NPCID.ArmsDealer)
            {{
{shop}
            }}
        }}

        public override void ModifyNPCLoot(NPC npc, NPCLoot npcLoot)
        {{
{drops}
        }}
    }}
}}
''')
print('generated', len(ROSTER))

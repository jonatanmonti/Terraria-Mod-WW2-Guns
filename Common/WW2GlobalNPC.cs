using Terraria;
using Terraria.GameContent.ItemDropRules;
using Terraria.ID;
using Terraria.ModLoader;

namespace WW2Guns.Common
{
    // Arms Dealer sells the sidearms (and a couple of Hardmode guns); some Dungeon enemies drop rare guns.
    public class WW2GlobalNPC : GlobalNPC
    {
        public override void ModifyShop(NPCShop shop)
        {
            if (shop.NpcType == NPCID.ArmsDealer)
            {
                shop.Add(ModContent.ItemType<global::WW2Guns.Content.Items.Germany.LugerP08>());
                shop.Add(ModContent.ItemType<global::WW2Guns.Content.Items.Italy.BerettaM1934>());
                shop.Add(ModContent.ItemType<global::WW2Guns.Content.Items.Japan.NambuType14>());
                shop.Add(ModContent.ItemType<global::WW2Guns.Content.Items.USSR.TokarevTT33>());
                shop.Add(ModContent.ItemType<global::WW2Guns.Content.Items.France.MAS1935>());
                shop.Add(ModContent.ItemType<global::WW2Guns.Content.Items.USA.ColtM1911>(), Condition.DownedEyeOfCthulhu);
                shop.Add(ModContent.ItemType<global::WW2Guns.Content.Items.UK.WebleyMkVI>(), Condition.DownedEyeOfCthulhu);
                shop.Add(ModContent.ItemType<global::WW2Guns.Content.Items.USA.ThompsonM1928>(), Condition.Hardmode);
                shop.Add(ModContent.ItemType<global::WW2Guns.Content.Items.USA.M1897TrenchGun>(), Condition.Hardmode);
            }
        }

        public override void ModifyNPCLoot(NPC npc, NPCLoot npcLoot)
        {
            if (npc.type == NPCID.SkeletonCommando)
                npcLoot.Add(ItemDropRule.Common(ModContent.ItemType<global::WW2Guns.Content.Items.UK.BoysATRifle>(), 10));
            if (npc.type == NPCID.SkeletonSniper)
                npcLoot.Add(ItemDropRule.Common(ModContent.ItemType<global::WW2Guns.Content.Items.Japan.Type97Sniper>(), 8));
            if (npc.type == NPCID.TacticalSkeleton)
                npcLoot.Add(ItemDropRule.Common(ModContent.ItemType<global::WW2Guns.Content.Items.Germany.MG42>(), 12));
            if (npc.type == NPCID.PirateDeadeye)
                npcLoot.Add(ItemDropRule.Common(ModContent.ItemType<global::WW2Guns.Content.Items.USA.ThompsonM1928>(), 20));
        }
    }
}

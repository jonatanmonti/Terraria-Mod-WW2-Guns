using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.UK
{
    // Boys Anti-Tank Rifle - United Kingdom (Anti-tank rifle)
    public class BoysATRifle : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 160,
            UseTime = 50,
            Knockback = 9.0f,
            Velocity = 18f,
            Crit = 10,
            Spread = 0f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 4,
            Scope = false,
            AutoReuse = false,
            Rarity = ItemRarityID.Lime,
            BuyPriceGold = 60,
            Width = 73,
            Height = 19,
            HoldoutX = -14f,
            MuzzleOffset = 55f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item40;

        public override void AddRecipes()
        {
            Recipe recipe = CreateRecipe();
            recipe.AddIngredient(ItemID.HallowedBar, 15);
            recipe.AddIngredient(ItemID.SoulofMight, 10);
            recipe.AddTile(TileID.MythrilAnvil);
            recipe.Register();
        }
    }
}

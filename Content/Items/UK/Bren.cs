using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.UK
{
    // Bren Gun - United Kingdom (Light machine gun)
    public class Bren : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 30,
            UseTime = 9,
            Knockback = 2.5f,
            Velocity = 12f,
            Crit = 2,
            Spread = 3f,
            AmmoSaveChance = 0.25f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = true,
            Rarity = ItemRarityID.Pink,
            BuyPriceGold = 28,
            Width = 54,
            Height = 22,
            HoldoutX = -8f,
            MuzzleOffset = 40f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item11;

        public override void AddRecipes()
        {
            Recipe recipe = CreateRecipe();
            recipe.AddRecipeGroup("WW2Guns:MythrilBar", 12);
            recipe.AddIngredient(ItemID.SoulofNight, 6);
            recipe.AddTile(TileID.MythrilAnvil);
            recipe.Register();
        }
    }
}

using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.USA
{
    // Browning BAR - United States (Light machine gun)
    public class BrowningBAR : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 34,
            UseTime = 10,
            Knockback = 3.0f,
            Velocity = 12f,
            Crit = 2,
            Spread = 3f,
            AmmoSaveChance = 0.2f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = true,
            Rarity = ItemRarityID.Pink,
            BuyPriceGold = 28,
            Width = 62,
            Height = 15,
            HoldoutX = -10f,
            MuzzleOffset = 46f,
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

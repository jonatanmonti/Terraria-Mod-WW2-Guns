using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.Japan
{
    // Type 96 LMG - Japan (Light machine gun)
    public class Type96LMG : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 26,
            UseTime = 8,
            Knockback = 2.0f,
            Velocity = 11f,
            Crit = 0,
            Spread = 4f,
            AmmoSaveChance = 0.33f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = true,
            Rarity = ItemRarityID.Pink,
            BuyPriceGold = 28,
            Width = 56,
            Height = 19,
            HoldoutX = -8f,
            MuzzleOffset = 42f,
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

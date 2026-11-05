using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.USSR
{
    // PPSh-41 - Soviet Union (Submachine gun)
    public class PPSh41 : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 18,
            UseTime = 4,
            Knockback = 1.0f,
            Velocity = 10f,
            Crit = 0,
            Spread = 8f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = true,
            Rarity = ItemRarityID.Pink,
            BuyPriceGold = 28,
            Width = 48,
            Height = 19,
            HoldoutX = -6f,
            MuzzleOffset = 36f,
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

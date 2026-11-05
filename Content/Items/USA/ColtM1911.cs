using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.USA
{
    // Colt M1911 - United States (Pistol)
    public class ColtM1911 : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 17,
            UseTime = 16,
            Knockback = 3.0f,
            Velocity = 9f,
            Crit = 4,
            Spread = 0f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = false,
            Rarity = ItemRarityID.Blue,
            BuyPriceGold = 3,
            Width = 22,
            Height = 17,
            HoldoutX = 2f,
            MuzzleOffset = 16f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item41;

        public override void AddRecipes()
        {
            Recipe recipe = CreateRecipe();
            recipe.AddRecipeGroup("WW2Guns:SilverBar", 12);
            recipe.AddRecipeGroup(RecipeGroupID.Wood, 8);
            recipe.AddTile(TileID.Anvils);
            recipe.Register();
        }
    }
}

using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.UK
{
    // Webley Mk VI - United Kingdom (Pistol)
    public class WebleyMkVI : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 22,
            UseTime = 22,
            Knockback = 4.0f,
            Velocity = 9f,
            Crit = 6,
            Spread = 0f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = false,
            Rarity = ItemRarityID.Blue,
            BuyPriceGold = 3,
            Width = 34,
            Height = 18,
            HoldoutX = -2f,
            MuzzleOffset = 26f,
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

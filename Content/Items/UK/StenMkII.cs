using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.UK
{
    // Sten Mk II - United Kingdom (Submachine gun)
    public class StenMkII : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 9,
            UseTime = 7,
            Knockback = 1.0f,
            Velocity = 8f,
            Crit = 0,
            Spread = 8f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = true,
            Rarity = ItemRarityID.Green,
            BuyPriceGold = 6,
            Width = 41,
            Height = 16,
            HoldoutX = -4f,
            MuzzleOffset = 31f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item11;

        public override void AddRecipes()
        {
            Recipe recipe = CreateRecipe();
            recipe.AddRecipeGroup("WW2Guns:EvilBar", 12);
            recipe.AddRecipeGroup(RecipeGroupID.IronBar, 6);
            recipe.AddTile(TileID.Anvils);
            recipe.Register();
        }
    }
}

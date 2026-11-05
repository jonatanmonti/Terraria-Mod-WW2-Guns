using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.France
{
    // MAS-38 - France (Submachine gun)
    public class MAS38 : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 9,
            UseTime = 7,
            Knockback = 1.0f,
            Velocity = 8f,
            Crit = 0,
            Spread = 6f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = true,
            Rarity = ItemRarityID.Green,
            BuyPriceGold = 6,
            Width = 39,
            Height = 14,
            HoldoutX = -3f,
            MuzzleOffset = 29f,
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

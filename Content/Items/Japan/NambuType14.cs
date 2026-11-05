using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.Japan
{
    // Nambu Type 14 - Japan (Pistol)
    public class NambuType14 : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 11,
            UseTime = 17,
            Knockback = 1.5f,
            Velocity = 8f,
            Crit = 4,
            Spread = 0f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = false,
            Rarity = ItemRarityID.White,
            BuyPriceGold = 1,
            Width = 27,
            Height = 16,
            HoldoutX = 2f,
            MuzzleOffset = 20f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item41;

        public override void AddRecipes()
        {
            Recipe recipe = CreateRecipe();
            recipe.AddRecipeGroup(RecipeGroupID.IronBar, 10);
            recipe.AddRecipeGroup(RecipeGroupID.Wood, 5);
            recipe.AddTile(TileID.Anvils);
            recipe.Register();
        }
    }
}

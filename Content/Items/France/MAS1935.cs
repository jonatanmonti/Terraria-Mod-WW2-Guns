using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.France
{
    // MAS 1935 - France (Pistol)
    public class MAS1935 : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 11,
            UseTime = 15,
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
            Width = 20,
            Height = 16,
            HoldoutX = 2f,
            MuzzleOffset = 15f,
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

using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.Germany
{
    // Luger P08 - Germany (Pistol)
    public class LugerP08 : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 12,
            UseTime = 16,
            Knockback = 2.0f,
            Velocity = 9f,
            Crit = 4,
            Spread = 0f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = false,
            Rarity = ItemRarityID.White,
            BuyPriceGold = 1,
            Width = 29,
            Height = 17,
            HoldoutX = 2f,
            MuzzleOffset = 22f,
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

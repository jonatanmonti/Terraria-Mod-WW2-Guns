using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.Italy
{
    // Carcano M91/38 - Italy (Bolt-action rifle)
    public class CarcanoM9138 : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 30,
            UseTime = 38,
            Knockback = 4.5f,
            Velocity = 11f,
            Crit = 8,
            Spread = 0f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = false,
            Rarity = ItemRarityID.Blue,
            BuyPriceGold = 3,
            Width = 57,
            Height = 11,
            HoldoutX = -9f,
            MuzzleOffset = 43f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item40;

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

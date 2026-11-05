using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.Germany
{
    // Karabiner 98k - Germany (Bolt-action rifle)
    public class Kar98k : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 38,
            UseTime = 40,
            Knockback = 5.0f,
            Velocity = 12f,
            Crit = 10,
            Spread = 0f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = false,
            Rarity = ItemRarityID.Green,
            BuyPriceGold = 6,
            Width = 63,
            Height = 11,
            HoldoutX = -10f,
            MuzzleOffset = 47f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item40;

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

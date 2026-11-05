using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.USA
{
    // M1 Carbine - United States (Semi-automatic rifle)
    public class M1Carbine : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 18,
            UseTime = 12,
            Knockback = 2.5f,
            Velocity = 11f,
            Crit = 4,
            Spread = 1f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = false,
            Rarity = ItemRarityID.Green,
            BuyPriceGold = 6,
            Width = 49,
            Height = 12,
            HoldoutX = -6f,
            MuzzleOffset = 37f,
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

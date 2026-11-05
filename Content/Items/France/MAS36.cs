using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.France
{
    // MAS-36 - France (Bolt-action rifle)
    public class MAS36 : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 35,
            UseTime = 36,
            Knockback = 4.5f,
            Velocity = 12f,
            Crit = 8,
            Spread = 0f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = false,
            Rarity = ItemRarityID.Green,
            BuyPriceGold = 6,
            Width = 61,
            Height = 11,
            HoldoutX = -10f,
            MuzzleOffset = 46f,
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

using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.USSR
{
    // Mosin-Nagant M91/30 - Soviet Union (Bolt-action rifle)
    public class MosinNagant : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 32,
            UseTime = 42,
            Knockback = 5.0f,
            Velocity = 12f,
            Crit = 8,
            Spread = 0f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = false,
            Rarity = ItemRarityID.Blue,
            BuyPriceGold = 3,
            Width = 78,
            Height = 11,
            HoldoutX = -15f,
            MuzzleOffset = 58f,
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

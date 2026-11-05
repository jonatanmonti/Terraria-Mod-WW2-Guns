using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.USSR
{
    // DP-27 - Soviet Union (Light machine gun)
    public class DP27 : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 32,
            UseTime = 9,
            Knockback = 2.5f,
            Velocity = 12f,
            Crit = 2,
            Spread = 4f,
            AmmoSaveChance = 0.25f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = true,
            Rarity = ItemRarityID.LightPurple,
            BuyPriceGold = 40,
            Width = 56,
            Height = 17,
            HoldoutX = -8f,
            MuzzleOffset = 42f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item11;

        public override void AddRecipes()
        {
            Recipe recipe = CreateRecipe();
            recipe.AddRecipeGroup("WW2Guns:AdamantiteBar", 14);
            recipe.AddIngredient(ItemID.SoulofNight, 8);
            recipe.AddIngredient(ItemID.IllegalGunParts, 1);
            recipe.AddTile(TileID.MythrilAnvil);
            recipe.Register();
        }
    }
}

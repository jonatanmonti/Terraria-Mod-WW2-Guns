using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.France
{
    // Hotchkiss M1914 - France (Machine gun)
    public class HotchkissM1914 : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 36,
            UseTime = 10,
            Knockback = 3.0f,
            Velocity = 12f,
            Crit = 0,
            Spread = 3f,
            AmmoSaveChance = 0.33f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = true,
            Rarity = ItemRarityID.LightPurple,
            BuyPriceGold = 40,
            Width = 58,
            Height = 17,
            HoldoutX = -9f,
            MuzzleOffset = 44f,
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

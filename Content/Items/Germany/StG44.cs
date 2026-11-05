using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.Germany
{
    // StG 44 - Germany (Assault rifle)
    public class StG44 : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 28,
            UseTime = 8,
            Knockback = 2.5f,
            Velocity = 11f,
            Crit = 4,
            Spread = 4f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = true,
            Rarity = ItemRarityID.LightPurple,
            BuyPriceGold = 40,
            Width = 54,
            Height = 19,
            HoldoutX = -8f,
            MuzzleOffset = 40f,
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

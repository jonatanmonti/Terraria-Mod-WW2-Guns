using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.USA
{
    // Thompson M1928 - United States (Submachine gun)
    public class ThompsonM1928 : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 20,
            UseTime = 6,
            Knockback = 1.5f,
            Velocity = 10f,
            Crit = 0,
            Spread = 7f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = true,
            Rarity = ItemRarityID.LightRed,
            BuyPriceGold = 18,
            Width = 50,
            Height = 18,
            HoldoutX = -7f,
            MuzzleOffset = 38f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item11;

        public override void AddRecipes()
        {
            Recipe recipe = CreateRecipe();
            recipe.AddRecipeGroup("WW2Guns:CobaltBar", 12);
            recipe.AddIngredient(ItemID.IllegalGunParts, 1);
            recipe.AddTile(TileID.Anvils);
            recipe.Register();
        }
    }
}

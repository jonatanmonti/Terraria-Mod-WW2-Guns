using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.Italy
{
    // Breda 30 - Italy (Light machine gun)
    public class Breda30 : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 22,
            UseTime = 10,
            Knockback = 2.0f,
            Velocity = 11f,
            Crit = 0,
            Spread = 5f,
            AmmoSaveChance = 0.25f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = true,
            Rarity = ItemRarityID.LightRed,
            BuyPriceGold = 18,
            Width = 54,
            Height = 13,
            HoldoutX = -8f,
            MuzzleOffset = 40f,
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

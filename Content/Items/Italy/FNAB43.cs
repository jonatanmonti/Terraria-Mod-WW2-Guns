using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.Italy
{
    // FNAB-43 - Italy (Submachine gun)
    public class FNAB43 : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 18,
            UseTime = 7,
            Knockback = 1.5f,
            Velocity = 10f,
            Crit = 0,
            Spread = 6f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = true,
            Rarity = ItemRarityID.LightRed,
            BuyPriceGold = 18,
            Width = 40,
            Height = 15,
            HoldoutX = -4f,
            MuzzleOffset = 30f,
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

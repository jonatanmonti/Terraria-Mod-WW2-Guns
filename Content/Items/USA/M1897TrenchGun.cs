using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.USA
{
    // M1897 Trench Gun - United States (Pump-action shotgun)
    public class M1897TrenchGun : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 20,
            UseTime = 40,
            Knockback = 5.0f,
            Velocity = 9f,
            Crit = 0,
            Spread = 14f,
            AmmoSaveChance = 0f,
            Pellets = 5,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = false,
            Rarity = ItemRarityID.LightRed,
            BuyPriceGold = 18,
            Width = 60,
            Height = 12,
            HoldoutX = -10f,
            MuzzleOffset = 45f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item36;

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

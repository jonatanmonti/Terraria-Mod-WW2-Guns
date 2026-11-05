using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.Germany
{
    // Gewehr 43 - Germany (Semi-automatic rifle)
    public class Gewehr43 : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 34,
            UseTime = 18,
            Knockback = 4.0f,
            Velocity = 12f,
            Crit = 6,
            Spread = 1f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = false,
            Rarity = ItemRarityID.LightRed,
            BuyPriceGold = 18,
            Width = 61,
            Height = 12,
            HoldoutX = -10f,
            MuzzleOffset = 46f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item40;

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

using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.USA
{
    // M1 Garand - United States (Semi-automatic rifle)
    public class M1Garand : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 28,
            UseTime = 14,
            Knockback = 4.0f,
            Velocity = 12f,
            Crit = 6,
            Spread = 1f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = false,
            Rarity = ItemRarityID.Orange,
            BuyPriceGold = 10,
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
            recipe.AddIngredient(ItemID.MeteoriteBar, 12);
            recipe.AddIngredient(ItemID.HellstoneBar, 6);
            recipe.AddTile(TileID.Anvils);
            recipe.Register();
        }
    }
}

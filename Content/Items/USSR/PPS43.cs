using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.USSR
{
    // PPS-43 - Soviet Union (Submachine gun)
    public class PPS43 : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 12,
            UseTime = 7,
            Knockback = 1.0f,
            Velocity = 9f,
            Crit = 0,
            Spread = 6f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = true,
            Rarity = ItemRarityID.Orange,
            BuyPriceGold = 10,
            Width = 39,
            Height = 17,
            HoldoutX = -3f,
            MuzzleOffset = 29f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item11;

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

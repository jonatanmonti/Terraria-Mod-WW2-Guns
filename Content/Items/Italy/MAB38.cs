using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.Italy
{
    // Beretta MAB 38 - Italy (Submachine gun)
    public class MAB38 : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 12,
            UseTime = 8,
            Knockback = 1.5f,
            Velocity = 10f,
            Crit = 0,
            Spread = 4f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = true,
            Rarity = ItemRarityID.Orange,
            BuyPriceGold = 10,
            Width = 48,
            Height = 18,
            HoldoutX = -6f,
            MuzzleOffset = 36f,
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

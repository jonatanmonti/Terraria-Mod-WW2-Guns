using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.Germany
{
    // MG 42 - Germany (Machine gun)
    public class MG42 : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 30,
            UseTime = 4,
            Knockback = 1.5f,
            Velocity = 12f,
            Crit = 0,
            Spread = 6f,
            AmmoSaveChance = 0.5f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = true,
            Rarity = ItemRarityID.Lime,
            BuyPriceGold = 60,
            Width = 56,
            Height = 17,
            HoldoutX = -8f,
            MuzzleOffset = 42f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item11;

        public override void AddRecipes()
        {
            Recipe recipe = CreateRecipe();
            recipe.AddIngredient(ItemID.HallowedBar, 15);
            recipe.AddIngredient(ItemID.SoulofMight, 10);
            recipe.AddTile(TileID.MythrilAnvil);
            recipe.Register();
        }
    }
}

using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.Japan
{
    // Type 92 HMG - Japan (Machine gun)
    public class Type92HMG : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 40,
            UseTime = 9,
            Knockback = 3.0f,
            Velocity = 13f,
            Crit = 0,
            Spread = 3f,
            AmmoSaveChance = 0.33f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = true,
            Rarity = ItemRarityID.Lime,
            BuyPriceGold = 60,
            Width = 59,
            Height = 19,
            HoldoutX = -9f,
            MuzzleOffset = 44f,
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

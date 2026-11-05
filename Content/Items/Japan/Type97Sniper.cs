using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.Japan
{
    // Type 97 Sniper Rifle - Japan (Bolt-action rifle)
    public class Type97Sniper : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 95,
            UseTime = 45,
            Knockback = 6.0f,
            Velocity = 16f,
            Crit = 20,
            Spread = 0f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 1,
            Scope = true,
            AutoReuse = false,
            Rarity = ItemRarityID.Pink,
            BuyPriceGold = 28,
            Width = 69,
            Height = 18,
            HoldoutX = -12f,
            MuzzleOffset = 52f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item40;

        public override void AddRecipes()
        {
            Recipe recipe = CreateRecipe();
            recipe.AddRecipeGroup("WW2Guns:MythrilBar", 12);
            recipe.AddIngredient(ItemID.SoulofNight, 6);
            recipe.AddTile(TileID.MythrilAnvil);
            recipe.Register();
        }
    }
}

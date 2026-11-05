using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.Italy
{
    // Breda M37 - Italy (Machine gun)
    public class BredaM37 : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 34,
            UseTime = 9,
            Knockback = 2.5f,
            Velocity = 12f,
            Crit = 0,
            Spread = 3f,
            AmmoSaveChance = 0.33f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = true,
            Rarity = ItemRarityID.LightPurple,
            BuyPriceGold = 40,
            Width = 58,
            Height = 20,
            HoldoutX = -9f,
            MuzzleOffset = 44f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item11;

        public override void AddRecipes()
        {
            Recipe recipe = CreateRecipe();
            recipe.AddRecipeGroup("WW2Guns:AdamantiteBar", 14);
            recipe.AddIngredient(ItemID.SoulofNight, 8);
            recipe.AddIngredient(ItemID.IllegalGunParts, 1);
            recipe.AddTile(TileID.MythrilAnvil);
            recipe.Register();
        }
    }
}

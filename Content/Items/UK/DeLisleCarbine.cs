using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WW2Guns.Common;

namespace WW2Guns.Content.Items.UK
{
    // De Lisle Carbine - United Kingdom (Bolt-action rifle)
    public class DeLisleCarbine : WW2Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 40,
            UseTime = 30,
            Knockback = 3.0f,
            Velocity = 12f,
            Crit = 15,
            Spread = 0f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = false,
            Rarity = ItemRarityID.LightRed,
            BuyPriceGold = 18,
            Width = 55,
            Height = 12,
            HoldoutX = -8f,
            MuzzleOffset = 41f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item11 with { Volume = 0.35f, Pitch = -0.4f };

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

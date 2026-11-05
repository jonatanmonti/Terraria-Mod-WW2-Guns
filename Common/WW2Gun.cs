using Microsoft.Xna.Framework;
using Terraria;
using Terraria.Audio;
using Terraria.DataStructures;
using Terraria.ID;
using Terraria.ModLoader;

namespace WW2Guns.Common
{
    /// <summary>Stats for one gun. Each weapon class fills one of these.</summary>
    public class GunData
    {
        public int Damage;
        public int UseTime;
        public float Knockback;
        public float Velocity;
        public int Crit;
        public float Spread;          // max random spread, in degrees
        public float AmmoSaveChance;  // 0..1 chance to not consume ammo
        public int Pellets = 1;       // >1 = shotgun
        public int ExtraPierce;       // extra enemies each bullet passes through
        public bool Scope;            // right click zoom like the Rifle Scope
        public bool AutoReuse;
        public int Rarity;
        public int BuyPriceGold;
        public int Width;
        public int Height;
        public float HoldoutX;
        public float MuzzleOffset;
    }

    /// <summary>
    /// Shared behaviour for every WW2 gun: ranged damage, uses vanilla bullets
    /// (Musket Ball, Silver Bullet, Meteor Shot, etc.), spread, ammo saving, shotgun pellets and piercing.
    /// </summary>
    public abstract class WW2Gun : ModItem
    {
        protected abstract GunData Data { get; }
        protected abstract SoundStyle Sound { get; }

        public override void SetStaticDefaults()
        {
            Item.ResearchUnlockCount = 1; // Journey mode
        }

        public override void SetDefaults()
        {
            GunData d = Data;
            Item.width = d.Width;
            Item.height = d.Height;

            Item.DamageType = DamageClass.Ranged;
            Item.damage = d.Damage;
            Item.knockBack = d.Knockback;
            Item.crit = d.Crit;
            Item.noMelee = true;

            Item.useStyle = ItemUseStyleID.Shoot;
            Item.useTime = d.UseTime;
            Item.useAnimation = d.UseTime;
            Item.autoReuse = d.AutoReuse;
            Item.UseSound = Sound;

            // Standard gun setup: the real projectile comes from the ammo.
            Item.shoot = ProjectileID.PurificationPowder;
            Item.shootSpeed = d.Velocity;
            Item.useAmmo = AmmoID.Bullet;

            Item.rare = d.Rarity;
            Item.value = Item.buyPrice(gold: d.BuyPriceGold);
        }

        public override Vector2? HoldoutOffset() => new Vector2(Data.HoldoutX, 0f);

        public override bool CanConsumeAmmo(Item ammo, Player player)
            => Main.rand.NextFloat() >= Data.AmmoSaveChance;

        public override void HoldItem(Player player)
        {
            if (Data.Scope)
                player.scope = true;
        }

        public override void ModifyShootStats(Player player, ref Vector2 position, ref Vector2 velocity, ref int type, ref int damage, ref float knockback)
        {
            // Spawn the bullet at the muzzle instead of the player's hand.
            Vector2 muzzle = Vector2.Normalize(velocity) * Data.MuzzleOffset;
            if (Collision.CanHit(position, 0, 0, position + muzzle, 0, 0))
                position += muzzle;

            if (Data.Pellets <= 1 && Data.Spread > 0f)
                velocity = velocity.RotatedByRandom(MathHelper.ToRadians(Data.Spread));
        }

        public override bool Shoot(Player player, EntitySource_ItemUse_WithAmmo source, Vector2 position, Vector2 velocity, int type, int damage, float knockback)
        {
            GunData d = Data;
            if (d.Pellets > 1)
            {
                for (int i = 0; i < d.Pellets; i++)
                {
                    Vector2 v = velocity.RotatedByRandom(MathHelper.ToRadians(d.Spread)) * Main.rand.NextFloat(0.85f, 1.1f);
                    Projectile.NewProjectile(source, position, v, type, damage, knockback, player.whoAmI);
                }
                return false;
            }

            if (d.ExtraPierce > 0)
            {
                int p = Projectile.NewProjectile(source, position, velocity, type, damage, knockback, player.whoAmI);
                Projectile proj = Main.projectile[p];
                if (proj.penetrate > 0)
                    proj.penetrate += d.ExtraPierce;
                proj.usesLocalNPCImmunity = true;
                proj.localNPCHitCooldown = -1; // each enemy is hit once per bullet
                return false;
            }

            return true;
        }
    }
}

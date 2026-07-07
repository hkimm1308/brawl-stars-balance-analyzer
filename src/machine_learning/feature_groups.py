"""
Feature groups used throughout the machine learning experiments.

Keeping all feature definitions in one file ensures that every model,
ablation study, and hyperparameter search uses the exact same features.
"""

# -----------------------------
# Core Character Statistics
# -----------------------------

CORE_STATS = [
    "Health",
    "TotalDamage",
    "EffectiveRangeTiles",
    "RangeScore",
    "AmmoCount",
]

# -----------------------------
# Combat Characteristics
# -----------------------------

COMBAT = [
    "ReloadSpeedScore",
    "AttackCooldownScore",
    "ProjectileSpeedScore",
    "ProjectileWidthScore",
    "BurstDamageScore",
    "SustainedDPSScore",
    "SuperChargeRateScore",
]

# -----------------------------
# Gameplay & Skill Expression
# -----------------------------

GAMEPLAY = [
    "MobilityScore",
    "EngageScore",
    "EscapeScore",
    "AimPrecision",
    "PositioningImportance",
    "DecisionComplexity",
    "MechanicalDifficulty",
    "SkillFloor",
    "SkillCeiling",
    "AreaControlScore",
    "LaneControlScore",
    "ObjectivePressureScore",
    "TeamUtilityScore",
    "SurvivabilityScore",
    "PokePressureScore",
    "CloseRangeThreatScore",
]

# -----------------------------
# Binary Gameplay Mechanics
# -----------------------------

MECHANICS = [
    "HasThrowAttack",
    "HasShotgunSpread",
    "HasMeleePrimary",
    "HasContinuousAttack",
    "HasBounceAttack",
    "HasDeployableCore",
    "HasPrecisionProjectile",
    "HasMultiProjectilePattern",
    "HasAreaPrimary",
    "HasDash",
    "HasJumpOrTeleport",
    "HasHealing",
    "HasStun",
    "HasSlow",
    "HasKnockback",
    "HasPull",
    "HasSilence",
    "HasShield",
    "HasInvisibility",
    "HasPetOrSummon",
    "HasPiercing",
    "HasSplashDamage",
    "HasWallBreak",
    "CanZone",
    "CanScoutBushes",
]

# -----------------------------
# Categorical Features
# -----------------------------

CATEGORIES = [
    "Rarity",
    "PrimaryRoleGroup",
    "PrimaryAttackCategory",
    "RangeClass",
    "MovementSpeed",
    "RangeCategory",
    "Class",
    "ReloadSpeedClass",
    "AttackCooldownClass",
    "ProjectileSpeedClass",
    "ProjectileWidthClass",
    "BurstDamageClass",
    "SustainedDPSClass",
    "SuperChargeRateClass",
    "HealingType",
    "SuperType",
    "HealingGroup",
    "SuperTypeGroup",
    "PrimaryWinConditionGroup",
]

# -----------------------------
# Combined Feature Sets
# -----------------------------

ALL_FEATURES = (
    CORE_STATS
    + COMBAT
    + GAMEPLAY
    + MECHANICS
    + CATEGORIES
)
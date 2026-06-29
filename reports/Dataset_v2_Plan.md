# Dataset Version 2 Plan

## Motivation

The first machine learning model demonstrated that the current dataset is too simplistic.

Many gameplay mechanics are represented as binary variables, which discard valuable information.

Example:

Current:

HasHealing = True

Improved:

HealingPerSecond = 420

or

HealingStrength = 4

---

# Planned Improvements

## Combat

- Reload Speed
- DPS
- Burst Damage
- Attack Cooldown
- Projectile Speed
- Projectile Width
- Super Charge Rate
- Super Recharge Rate

---

## Mobility

- Dash Distance
- Jump
- Teleport
- Speed Boost
- Wall Climb

---

## Utility

- Healing Amount
- Shield Strength
- Reveal Invisible
- Knockback Distance
- Pull Strength
- Root Duration
- Silence Duration

---

## Crowd Control

Instead of

HasStun

store

Stun Duration

Instead of

HasSlow

store

Slow Strength

or

Slow Duration

---

## Area Control

Replace

HasAreaControl

with

AreaControlStrength

Scale:

0–5

---

## Difficulty

Instead of one variable:

Skill Ceiling

Create multiple features:

- Mechanical Difficulty
- Positioning Difficulty
- Decision Complexity
- Skill Floor
- Skill Ceiling

---

# Long-Term Goal

The final objective is to build a machine learning model capable of estimating the expected Meta Score of a newly designed brawler before release using only gameplay characteristics.

This would allow the model to evaluate game balance before players have access to the character.
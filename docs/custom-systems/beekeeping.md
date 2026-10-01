# Beekeeping

Apiculture is the science (and some say art) of raising honey bees. Bees live together in groups called colonies and make their homes in beehives. Tending a hive is rewarding but takes a steady hand.

All you need to start is a beehive deed and an open area with plenty of flowers and water nearby.

- **Stages:** Hives grow through Colonizing → Brooding → Producing.
- **Health:** Overall health ranges from Dying to Thriving.
- **Resources:** Water and flowers within range feed the hive.
- **Treatments:** Pour potions into the hive to combat pests, illness, or fatigue.
- **Supplements:** Pollen Patties and sweetened water give the hive a small extra boost.
- **Harvest:** Once Producing, collect honey (bottles) and beeswax with a hive tool.

Hives perform a growth check once per day at world save. Watch the Last Tending indicator in the top-right of the control panel to see how the most recent check went.

!!! tip
    A single hive can support up to 100,000 bees. Healthy hives can live indefinitely, but older hives are more prone to disease.

## Getting started

You can find the Beekeeper NPC in Occlo at these coordinates 3694, 2544.

Single-click the NPC to find the [Reward Store](../game-mechanics/currencies.md#apiary-marks-store) or get a [Honey Order](#honey-orders).

From the vendor you can buy:

|                                 Item                                  |               Use               |
|:---------------------------------------------------------------------:|:-------------------------------:|
|       ![icon](../assets/items/beehive-deed.png)<br>Beehive Deed       |     Where the magic begins      |
|          ![icon](../assets/items/hive-tool.png)<br>Hive Tool          |   To harvester Honey and Wax    |
| ![icon](../assets/items/wax-processing-pot.png)<br>Wax Processing Pot | Process Raw Wax into usable Wax |
|   ![icon](../assets/items/wax-crafting-pot.png)<br>Wax Crafting Pot   |    Tool for crafting candles    |
|       ![icon](../assets/items/common-honey.png)<br>Common Honey       |                -                |

### Placing and activating a hive

A newly placed Beehive starts in **Dormant** mode. While it's dormant you can chop it with an axe to get the deed back, so you can try a different spot.

Double-click the Beehive to activate it and open the gump. Once a hive is active it can no longer be chopped down.

### Moving a hive

To move an active hive, stand on the spot in your house where you want it and use the Move Hive option on the gump. Only the owner of the house the hive stands in can relocate it.

Moving a hive disturbs the bees, so it pushes the next growth check back by 4 hours.

### Hibernation

You can put a hive into hibernation from the gump. While it hibernates, growth, production, and maladies are all on hold, and you can't extract honey or wax.

### Destroying a hive

To destroy an active hive, use the button on the gump. You only need an axe if the hive is empty or dead, and the deed is not returned.

## Stages

Every beehive grows through five internal stages, grouped into three named phases visible on the control panel.

### Colonizing (Stages 1 - 2)

Newly placed hives begin here. Scouts survey the surrounding terrain for water and flowers. No honey or wax is produced yet, but the colony is establishing itself.

### Brooding (Stages 3 - 4)

Egg-laying ramps up as the colony prepares for full production. Population increases steadily if conditions are good.

### Producing (Stage 5)

The hive has matured. Excess honey and beeswax are now generated each growth check. A thriving colony produces these at an increased rate.

If conditions get bad enough - illness, infestation, or prolonged shortages - the colony may abscond, leaving an empty hive behind. Redeem an empty hive with an axe.

## Health

A hive's wellbeing is measured by two values: Overall Health and Population.

### Overall Health

<span style="color: #7799ee;">**Thriving:**</span> Extremely healthy. Honey and wax are produced at an increased rate.

<span style="color: #80e732;">**Healthy:**</span> Producing normally with surplus honey and wax.

<span style="color: #f28b00;">**Sickly:**</span> Producing has stalled. Apply treatments and check resources.

<span style="color: #ff0000;">**Dying:**</span> Act quickly - population will start dropping if not stabilized.

### Population

Population is a rough count of bees in the hive. More is not always better. Larger hives consume more water and flowers, and the area they forage from grows with their size - so resources must scale with them.

If a hive runs out of resources for too long, bees will die off or the entire colony may abandon the hive. Keep an eye on the Resources tab.

## Resources

Bees need both water and flowers within their foraging range. The control panel shows the status of each as a coloured label plus the source count.

### Water
  
Place filled water barrels or tubs near the hive. Each one counts as a source while it holds water; hives gradually drain them. Note that too much water can breed bacteria, making the hive more susceptible to disease.

Water barrels can be crafted with [Carpentry](../skills/crafting/carpentry.md#__tabbed_1_6).

#### Sweetened water

Add **Refined Sugar** to a water barrel to sweeten it, which gives the bees a slight water boost. You can get Refined Sugar as a [Cooking BOD reward](../skills/crafting/cooking.md#bod-rewards).

### Flowers

Flowers are used for food, building, and almost every hive function. An overabundance of flowers brings more parasites and insects with them.

- Flowers must be in non-decorative mode
- Flowers that are around beehives will see a slight boost in resistance to parasites and health
- Certain flowers slightly increase the chances that the harvested honey will be of a rarer quality

The following flowers make the bees happy:

|                                                                     |                                                                  |                                                                    |                                                      |                                                         |
|:-------------------------------------------------------------------:|:----------------------------------------------------------------:|:------------------------------------------------------------------:|:----------------------------------------------------:|:-------------------------------------------------------:|
|  ![icon](../assets/items/hops-plant-east.png)<br>Hops Plant (East)  | ![image](../assets/items/campion-flowers.png)<br>Campion Flowers | ![image](../assets/items/foxglove-flowers.png)<br>Foxglove Flowers |    ![image](../assets/items/lilies.png)<br>Lilies    |    ![icon](../assets/items/cattails.png)<br>Cattails    |
| ![icon](../assets/items/hops-plant-south.png)<br>Hops Plant (South) |         ![image](../assets/items/poppies.png)<br>Poppies         |  ![image](../assets/items/orfluer-flowers.png)<br>Orfluer Flowers  | ![image](../assets/items/snowdrops.png)<br>Snowdrops | ![icon](../assets/items/water-lilly.png)<br>Water Lilly |

For more information about flowers visit the [Gardening](../game-mechanics/gardening.md) page.

### Foraging Range  

Base range: 2 tiles plus 1 per population level.

Agility boost: ![](../assets/items/agility-potion.png) Greater Agility potions extend range by 1 per dose for the growth check.

### Reading the Status

<span style="color: #80e732;">**Adequate / Plentiful:**</span> Resources are well-matched to the colony's size.

<span style="color: #f28b00;">**Low / Very Low:**</span> Add more sources or the hive will stop growing.

<span style="color: #ff0000;">**Excessive / Overflowing:**</span> Too much. Remove some sources to lower disease and pest risk.

## Treatments

Pour potions from your backpack into the hive using the Potion Treatments panel. Each potion type holds up to 2 doses at a time; the doses are consumed at the next growth check.

- ![](../assets/items/agility-potion.png) **Greater Agility:** Boosts honey and wax output and extends foraging range. Bees work harder for one growth cycle.
- ![](../assets/items/poison-potion.png) **Greater Poison / Deadly Poison:** Kills parasitic mites and wax moths. Excess poison harms the bees - use only when infestation is present.
- ![](../assets/items/cure-potion.png) **Greater Cure:** Cures foul brood, dysentery, and other diseases. Also neutralizes lingering poison in the hive.
- ![](../assets/items/heal-potion.png) **Greater Heal:** Restores hive health, but only if the hive has no active parasites or disease. Cure those first.
- ![](../assets/items/strength-potion.png) **Greater Strength:** Builds up immunity, reducing the chance of future infestations and illness.

Lesser and standard potions are too weak - only Greater (and Deadly Poison) varieties have any effect.

## Pollen Patties

A **Pollen Patty** is a supplement you can apply to a hive to slightly raise the chance of harvesting better quality honey. It works alongside the [flowers](#flowers) that already improve honey quality.

You can get Pollen Patties as a [Cooking BOD reward](../skills/crafting/cooking.md#bod-rewards).

## Indicators

The Last Tending pill in the top-right of the control panel summarizes what happened at the most recent growth check.

- <span style="color: #80e732;">**▲ Population grew:**</span> A new bee population level was reached.
- <span style="color: #7799ee;">**▲ Hive matured:**</span> The hive advanced a stage or produced honey/wax this cycle.
- <span style="color: #ff0000;">**▼ Population fell:**</span> The colony lost bees - usually from illness, pests, or shortage.
- <span style="color: #ff0000;">**! Too sickly to grow:**</span> Overall health is below Healthy; fix that before it can grow.
- <span style="color: #f28b00;">**! Resources too low:**</span> Water or flowers were insufficient at the last check.
- **– No change yet:** The hive hasn't had a growth check since being placed.

Growth checks happen during the daily world save. If you make changes after the check, you'll see the results at the next save.

## Honey

Once a hive reaches the Producing stage, use the Harvest button on the control panel. A hive tool and empty bottles are required - each harvester uses a charge.

Once you have the Honey, use [Taste Identification](../skills/utility-and-support/taste-identification.md) to identify the type. You have three attempts. If you fail all three, the Honey will default to Wildflower or Clover.

[Item Identification](../skills/utility-and-support/item-identification.md) adds a 5% success rate boost when using Taste ID.

Honey is used in [Cooking](../skills/crafting/cooking.md) and [Honey Orders](#honey-orders).

## Wax

Beeswax straight from the hive is full of impurities and difficult to work with. The process of cleaning it is called rendering.

Wax is used to [craft candles](#wax-crafting-list).

### Step 1: Scrape the Hive

Once a hive reaches the Producing stage, use the Harvest button on the control panel. A hive tool is required - each scrape uses a charge.

### Step 2: Render in a Wax Pot

Place the raw beeswax into a small wax pot, then set the pot on a heat source. The wax melts and the impurities - called slumgum - separate out.

### Step 3: Form Pure Beeswax

With the slumgum removed, the rendered wax can be poured into ingots or moulds, ready for crafting candles, polish, seals, or anything else a clever artisan needs.

!!! Tip
    Rendering takes time over the heat. Make sure you have a steady fire and don't wander too far from the pot.

### Wax types

Currently all wax types are treated the same whenever wax is required, and slumgum is simply a byproduct with no current use.

|                           Wax type                            |                                                         |                                                           |                                                               |                                                           |                     Slumgum                     |
|:-------------------------------------------------------------:|:-------------------------------------------------------:|:---------------------------------------------------------:|:-------------------------------------------------------------:|:---------------------------------------------------------:|:-----------------------------------------------:|
| ![icon](../assets/items/common-beeswax.png)<br>Common Beeswax | ![icon](../assets/items/raw-beeswax.png)<br>Raw Beeswax | ![icon](../assets/items/fine-beeswax.png)<br>Fine Beeswax | ![icon](../assets/items/virgin-beeswax.png)<br>Virgin Beeswax | ![icon](../assets/items/pure-beeswax.png)<br>Pure Beeswax | ![icon](../assets/items/slumgum.png)<br>Slumgum |

## Honey orders

To get a Honey Order, single‑click the Beekeeper NPC in Occlo at coordinates 3694, 2544

You can get one order every 24 hours per account.

Unlike BODs, the timer doesn't reset when you turn an order in.

Completed orders must be turned in to the Beekeeper NPC.

Completing orders will award Apiary Marks that can be exchanged for [rewards](../game-mechanics/currencies.md#apiary-marks-store).

|                       Order Tiers                        |                                                              |                                                      |                                                                    |
|:--------------------------------------------------------:|:------------------------------------------------------------:|:----------------------------------------------------:|:------------------------------------------------------------------:|
| ![icon](../assets/items/simple-honey-oder.png)<br>Simple | ![icon](../assets/items/standard-honey-oder.png)<br>Standard | ![icon](../assets/items/rare-honey-oder.png)<br>Rare | ![icon](../assets/items/exceptional-honey-oder.png)<br>Exceptional |

|                                Honey Type                                 | Points |
|:-------------------------------------------------------------------------:|:------:|
|         ![icon](../assets/items/clover-honey.png)<br>Clover Honey         |   1    |
|     ![icon](../assets/items/wildflower-honey.png)<br>Wildflower Honey     |   2    |
|      ![icon](../assets/items/buckwheat-honey.png)<br>Buckwheat Honey      |   3    |
| ![icon](../assets/items/orange-blossom-honey.png)<br>Orange Blossom Honey |   3    |
|       ![icon](../assets/items/lavender-honey.png)<br>Lavender Honey       |   6    |
|        ![icon](../assets/items/heather-honey.png)<br>Heather Honey        |   8    |
|       ![icon](../assets/items/sourwood-honey.png)<br>Sourwood Honey       |   15   |
|         ![icon](../assets/items/tupelo-honey.png)<br>Tupelo Honey         |   25   |

## Wax Crafting list

This table shows what you can craft using the Wax Crafting Pot.

The skill required for crafting is Taste Identification.

The hue of colored candles is random.

=== "Resources"

    |                           Item                            |    Resources     | Skill |
    |:---------------------------------------------------------:|:----------------:|:-----:|
    |  ![icon](../assets/items/candle-wick.png)<br>Candle Wick  | 1 Wax<br>1 Cloth | 50.0  |
    | ![icon](../assets/items/blank-candle.png)<br>Blank Candle |      2 Wax       | 50.0  |

=== "Candles"

    |                                   Item                                    |                           Resources                            | Skill |
    |:-------------------------------------------------------------------------:|:--------------------------------------------------------------:|:-----:|
    |         ![icon](../assets/items/small-candle.png)<br>Small Candle         |                1 Blank Candle<br>1 Candle Wick                 | 80.0  |
    | ![icon](../assets/items/small-colored-candle.png)<br>Small Colored Candle |           1 Blank Candle<br>1 Dyes<br>1 Candle Wick            | 80.0  |
    |         ![icon](../assets/items/large-candle.png)<br>Large Candle         |                1 Blank Candle<br>1 Candle Wick                 | 80.0  |
    | ![icon](../assets/items/large-colored-candle.png)<br>Large Colored Candle |           1 Blank Candle<br>1 Dyes<br>1 Candle Wick            | 80.0  |
    |         ![icon](../assets/items/skull-candle.png)<br>Skull Candle         |     1 Blank Candle<br>1 Candle Wick<br>1 Candle Fit Skull      | 80.0  |
    |       ![icon](../assets/items/candle-of-love.png)<br>Candle of Love       | 1 Blank Candle<br>1 Dyes<br>1 Candle Wick<br>1 Essence Of Love | 80.0  |

=== "Decorative"

    |                                    Item                                     |    Resources    | Skill |
    |:---------------------------------------------------------------------------:|:---------------:|:-----:|
    |         ![icon](../assets/items/dipping-stick.png)<br>Dipping Stick         | 3 Blank Candle  | 75.0  |
    | ![icon](../assets/items/pile-of-blank-candles.png)<br>Pile of Blank Candles | 5 Blank Candle  | 75.0  |
    |    ![icon](../assets/items/some-blank-candles.png)<br>Some Blank Candles    | 3 Blank Candle  | 75.0  |
    |          ![icon](../assets/items/raw-wax-bust.png)<br>Raw Wax Bust          |      4 Wax      | 85.0  |
    |    ![icon](../assets/items/pot-of-molten-gold.png)<br>Pot of Molten Gold    | 30 Blank Candle | 75.0  |

## Related pages

- [Taste Identification](../skills/utility-and-support/taste-identification.md)
- [Item Identification](../skills/utility-and-support/item-identification.md)
- [Gardening](../game-mechanics/gardening.md)
- [Cooking](../skills/crafting/cooking.md)
- [Apiary Marks Store](../game-mechanics/currencies.md#apiary-marks-store)

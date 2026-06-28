# Gardening

New Dawn's gardening system lets you grow and cross-pollinate a wide variety of decorative plants. Seeds are planted in pots, cared for over several days, and bred with other plants to unlock new varieties and color combinations. All fully grown plants are **purely decorative** — they exist to beautify your home and nothing more.

---

## Getting Started

Plants are grown in **plant pots**, purchased from the provisioner. Before you can plant a seed, the pot needs to be prepared:

1. Buy an empty plant pot from the provisioner.
2. Find a bare patch of earth (roadside dirt works) and fill the pot with soil.
3. With a **jug of water** in your pack, double-click the pot to open the plant gump, then click the water jug icon **twice** to soften the soil.
4. Double-click your seed and target the pot to plant it.

Once planted, the pot needs to be **locked down in your house** or carried in your **backpack** for the plant to grow.

### Growth Checks

| Location                    | Frequency                 | Notes                                 |
| --------------------------- | ------------------------- | ------------------------------------- |
| Locked down in a house      | Once per day at server up | Plant will sicken if left untended    |
| Character's backpack        | Every 23 hours            | Only while the character is logged in |
| Secure container / bank box | Never                     | Plant will neither grow nor sicken    |

---

## Seeds

### Basic Seeds

The most common seeds drop from **Bog Things** and their **Boglings**. They come in four starting colors — **Red**, **Blue**, **Yellow**, and **Plain** — and grow into one of the three first-generation plant types. These seeds are the foundation of the cross-pollination system.

### Rare Seeds

Rare colored seeds yield plants in unusual colors, including **Black** and **White** which can also emerge as mutations from regular breeding. Plants grown from rare seeds are endpoint decoratives — they cannot be cross-pollinated and produce no seeds.

### Bonsai Seeds

Found on creatures in the **Tokuno Islands**, bonsai seeds grow into miniature decorative trees in five rarity tiers:

- Common
- Uncommon
- Rare
- Exceptional
- Exotic

Like rare seeds, bonsai plants cannot be cross-pollinated and produce no seeds.

---

## Plant Types and Generations

There are **17 breedable plant types** arranged across four generations. Higher generation plants can only be unlocked through cross-pollination.

### Generation 1

| Plant            |
| ---------------- |
| Tribarrel Cactus |
| Fern             |
| Campion Flowers  |

### Generation 2

| Plant       | Parents                 |
| ----------- | ----------------------- |
| Water Plant | Tribarrel Cactus × Fern |
| Lilies      | Campion Flowers × Fern  |

### Generation 3

| Plant               | Parents                        |
| ------------------- | ------------------------------ |
| Prickly Pear Cactus | Tribarrel Cactus × Water Plant |
| Small Palm          | Water Plant × Fern             |
| Rushes              | Lilies × Fern                  |
| Snowdrops           | Lilies × Campion Flowers       |

### Generation 4

| Plant         | Parents                                |
| ------------- | -------------------------------------- |
| Barrel Cactus | Tribarrel Cactus × Prickly Pear Cactus |
| Snake Plant   | Water Plant × Prickly Pear Cactus      |
| Century Plant | Water Plant × Small Palm               |
| Ponytail Palm | Small Palm × Fern                      |
| Elephant Ears | Fern × Rushes                          |
| Pampas Grass  | Rushes × Lilies                        |
| Bulrushes     | Lilies × Snowdrops                     |
| Poppies       | Snowdrops × Campion Flowers            |

---

## Cross-Pollination

When a plant reaches **day 7** of its growth cycle it begins producing pollen and can be cross-pollinated. Left alone, it will self-pollinate by day 9, producing seeds that grow into an identical copy of the parent. To create a hybrid you must manually pollinate it with pollen from a different plant before that happens.

**How to cross-pollinate:**

1. Open the plant gump of the pollen donor and navigate to **Page 2**.
2. Click the **Cross-Pollinate** button — this gives you a targeting cursor.
3. Target the receiving plant. That plant will now produce hybrid seeds.

!!! info "One Pollination Per Plant"
A plant can only be pollinated once. You can still collect pollen from an already-pollinated plant to use on others, but the pollinated plant itself cannot receive pollen again.

### Calculating the Offspring Type

Each of the 17 breedable plants has an assigned number. Add the two parent numbers together, then divide by two. If the result is a whole number, that is the offspring. If the result is a decimal (odd sum), there is a **50/50 chance** of either adjacent plant type.

**Example:** Prickly Pear Cactus (3) × Ponytail Palm (8) = 11 ÷ 2 = 5.5 → offspring is either a Water Plant (5) or a Century Plant (6).

| #   | Plant               |
| --- | ------------------- |
| 1   | Tribarrel Cactus    |
| 2   | Barrel Cactus       |
| 3   | Prickly Pear Cactus |
| 4   | Fern                |
| 5   | Water Plant         |
| 6   | Century Plant       |
| 7   | Small Palm          |
| 8   | Ponytail Palm       |
| 9   | Snake Plant         |
| 10  | Elephant Ears       |
| 11  | Campion Flowers     |
| 12  | Lilies              |
| 13  | Snowdrops           |
| 14  | Rushes              |
| 15  | Pampas Grass        |
| 16  | Bulrushes           |
| 17  | Poppies             |

### Color Mixing

Colors combine like paint. Crossing two plants of **different** colors always produces a **dull** result; crossing two plants of the **same** color produces a **bright** version.

|            | Red        | Blue        | Yellow        | Purple        | Green        | Orange        | Plain |
| ---------- | ---------- | ----------- | ------------- | ------------- | ------------ | ------------- | ----- |
| **Red**    | Bright Red | Purple      | Orange        | Red           | Red          | Red           | Plain |
| **Blue**   | Purple     | Bright Blue | Green         | Blue          | Blue         | Blue          | Plain |
| **Yellow** | Orange     | Green       | Bright Yellow | Yellow        | Yellow       | Yellow        | Plain |
| **Purple** | Red        | Blue        | Yellow        | Bright Purple | Blue         | Red           | Plain |
| **Green**  | Red        | Blue        | Yellow        | Blue          | Bright Green | Yellow        | Plain |
| **Orange** | Red        | Blue        | Yellow        | Red           | Yellow       | Bright Orange | Plain |
| **Plain**  | Plain      | Plain       | Plain         | Plain         | Plain        | Plain         | Plain |

**Key rules:**

- Primary colors: **Red, Blue, Yellow**
- Secondary colors: **Purple, Green, Orange**
- Two different primaries → secondary color
- Primary + secondary (or two different secondaries) → primary color
- Anything × **Plain** → Plain
- **Black** and **White** are rare mutations; plants of these colors produce no seeds and cannot be bred further

---

## Caring for Your Plants

Each daily growth check evaluates your plant's overall health. Neglected or improperly treated plants will sicken and may die. Double-click the pot at any time to open the plant gump and check its status.

### Plant Gump — Page 1

#### Growth Stage (Top Left)

Tracks days 1–9. The plant reaches maturity at **day 7** (pollen becomes available). At **day 9** it self-pollinates if you haven't done so, the counter stops, and the plant can be set as decorative.

#### Growth Result (Top Right)

| Icon     | Meaning                             |
| -------- | ----------------------------------- |
| Red !    | Plant is in an invalid location     |
| Red −    | Plant is unhealthy and did not grow |
| Yellow − | Growth check hasn't happened yet    |
| Blue +   | Grew successfully                   |
| Green +  | Accelerated growth (fertile soil)   |

#### Watering

Apply water each cycle using a **jug of water** in your backpack:

| Status   | Meaning           | Action                        |
| -------- | ----------------- | ----------------------------- |
| Yellow − | Needs water       | Click jug icon once           |
| Red −    | Very thirsty      | Click jug icon twice          |
| +        | Correctly watered | Nothing needed                |
| Red +    | Overwatered       | Do not water again this cycle |

#### Insect Infestation

Treat with **Greater Poison Potions** in your backpack:

| Icon     | Severity | Clicks Required |
| -------- | -------- | --------------- |
| Yellow + | Minor    | 1               |
| Red +    | Severe   | 2               |

#### Fungus Infection

Treat with **Greater Cure Potions** in your backpack:

| Icon     | Severity | Clicks Required |
| -------- | -------- | --------------- |
| Yellow + | Minor    | 1               |
| Red +    | Severe   | 2               |

#### Poisoned

Caused by over-applying Greater Poison Potions. Treat with **Greater Heal Potions** (1 or 2 clicks depending on severity).

#### Diseased

Caused by over-applying Greater Cure Potions. Treat with **Greater Heal Potions** (1 or 2 clicks depending on severity).

#### Strength Supplement

Using one **Greater Strength Potion** per day builds the plant's resistance to insect and fungus problems.

#### Remove Plant (Bottom Right)

Opens the option to remove the plant from the pot.

!!! warning "Removing a Plant"
Removed during seed or sapling stage: the seed is returned to your backpack along with the empty pot. Removed after the sapling stage: **the plant is destroyed** and only the empty pot is returned.

---

### Plant Gump — Page 2

#### Pollination State

| Symbol  | Meaning                                        |
| ------- | ---------------------------------------------- |
| −       | Not yet producing pollen (below day 7)         |
| Red X   | Cannot be cross-pollinated                     |
| Red !   | Pollen available — ready to collect or receive |
| Green + | Already pollinated                             |

#### Seed State

Displayed as `harvested / remaining`. Once the display reads `0/0` the plant will produce no further seeds. Click the harvest icon below to collect them.

#### Set Decorative (Top Right)

Only appears after day 9. Clicking this converts the plant into a permanent **decorative item** placed in your backpack that needs no further care.

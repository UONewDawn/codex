# SERVER PATCH 1.10

## April 19th, 2026

This patch introduces a new PvP Battleground called Conquest, the in-game Auction House, player vendor adjustments, CTF adjustments, and several bug fixes and enhancements.

## 🛠️ Bug Fixes & Enhancements

- Decorative plants will show the plant name
- You can set longer house names (was 16, now 32)
- If you log back into a Rift after being disconnected, if you have a timer left, it will keep you in the zone and not reset
- Added achievements and titles for champions (including Harrower)
- When Harrower is killed, like Champs, a message is sent to the main Discord channel (on a delay)
- Desert of Compassion has desert ambiance music
- The tailoring kits obtained as BOD reward can now be used to show clothing durability (similar to Arms Lore)
- Blessed clothing has a much lower chance of taking damage
- Updated the Codex Rift countdown gump to be more helpful
- Lowered the chances of cloth taking damage if blessed, and removed any damage when in a battleground like CTF or Conquest
- Fixed issue with transferring pets
- After you claim your pet, it will be at full happiness because the stable master treated your pet well
- Graceful hinds no longer drop the material needed for deer masks, instead the majestic stag does
- Tailors can now craft horned tribal masks and regular tribal masks. The materials for them drop off the horned goats and savages
- Added a tailoring BOD reward at 750 and 800, a tailoring apron that gives you +5 or +10 tailoring when worn
- Fixed guild resignation not showing the correct guild gump
- Rare horses can now be bonded regardless of taming skill level

## ⚔️ Conquest

Following on the heels of the release of Capture the Flag, Conquest is now available!

Compete for dominance in Ultima 7's Trinsic, where two teams compete for capture points within the town. Head over to Dawn (event center) and queue up!

- War tokens are awarded at the end of the game based on points (points are gained based on kills & caps)
- Conquest has its own daily cap outside of the daily cap you have in CTF
- Min 5v5 for teams and each team starts with 400 tickets

## 🚩 Capture the Flag

Just some adjustments to CTF based on feedback

- After the flag is capped and players are returned to base, a blocker is placed on the teleporter for 5 seconds
- Fixed issue preventing you from queuing up when the minimum number has been hit
- If you're dead at the end of a CTF match, you will be sent to Dawn
- Several CTF messages have been moved to be overhead messages instead of system message
- You no longer take damage on clothing when you're in a CTF (or duel)
- The scoreboard is now more compact and will display more often during a CTF match

## 💰 Player Vendors

Player vendors have seen some changes to better support the player economy

### 🏪 Vendor Upkeep

In a previous patch, the vendor charge was cut in half. To continue to balance out player vendors, the daily rate has been reduced again.

```csharp
daily_rate = (int)(60 + total_price_of_items_for_sale / 500 * 3)
```

This daily rate is reduced every real world day. For example, if you're selling 500k worth of items, you will be charged 3060gp per real world day. This is roughly a 50% cut to the existing cost.

### Other Changes

- You can now give your vendor a shop name, which will be displayed above their head
- If a shop is sold out of items, it will display "Sold Out" above their heads
- You can now view the paperdoll of your vendor
- You can now toggle your vendor to sell only to guild members
- You can now toggle a discount off your sale price for guild members
- When your vendor takes his daily vendor fee, if you have 2 or less days left, Iolo will attempt to send you a message on Discord.
- Vendors that have no items for sale, and haven't been refreshed by the owner will auto-dismiss in 30 days. Prior to that, on the 25th day, Iolo will attempt to send you a message on Discord.
- If your vendor is auto-dismissed, the gold they're holding for you will be placed in your bank
- If your vendor had 3 or less visitors with no sales, your per real world day charge is reduced again by 50%
- You can now see how many unique people visited your vendor on a daily basis and total visits
- You can now see your daily income and total income
- The gump has been updated to reflect the changes above

## 🔨 Auction House 🏠

The auction how is now live! You can now auction off items at the auctioneer just north of the Ocllo bank!

- Set starting bids, minimum increments, buyout prices, reserve prices, and auction duration (1h to 7d)
- Enable auto-extend so auctions cannot be 'sniped'
- Max of 3 active auctions per account
- Your item is held in "escrow" and is either given to the winner of the auction
- When a player bids, the gold is held in escrow
- If you get outbid, your hold is returned to you
- You can toggle Discord messages via `[profile` to help you follow your auctions
- The auction house takes 5% off the sale if they sell your item

## 🎣 Fishing

- Big fish now have proper weight variance. Most catches will land near the average, with heavy or light specimens being appropriately rare. Previously the formula heavily favored low weights and skipped some values entirely

Also, from the Fisherman's Guild:

<div class="rpg-scroll" markdown="1">
Notice from the Fisherman's Guild

Hear ye, anglers of harbor and coast — by word of the Fisherman's Guild, the deep waters have grown richer than before. **More than 35 new rare species** have been sighted in the far seas, each with a unique range of weight, awaiting those with the patience, skill, and fortune to draw them from the depths.

Furthermore, let it be known that the tides have at last spared honest fishers the indignity of dredging up **waterlogged boots and shoes**. Such debris has been cleared from the common catch, leaving the seas to yield treasures more fitting of the trade.

Cast true, and may your lines return heavy.

<span class="rpg-signature">The Fisherman's Guild</span>
</div>
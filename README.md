# DeepHammy - Virtual Hamster Pet
- The hamster has a set of mandatory survival needs and secondary needs. 
- Meeting a need provides the hamster with a reward over time. 
- The hamster naturally learns to maximize rewards over time. 
- Only what the hamster currently thinks will maximize its reward is displayed to the user, rather than what it actually may need.
- Not all rewards are positive. For instance, hamsternip provides a reward upfront, but negatively impacts the hamsters health over time.

## Survival Needs
If primary needs are not met, hamster receives reduced rewards for secondary needs.
- Eating
- Drinking
- Sleeping

## Secondary Needs
- HamsterNip
- Petting
- Toys

## Emotions
Hamster emotional state effects its reward levels
- Neutral - This is the base hamster state. No effect to rewards.
- Happy - When hamster receives alot of rewards. Rewards are increased further.
- Angry - When the hamster has unmet needs to has a chance to become angry. Hamster wrecks the toys / food / water you gave him in a fit of rage. 
- Sad - When hamster does not receive many rewards. Hamster less likely to eat, drink, or sleep. Easier to fall into addictions.

## Nueral Network
### Inputs
- Hunger
- Thirst
- Sleep
- HamsterNip Addiction
- Affection
- Entertainment

### Outputs
- Needs (Eat, Drink, Sleep, HamsterNip, Attention, Toys)
- Emotion (Neutral, Happy, Angry, Sad)
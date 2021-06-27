
# enum?
type HarvestColours { TODO_REMOVE_THIS: u8 }

type HarvestCraftOptionIcons {
  Id: string @unique
  DDSFile: string
}

type HarvestCraftOptions {
  Id: string @unique
  Text: string
  _: i32
  HarvestObjectsKey: HarvestObjects
  HarvestCraftTiersKey: HarvestCraftTiers
  Command: string
  Parameters: string
  AchievementItemsKeys: [AchievementItems]
  _: bool
  _: i32
  HarvestCraftOptionIconsKeys: [HarvestCraftOptionIcons]
  PlainText: string
}

type HarvestCraftTiers {
  Id: string @unique
  FrameImage: string
  FrameHighlight: string
}

type HarvestDurability {
  HarvestObjectsKey: HarvestObjects @unique
  Durability: i32
}

type HarvestEncounterScaling {
  Level: i32
  Multiplier: f32
  StatsKeys: [u64]
  StatsValues: [i32]
}

type HarvestInfrastructure {
  HarvestObjectsKey: HarvestObjects @unique
  _: i32
  _: i32
  _: i32
  _: rid
  _: rid
  _: i32
  _: rid
  _: [rid]
  _: i32
  HarvestInfrastructureKey: HarvestInfrastructure
}

# enum?
type HarvestInfrastructureCategories { TODO_REMOVE_THIS: u8 }

# enum?
type HarvestMetaCraftingOptions { TODO_REMOVE_THIS: u8 }

type HarvestObjects {
  BaseItemTypesKey: BaseItemTypes @unique
  AOFile: string
  ObjectType: i32
}

type HarvestPerLevelValues {
  Level: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
}

# enum?
type HarvestPlantBoosterFamilies { TODO_REMOVE_THIS: u8 }

type HarvestPlantBoosters {
  HarvestObjectsKey: HarvestObjects @unique
  Radius: i32
  _: rid
  Lifeforce: i32
  AdditionalCraftingOptionsChance: i32
  RareExtraChances: i32
  HarvestPlantBoosterFamilies: i32
}

type HarvestSeedTypes {
  HarvestObjectsKey: HarvestObjects @unique
  _: rid
  GrowthCycles: i32
  AOFiles: [string]
  _: [i32]
  _: i32
  Tier: i32
  RequiredNearbySeed_Tier: i32
  RequiredNearbySeed_Amount: i32
  WildLifeforceConsumedPercentage: i32
  VividLifeforceConsumedPercentage: i32
  PrimalLifeforceConsumedPercentage: i32
  Text: string
  HarvestCraftOptionsKeys: [HarvestCraftOptions]
  _: i32
  _: [i32]
  AchievementItemsKeys: [AchievementItems]
  OutcomeType: i32
}

type HarvestSpecialCraftCosts {
  _: rid
  _: i32
  _: i32
}

type HarvestSpecialCraftOptions {
  _: rid
  _: i32
  _: rid
}
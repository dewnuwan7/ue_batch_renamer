#UE Batch Renamer by Dewnuwan Jayaweera
#tested on UE 5.3, 5.4 & 5.5

import unreal

# Custom Prefix
CUSTOM_PREFIX = ""

# maping ue asset types to  prefixes
ASSET_TYPE_PREFIXES = {
    "StaticMesh": "SM_",
    "Material": "MAT_",
    "MaterialInstanceConstant": "MI_",
    "Texture2D": "T_",
    "Blueprint": "BP_",
    "NiagaraSystem": "NS_",
    "SkeletalMesh": "SKM_",
    "World": "LVL_",
    "LevelSequence": "LS_"  
}

# remove known prefixees
KNOWN_PREFIXES = set(ASSET_TYPE_PREFIXES.values())

# get seleteced assets
selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()

for asset in selected_assets:
    original_name = asset.get_name()
    asset_path = unreal.EditorAssetLibrary.get_path_name_for_loaded_asset(asset)
    class_name = asset.get_class().get_name()


    type_prefix = ASSET_TYPE_PREFIXES.get(class_name, "UNK_")
    clean_name = original_name
    for prefix in KNOWN_PREFIXES:
        if clean_name.startswith(prefix):
            clean_name = clean_name[len(prefix):]
            break
    if CUSTOM_PREFIX and clean_name.startswith(CUSTOM_PREFIX):
        clean_name = clean_name[len(CUSTOM_PREFIX):]

    # new name 
    clean_name = clean_name.replace(" ", "_")
    new_name = f"{type_prefix}{CUSTOM_PREFIX}{clean_name}"

    # skipping rename
    if new_name == original_name:
        continue

    # Rename the asset
    new_asset_path = f"{unreal.Paths.get_path(asset_path)}/{new_name}"
    success = unreal.EditorAssetLibrary.rename_asset(asset_path, new_asset_path)

    if success:
        print(f"✅ Renamed: {original_name} ➜ {new_name}")
    else:
        print(f"❌ Failed to rename: {original_name}")

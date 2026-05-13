import bpy

# --------------------------------------------------
# CONSTANTS & DEFAULTS
# --------------------------------------------------

ARKIT_DEFAULTS = {
    "Brows": ["browDown","browDownLeft","browDownRight","browInnerUp","browOuterUp","browOuterUpLeft","browOuterUpRight"],
    "Eyes": ["eyeBlink","eyeBlinkLeft","eyeBlinkRight","eyeLookDown","eyeLookDownLeft","eyeLookDownRight","eyeLookIn","eyeLookInLeft","eyeLookInRight",
             "eyeLookOut","eyeLookOutLeft","eyeLookOutRight","eyeLookUp","eyeLookUpLeft","eyeLookUpRight","eyeSquint","eyeSquintLeft","eyeSquintRight","eyeWide","eyeWideLeft","eyeWideRight"],
    "Cheeks": ["cheekPuff","cheekSquint","cheekSquintLeft","cheekSquintRight"],
    "Jaw": ["jawForward","jawLeft","jawRight","jawOpen"],
    "Mouth": ["mouthClose","mouthFunnel","mouthPucker","mouthLeft","mouthRight","mouthSmile","mouthSmileLeft","mouthSmileRight",
              "mouthFrown","mouthFrownLeft","mouthFrownRight","mouthDimple","mouthDimpleLeft","mouthDimpleRight","mouthStretch","mouthStretchLeft","mouthStretchRight",
              "mouthRollLower","mouthRollUpper","mouthShrugLower","mouthShrugUpper","mouthPress","mouthPressLeft","mouthPressRight",
              "mouthLowerDown","mouthLowerDownLeft","mouthLowerDownRight","mouthUpperUp","mouthUpperUpLeft","mouthUpperUpRight", "tongueOut"],
    "Nose": ["noseSneer","noseSneerRight","noseSneerLeft"],
    "Other": []
}

VRM_DEFAULTS = {
    "Emotions": ["happy", "angry", "sad", "relaxed", "surprised", "neutral"],
    "Visemes":  ["aa", "ih", "ou", "ee", "oh"],
    "Blink":    ["blink", "blinkLeft", "blinkRight"],
    "Look":     ["lookUp", "lookDown", "lookLeft", "lookRight"],
}

VRCHAT_DEFAULTS = {
    "VRC_Eye": [
        "EyeLookOutRight", "EyeLookInRight", "EyeLookUpRight", "EyeLookDownRight",
        "EyeLookOutLeft", "EyeLookInLeft", "EyeLookUpLeft", "EyeLookDownLeft",
        "EyeClosedRight", "EyeClosedLeft", "EyeSquintRight", "EyeSquintLeft",
        "EyeWideRight", "EyeWideLeft", "EyeDilationRight", "EyeDilationLeft",
        "EyeConstrictRight", "EyeConstrictLeft",
    ],
    "VRC_Brow": [
        "BrowPinchRight", "BrowPinchLeft", "BrowLowererRight", "BrowLowererLeft",
        "BrowInnerUpRight", "BrowInnerUpLeft", "BrowOuterUpRight", "BrowOuterUpLeft",
    ],
    "VRC_Nose": [
        "NoseSneerRight", "NoseSneerLeft",
        "NasalDilationRight", "NasalDilationLeft", "NasalConstrictRight", "NasalConstrictLeft",
    ],
    "VRC_Cheek": [
        "CheekSquintRight", "CheekSquintLeft",
        "CheekPuffRight", "CheekPuffLeft", "CheekSuckRight", "CheekSuckLeft",
    ],
    "VRC_Jaw": [
        "JawOpen", "MouthClosed", "JawRight", "JawLeft", "JawForward",
        "JawBackward", "JawClench", "JawMandibleRaise",
    ],
    "VRC_Lip": [
        "LipSuckUpperRight", "LipSuckUpperLeft", "LipSuckLowerRight", "LipSuckLowerLeft",
        "LipSuckCornerRight", "LipSuckCornerLeft",
        "LipFunnelUpperRight", "LipFunnelUpperLeft", "LipFunnelLowerRight", "LipFunnelLowerLeft",
        "LipPuckerUpperRight", "LipPuckerUpperLeft", "LipPuckerLowerRight", "LipPuckerLowerLeft",
    ],
    "VRC_Mouth": [
        "MouthUpperUpRight", "MouthUpperUpLeft", "MouthLowerDownRight", "MouthLowerDownLeft",
        "MouthUpperDeepenRight", "MouthUpperDeepenLeft", "MouthUpperRight", "MouthUpperLeft",
        "MouthLowerRight", "MouthLowerLeft",
        "MouthCornerPullRight", "MouthCornerPullLeft", "MouthCornerSlantRight", "MouthCornerSlantLeft",
        "MouthFrownRight", "MouthFrownLeft", "MouthStretchRight", "MouthStretchLeft",
        "MouthDimpleRight", "MouthDimpleLeft",
        "MouthRaiserUpper", "MouthRaiserLower", "MouthPressRight", "MouthPressLeft",
        "MouthTightenerRight", "MouthTightenerLeft",
    ],
    "VRC_Tongue": [
        "TongueOut", "TongueUp", "TongueDown", "TongueRight", "TongueLeft",
        "TongueRoll", "TongueBendDown", "TongueCurlUp", "TongueSquish", "TongueFlat",
        "TongueTwistRight", "TongueTwistLeft",
    ],
    "VRC_Advanced": [
        "SoftPalateClose", "ThroatSwallow", "NeckFlexRight", "NeckFlexLeft",
    ],
    "VRC_Visemes": [
        "vrc.v_sil", "vrc.v_PP", "vrc.v_FF", "vrc.v_TH", "vrc.v_DD",
        "vrc.v_kk", "vrc.v_CH", "vrc.v_SS", "vrc.v_nn", "vrc.v_RR",
        "vrc.v_aa", "vrc.v_E", "vrc.v_I", "vrc.v_O", "vrc.v_U",
    ],
}

MMD_DEFAULTS = {
    "MMD_Visemes": ["あ", "い", "う", "え", "お", "ん", "∧", "ω"],
    "MMD_Expressions": [
        "まばたき", "笑い", "ウィンク", "ウィンク右", "ウィンク２",
        "なごみ", "じと目", "びっくり",
        "困る", "怒り", "にこり", "真面目", "てへぺろ", "照れ",
    ],
}

# ARKit shape → one or more VRChat Unified Expression shapes
ARKIT_TO_VRCHAT_MAP = [
    # Eye
    ("eyeBlinkLeft",     "EyeClosedLeft"),
    ("eyeBlinkRight",    "EyeClosedRight"),
    ("eyeSquintLeft",    "EyeSquintLeft"),
    ("eyeSquintRight",   "EyeSquintRight"),
    ("eyeWideLeft",      "EyeWideLeft"),
    ("eyeWideRight",     "EyeWideRight"),
    ("eyeLookUpLeft",    "EyeLookUpLeft"),
    ("eyeLookUpRight",   "EyeLookUpRight"),
    ("eyeLookDownLeft",  "EyeLookDownLeft"),
    ("eyeLookDownRight", "EyeLookDownRight"),
    ("eyeLookInLeft",    "EyeLookInLeft"),
    ("eyeLookInRight",   "EyeLookInRight"),
    ("eyeLookOutLeft",   "EyeLookOutLeft"),
    ("eyeLookOutRight",  "EyeLookOutRight"),
    # Brow  (browDown splits to both Lowerer and Pinch; browInnerUp is bilateral)
    ("browDownLeft",     "BrowLowererLeft"),
    ("browDownLeft",     "BrowPinchLeft"),
    ("browDownRight",    "BrowLowererRight"),
    ("browDownRight",    "BrowPinchRight"),
    ("browInnerUp",      "BrowInnerUpLeft"),
    ("browInnerUp",      "BrowInnerUpRight"),
    ("browOuterUpLeft",  "BrowOuterUpLeft"),
    ("browOuterUpRight", "BrowOuterUpRight"),
    # Cheek (cheekPuff is bilateral in ARKit)
    ("cheekPuff",        "CheekPuffLeft"),
    ("cheekPuff",        "CheekPuffRight"),
    ("cheekSquintLeft",  "CheekSquintLeft"),
    ("cheekSquintRight", "CheekSquintRight"),
    # Jaw
    ("jawOpen",    "JawOpen"),
    ("jawLeft",    "JawLeft"),
    ("jawRight",   "JawRight"),
    ("jawForward", "JawForward"),
    ("mouthClose", "MouthClosed"),
    # Nose
    ("noseSneerLeft",  "NoseSneerLeft"),
    ("noseSneerRight", "NoseSneerRight"),
    # Lips
    ("mouthFunnel", "LipFunnelUpperLeft"),
    ("mouthFunnel", "LipFunnelUpperRight"),
    ("mouthFunnel", "LipFunnelLowerLeft"),
    ("mouthFunnel", "LipFunnelLowerRight"),
    ("mouthPucker", "LipPuckerUpperLeft"),
    ("mouthPucker", "LipPuckerUpperRight"),
    ("mouthPucker", "LipPuckerLowerLeft"),
    ("mouthPucker", "LipPuckerLowerRight"),
    ("mouthRollLower", "LipSuckLowerLeft"),
    ("mouthRollLower", "LipSuckLowerRight"),
    ("mouthRollUpper", "LipSuckUpperLeft"),
    ("mouthRollUpper", "LipSuckUpperRight"),
    # Mouth
    ("mouthUpperUpLeft",    "MouthUpperUpLeft"),
    ("mouthUpperUpRight",   "MouthUpperUpRight"),
    ("mouthLowerDownLeft",  "MouthLowerDownLeft"),
    ("mouthLowerDownRight", "MouthLowerDownRight"),
    ("mouthSmileLeft",      "MouthCornerPullLeft"),
    ("mouthSmileRight",     "MouthCornerPullRight"),
    ("mouthFrownLeft",      "MouthFrownLeft"),
    ("mouthFrownRight",     "MouthFrownRight"),
    ("mouthStretchLeft",    "MouthStretchLeft"),
    ("mouthStretchRight",   "MouthStretchRight"),
    ("mouthDimpleLeft",     "MouthDimpleLeft"),
    ("mouthDimpleRight",    "MouthDimpleRight"),
    ("mouthPressLeft",      "MouthPressLeft"),
    ("mouthPressRight",     "MouthPressRight"),
    ("mouthShrugLower",     "MouthRaiserLower"),
    ("mouthShrugUpper",     "MouthRaiserUpper"),
    ("mouthLeft",           "MouthUpperLeft"),
    ("mouthLeft",           "MouthLowerLeft"),
    ("mouthRight",          "MouthUpperRight"),
    ("mouthRight",          "MouthLowerRight"),
    # Tongue
    ("tongueOut", "TongueOut"),
]

# VRM viseme → VRChat vrc.v_* viseme  (consonants use nearest vowel as approximation)
VRM_TO_VRC_VISEME_MAP = [
    ("aa", "vrc.v_aa"),
    ("ee", "vrc.v_E"),
    ("ih", "vrc.v_I"),
    ("oh", "vrc.v_O"),
    ("ou", "vrc.v_U"),
    ("aa", "vrc.v_FF"),  # f/v: open, teeth showing
    ("aa", "vrc.v_TH"),  # th: open, tongue forward
    ("aa", "vrc.v_DD"),  # d/t: open, tongue alveolar
    ("aa", "vrc.v_kk"),  # k/g: open
    ("ih", "vrc.v_CH"),  # ch/sh: front, narrow
    ("ih", "vrc.v_SS"),  # s/z: teeth close
    ("ih", "vrc.v_nn"),  # n/ng: front
    ("ou", "vrc.v_RR"),  # r: rounded
    # vrc.v_sil and vrc.v_PP stay at basis (no VRM equivalent)
]

# VRM blink/look → MMD eye expressions
VRM_TO_MMD_BLINK_MAP = [
    ("blink",      "まばたき"),   # blink both
    ("blinkLeft",  "ウィンク"),   # wink left
    ("blinkRight", "ウィンク右"), # wink right
    ("blinkLeft",  "ウィンク２"), # alt wink, approximate with left
    ("blink",      "笑い"),       # laugh/squint ≈ blink
    ("blink",      "なごみ"),     # relaxed eyes ≈ soft blink
    ("blink",      "じと目"),     # half-lidded ≈ blink
]

# VRM viseme → MMD Japanese viseme / expression
VRM_TO_MMD_MAP = [
    ("aa", "あ"),
    ("ih", "い"),
    ("ou", "う"),
    ("ee", "え"),
    ("oh", "お"),
    ("ou", "ω"),   # pout ≈ ou
    ("aa", "∧"),   # open triangle mouth ≈ aa
]

# --------------------------------------------------
# UTILITIES
# --------------------------------------------------

def sync_all_active_indices(context, shape_name):
    """Ensures the blue selection bar moves on Driver and all Driven meshes."""
    scene = context.scene
    objs = [t.obj for t in scene.ak_targets if t.obj]
    if scene.ak_driver_mesh:
        objs.append(scene.ak_driver_mesh)

    for o in objs:
        if o and o.type == 'MESH' and o.data.shape_keys:
            idx = o.data.shape_keys.key_blocks.find(shape_name)
            if idx != -1:
                o.active_shape_key_index = idx

def _copy_shape_on_obj(obj, src_name, dst_name):
    """Copy vertex positions from src shape key to dst shape key on one mesh. Returns True if src was found."""
    kb = obj.data.shape_keys.key_blocks
    src = kb.get(src_name)
    if not src:
        return False
    if dst_name not in kb:
        obj.shape_key_add(name=dst_name, from_mix=False)
    dst = kb[dst_name]
    for i in range(len(obj.data.vertices)):
        dst.data[i].co = src.data[i].co.copy()
    dst.value = 0.0
    return True

def autosort_shapes_logic(context):
    """Sorts shapes into ARKit/VRM folders by template order, Corrective_/Jiggle_ by prefix, then 'Other'."""
    scene = context.scene
    master = scene.ak_driver_mesh

    if not master or not master.data.shape_keys:
        return

    kb = master.data.shape_keys.key_blocks
    assigned_names = set()

    # 1. Clear current CSV strings to rebuild them in the correct order
    for g in scene.ak_groups:
        g.shapes_csv = ""

    # 2. Re-populate ARKit groups (always present)
    for folder_name, shape_template_list in ARKIT_DEFAULTS.items():
        group = next((g for g in scene.ak_groups if g.name == folder_name), None)
        if not group:
            group = scene.ak_groups.add()
            group.name = folder_name
        found_in_mesh = [s for s in shape_template_list if s in kb and s != "Basis"]
        assigned_names.update(found_in_mesh)
        group.shapes_csv = ",".join(found_in_mesh)

    # 3. Re-populate optional groups (VRM / VRChat / MMD) only when shapes are present
    for defaults in (VRM_DEFAULTS, VRCHAT_DEFAULTS, MMD_DEFAULTS):
        for folder_name, shape_template_list in defaults.items():
            found_in_mesh = [s for s in shape_template_list if s in kb and s != "Basis"]
            assigned_names.update(found_in_mesh)
            if found_in_mesh:
                group = next((g for g in scene.ak_groups if g.name == folder_name), None)
                if not group:
                    group = scene.ak_groups.add()
                    group.name = folder_name
                group.shapes_csv = ",".join(found_in_mesh)
            else:
                idx = scene.ak_groups.find(folder_name)
                if idx != -1:
                    scene.ak_groups.remove(idx)

    # 4. Prefix-based folders: Corrective_ and Jiggle_
    all_shape_names = [key.name for key in kb if key.name != "Basis"]
    for prefix, folder_name in [("Corrective_", "Corrective"), ("Jiggle_", "Jiggle")]:
        prefix_shapes = sorted(s for s in all_shape_names if s.startswith(prefix) and s not in assigned_names)
        assigned_names.update(prefix_shapes)
        if prefix_shapes:
            group = next((g for g in scene.ak_groups if g.name == folder_name), None)
            if not group:
                group = scene.ak_groups.add()
                group.name = folder_name
            group.shapes_csv = ",".join(prefix_shapes)
        else:
            idx = scene.ak_groups.find(folder_name)
            if idx != -1:
                scene.ak_groups.remove(idx)

    # 5. Everything else → Other
    other_group = next((g for g in scene.ak_groups if g.name == "Other"), None)
    if not other_group:
        other_group = scene.ak_groups.add()
        other_group.name = "Other"
    unassigned = sorted(key.name for key in kb if key.name != "Basis" and key.name not in assigned_names)
    other_group.shapes_csv = ",".join(unassigned)

    # 6. Push special folders to the bottom in order: Corrective, Jiggle, Other
    for fname in ["Corrective", "Jiggle", "Other"]:
        idx = scene.ak_groups.find(fname)
        if idx != -1:
            scene.ak_groups.move(idx, len(scene.ak_groups) - 1)

# --------------------------------------------------
# VRM ARMATURE UTILITIES
# --------------------------------------------------

def get_vrm_armature_and_extension():
    """Find the scene's VRM armature and its VRM 1.0 extension.
    Returns (armature_data, armature_obj, vrm_extension) or (None, None, None)."""
    armature = bpy.data.armatures.get("Armature")
    if not armature or not hasattr(armature, "vrm_addon_extension"):
        return None, None, None
    vrm_extension = armature.vrm_addon_extension
    if not hasattr(vrm_extension, "vrm1"):
        return None, None, None
    armature_obj = next(
        (o for o in bpy.data.objects if o.type == 'ARMATURE' and o.data == armature), None
    )
    return armature, armature_obj, vrm_extension

def get_vrm_mesh(context):
    """Return the best candidate mesh for VRM operations.
    Prefers the active object if it's a mesh with shape keys, falls back to any mesh with shape keys."""
    active = context.active_object
    if active and active.type == 'MESH' and active.data.shape_keys:
        return active
    return next((o for o in bpy.data.objects if o.type == 'MESH' and o.data.shape_keys), None)

def vrm_expression_exists(expressions, name):
    """Return True if a custom VRM expression with this name already exists."""
    return any(c.custom_name == name for c in expressions.custom)

def vrm_bind_exists(expression, mesh_obj, shape_name):
    """Return True if this mesh/shape combo is already bound to the expression."""
    return any(
        b.node.bpy_object == mesh_obj and b.index == shape_name
        for b in expression.morph_target_binds
    )

def add_vrm_expression_with_bind(arm_name, expressions, mesh_obj, shape_name):
    """Create a VRM custom expression and bind it to shape_name on mesh_obj.
    Returns True on success."""
    bpy.ops.vrm.add_vrm1_expressions_custom_expression(
        armature_name=arm_name, custom_expression_name=shape_name)
    new_custom = expressions.custom[-1]
    bpy.ops.vrm.add_vrm1_expression_morph_target_bind(
        armature_name=arm_name, expression_name=shape_name)
    if new_custom.morph_target_binds:
        bind = new_custom.morph_target_binds[-1]
        bind.node.bpy_object = mesh_obj
        bind.index = shape_name
        bind.weight = 1.0
        return True
    return False

# --------------------------------------------------
# DATA MODELS
# --------------------------------------------------

class AK_GroupItem(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(name="Group Name")
    is_expanded: bpy.props.BoolProperty(name="Expanded", default=True)
    shapes_csv: bpy.props.StringProperty(name="Shapes", default="")

class AK_Target(bpy.types.PropertyGroup):
    obj: bpy.props.PointerProperty(type=bpy.types.Object)

# --------------------------------------------------
# OPERATORS
# --------------------------------------------------

class AK_OT_select_shape_key(bpy.types.Operator):
    bl_idname = "ak.select_shape_key"
    bl_label = "Select Blendshape"
    bl_description = "Selects this blendshape on the driver and all driven meshes"
    
    shape_name: bpy.props.StringProperty()
    
    def execute(self, context):
        sync_all_active_indices(context, self.shape_name)
        return {'FINISHED'}

class AK_OT_add_arkit_shapes(bpy.types.Operator):
    bl_idname = "ak.add_arkit_shapes"
    bl_label = "Add ARKit Shapes (Batch)"
    bl_description = "Add the 52 default ARKit blendshapes and pre-mirrored base versions."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        target = scene.ak_driver_mesh
            
        if not target:
            self.report({'WARNING'}, "Assign main Driver mesh first.")
            return {'CANCELLED'}

        all_arkit = [s for g in ARKIT_DEFAULTS.values() for s in g]
        
        if not target.data.shape_keys: target.shape_key_add(name="Basis")
        kb = target.data.shape_keys.key_blocks
        for s_name in all_arkit:
            if s_name not in kb: target.shape_key_add(name=s_name)
            kb[s_name].value = 0.0

        autosort_shapes_logic(context)

        return {'FINISHED'}
    
class AK_OT_add_vrm_shapes(bpy.types.Operator):
    bl_idname = "ak.add_vrm_shapes"
    bl_label = "Add VRM Shapes (Batch)"
    bl_description = "Add the 18 default VRM blendshapes (Emotions, Visemes, Blink, Look)."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        target = scene.ak_driver_mesh

        if not target:
            self.report({'WARNING'}, "Assign main Driver mesh first.")
            return {'CANCELLED'}

        all_vrm = [s for g in VRM_DEFAULTS.values() for s in g]

        if not target.data.shape_keys: target.shape_key_add(name="Basis")
        kb = target.data.shape_keys.key_blocks
        for s_name in all_vrm:
            if s_name not in kb: target.shape_key_add(name=s_name)
            kb[s_name].value = 0.0

        autosort_shapes_logic(context)
        return {'FINISHED'}

class AK_OT_add_vrchat_shapes(bpy.types.Operator):
    bl_idname = "ak.add_vrchat_shapes"
    bl_label = "Add VRChat Shapes (Batch)"
    bl_description = "Add the VRCFT Unified Expression blendshapes for VRChat face tracking."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        target = scene.ak_driver_mesh

        if not target:
            self.report({'WARNING'}, "Assign main Driver mesh first.")
            return {'CANCELLED'}

        all_vrc = [s for g in VRCHAT_DEFAULTS.values() for s in g]

        if not target.data.shape_keys: target.shape_key_add(name="Basis")
        kb = target.data.shape_keys.key_blocks
        for s_name in all_vrc:
            if s_name not in kb: target.shape_key_add(name=s_name)
            kb[s_name].value = 0.0

        autosort_shapes_logic(context)
        return {'FINISHED'}


class AK_OT_add_mmd_shapes(bpy.types.Operator):
    bl_idname = "ak.add_mmd_shapes"
    bl_label = "Add MMD Shapes (Batch)"
    bl_description = "Add standard MMD viseme and expression blendshapes."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        target = scene.ak_driver_mesh

        if not target:
            self.report({'WARNING'}, "Assign main Driver mesh first.")
            return {'CANCELLED'}

        all_mmd = [s for g in MMD_DEFAULTS.values() for s in g]

        if not target.data.shape_keys: target.shape_key_add(name="Basis")
        kb = target.data.shape_keys.key_blocks
        for s_name in all_mmd:
            if s_name not in kb: target.shape_key_add(name=s_name)
            kb[s_name].value = 0.0

        autosort_shapes_logic(context)
        return {'FINISHED'}


class AK_OT_copy_arkit_to_vrchat(bpy.types.Operator):
    bl_idname = "ak.copy_arkit_to_vrchat"
    bl_label = "VRC from ARKit"
    bl_description = "Generate VRChat Unified Expression shapes by copying from the nearest matching ARKit blendshapes."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        objs = [o for o in ([scene.ak_driver_mesh] + [t.obj for t in scene.ak_targets])
                if o and o.type == 'MESH']
        if not objs:
            self.report({'WARNING'}, "No meshes found.")
            return {'CANCELLED'}
        for obj in objs:
            if not obj.data.shape_keys:
                obj.shape_key_add(name="Basis")
            for src, dst in ARKIT_TO_VRCHAT_MAP:
                _copy_shape_on_obj(obj, src, dst)
        autosort_shapes_logic(context)
        self.report({'INFO'}, "VRChat shapes generated from ARKit.")
        return {'FINISHED'}


class AK_OT_copy_vrm_to_vrc_visemes(bpy.types.Operator):
    bl_idname = "ak.copy_vrm_to_vrc_visemes"
    bl_label = "VRC Visemes from VRM"
    bl_description = "Generate vrc.v_* viseme shapes by copying from the nearest matching VRM visemes."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        objs = [o for o in ([scene.ak_driver_mesh] + [t.obj for t in scene.ak_targets])
                if o and o.type == 'MESH']
        if not objs:
            self.report({'WARNING'}, "No meshes found.")
            return {'CANCELLED'}
        for obj in objs:
            if not obj.data.shape_keys:
                obj.shape_key_add(name="Basis")
            for src, dst in VRM_TO_VRC_VISEME_MAP:
                _copy_shape_on_obj(obj, src, dst)
        autosort_shapes_logic(context)
        self.report({'INFO'}, "VRChat visemes generated from VRM.")
        return {'FINISHED'}


class AK_OT_copy_vrm_to_mmd(bpy.types.Operator):
    bl_idname = "ak.copy_vrm_to_mmd"
    bl_label = "MMD from VRM"
    bl_description = "Generate MMD viseme shapes by copying from the nearest matching VRM visemes."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        objs = [o for o in ([scene.ak_driver_mesh] + [t.obj for t in scene.ak_targets])
                if o and o.type == 'MESH']
        if not objs:
            self.report({'WARNING'}, "No meshes found.")
            return {'CANCELLED'}
        for obj in objs:
            if not obj.data.shape_keys:
                obj.shape_key_add(name="Basis")
            for src, dst in VRM_TO_MMD_MAP:
                _copy_shape_on_obj(obj, src, dst)
        autosort_shapes_logic(context)
        self.report({'INFO'}, "MMD visemes generated from VRM.")
        return {'FINISHED'}


class AK_OT_copy_vrm_blink_to_mmd(bpy.types.Operator):
    bl_idname = "ak.copy_vrm_blink_to_mmd"
    bl_label = "MMD Eyes from VRM"
    bl_description = "Generate MMD eye expression shapes by copying from the nearest matching VRM blink shapes."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        objs = [o for o in ([scene.ak_driver_mesh] + [t.obj for t in scene.ak_targets])
                if o and o.type == 'MESH']
        if not objs:
            self.report({'WARNING'}, "No meshes found.")
            return {'CANCELLED'}
        for obj in objs:
            if not obj.data.shape_keys:
                obj.shape_key_add(name="Basis")
            for src, dst in VRM_TO_MMD_BLINK_MAP:
                _copy_shape_on_obj(obj, src, dst)
        autosort_shapes_logic(context)
        self.report({'INFO'}, "MMD eye expressions generated from VRM blink shapes.")
        return {'FINISHED'}


class AK_OT_merge_lr_blendshape(bpy.types.Operator):
    bl_idname = "ak.merge_lr_blendshape"
    bl_label = "Merge L+R to Unified"
    bl_description = "Combines the Left and Right split shapes back into a single unified shape (left side from *Left, right side from *Right)."
    bl_options = {'REGISTER', 'UNDO'}

    shape_name: bpy.props.StringProperty()

    def execute(self, context):
        scene = context.scene
        left_name  = self.shape_name + "Left"
        right_name = self.shape_name + "Right"

        objs = [o for o in ([scene.ak_driver_mesh] + [t.obj for t in scene.ak_targets])
                if o and o.type == 'MESH' and o.data.shape_keys]

        if not objs:
            self.report({'WARNING'}, "No meshes with shape keys found.")
            return {'CANCELLED'}

        for obj in objs:
            kb = obj.data.shape_keys.key_blocks
            left_shape  = kb.get(left_name)
            right_shape = kb.get(right_name)
            basis       = kb.get("Basis")
            if not left_shape or not right_shape or not basis:
                continue

            if self.shape_name not in kb:
                obj.shape_key_add(name=self.shape_name, from_mix=False)
            unified = kb[self.shape_name]

            for i, v in enumerate(obj.data.vertices):
                b_co = basis.data[i].co
                if b_co.x > 0.001:
                    unified.data[i].co = left_shape.data[i].co.copy()
                elif b_co.x < -0.001:
                    unified.data[i].co = right_shape.data[i].co.copy()
                else:
                    unified.data[i].co = left_shape.data[i].co.copy()
            unified.value = 0.0

        autosort_shapes_logic(context)
        self.report({'INFO'}, f"Merged {left_name} + {right_name} → {self.shape_name}")
        return {'FINISHED'}


class AK_OT_swap_lr_names(bpy.types.Operator):
    bl_idname = "ak.swap_lr_names"
    bl_label = "Fix L/R Names"
    bl_description = "Swap the names of this shape and its Left/Right partner across all meshes (fixes inverted L/R assignments)."
    bl_options = {'REGISTER', 'UNDO'}

    shape_name: bpy.props.StringProperty()

    def execute(self, context):
        scene = context.scene
        name = self.shape_name
        if name.endswith("Left"):
            partner = name[:-4] + "Right"
        elif name.endswith("Right"):
            partner = name[:-5] + "Left"
        else:
            self.report({'WARNING'}, "Shape is not a Left/Right variant.")
            return {'CANCELLED'}

        objs = [o for o in ([scene.ak_driver_mesh] + [t.obj for t in scene.ak_targets])
                if o and o.type == 'MESH' and o.data.shape_keys]

        for obj in objs:
            kb = obj.data.shape_keys.key_blocks
            a = kb.get(name)
            b = kb.get(partner)
            if not a or not b:
                continue
            a.name = "__ak_tmp__"
            b.name = name
            kb["__ak_tmp__"].name = partner

        autosort_shapes_logic(context)
        self.report({'INFO'}, f"Swapped names: {name} ↔ {partner}")
        return {'FINISHED'}


class AK_OT_autosort_shapes(bpy.types.Operator):
    bl_idname = "ak.autosort_shapes"
    bl_label = "Autosort Shapes"
    bl_description = "Sorts shapes into ARKit folders by template order, then moves extras to 'Other'."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        autosort_shapes_logic(context)

        return {'FINISHED'}

class AK_OT_mirror_blendshape(bpy.types.Operator):
    bl_idname = "ak.mirror_blendshape"
    bl_label = "Split Left/Right"
    bl_description = "Splits the shape based on X axis across Driver and Driven meshes."
    bl_options = {'REGISTER', 'UNDO'}
    
    shape_name: bpy.props.StringProperty()
    
    def execute(self, context):
        scene = context.scene
        
        # Gather ALL meshes (Driver + Targets)
        objs = [t.obj for t in scene.ak_targets if t.obj]
        driver_obj = scene.ak_driver_mesh
        if driver_obj: objs.append(driver_obj)
        
        if not objs: return {'CANCELLED'}
        
        left_name = self.shape_name + "Left"
        right_name = self.shape_name + "Right"
        
        for obj in objs:
            if not obj or obj.type != 'MESH' or not obj.data.shape_keys: continue
            
            kb = obj.data.shape_keys.key_blocks
            target_shape = kb.get(self.shape_name)
            basis = kb.get("Basis")
            
            # Skip if this specific mesh doesn't have the shape we're trying to split
            if not target_shape or not basis: continue
            
            # 1. Delete existing L/R shapes on this mesh if they exist
            for n in (left_name, right_name):
                if n in kb:
                    obj.shape_key_remove(kb[n])
                    
            # 2. Create new Left and Right shapes
            left_shape = obj.shape_key_add(name=left_name, from_mix=False)
            right_shape = obj.shape_key_add(name=right_name, from_mix=False)
            
            # 3. Split based on X-Axis coordinates relative to THIS mesh's basis
            #    +X = character's left side   →  Left shape deforms, Right stays at basis
            #    -X = character's right side  →  Right shape deforms, Left stays at basis
            #    center (|x| <= 0.001)        →  both stay at basis (clean half-shapes)
            for i, v in enumerate(obj.data.vertices):
                b_co = basis.data[i].co
                s_co = target_shape.data[i].co

                if b_co.x > 0.001:
                    left_shape.data[i].co  = s_co
                    right_shape.data[i].co = b_co
                elif b_co.x < -0.001:
                    right_shape.data[i].co = s_co
                    left_shape.data[i].co  = b_co
                else:
                    left_shape.data[i].co  = b_co
                    right_shape.data[i].co = b_co
                    
        # 4. DIRECT DRIVER LINKING
        if driver_obj and driver_obj.data.shape_keys:
            for t in scene.ak_targets:
                tar = t.obj
                if not tar or not tar.data.shape_keys: continue
                
                # Only link the two new shapes we just made
                for n in (left_name, right_name):
                    t_kb = tar.data.shape_keys.key_blocks.get(n)
                    if t_kb:
                        t_kb.driver_remove("value")
                        drv = t_kb.driver_add("value").driver
                        drv.type = 'SUM'
                        var = drv.variables.new()
                        var.name = "src_val"
                        var.type = 'SINGLE_PROP'
                        # SAFELY TARGET THE OBJECT TO AVOID CRASHES
                        var.targets[0].id_type = 'OBJECT'
                        var.targets[0].id = driver_obj
                        var.targets[0].data_path = f'data.shape_keys.key_blocks["{n}"].value'
                
        autosort_shapes_logic(context)
        
        self.report({'INFO'}, f"Split {self.shape_name} into {left_name} and {right_name} and linked drivers.")
        return {'FINISHED'}

class AK_OT_swap_lr_blendshape(bpy.types.Operator):
    bl_idname = "ak.swap_lr_blendshape"
    bl_label = "Swap Left/Right"
    bl_description = "Swaps the vertex data between the Left and Right split shapes across all meshes."
    bl_options = {'REGISTER', 'UNDO'}

    shape_name: bpy.props.StringProperty()

    def execute(self, context):
        scene = context.scene
        objs = [t.obj for t in scene.ak_targets if t.obj]
        if scene.ak_driver_mesh:
            objs.append(scene.ak_driver_mesh)

        left_name  = self.shape_name + "Left"
        right_name = self.shape_name + "Right"

        for obj in objs:
            if not obj or obj.type != 'MESH' or not obj.data.shape_keys:
                continue
            kb = obj.data.shape_keys.key_blocks
            left_shape  = kb.get(left_name)
            right_shape = kb.get(right_name)
            if not left_shape or not right_shape:
                continue

            # Swap co data in place using a temp buffer
            for i in range(len(obj.data.vertices)):
                tmp = left_shape.data[i].co.copy()
                left_shape.data[i].co  = right_shape.data[i].co
                right_shape.data[i].co = tmp

        self.report({'INFO'}, f"Swapped {left_name} <-> {right_name}.")
        return {'FINISHED'}


class AK_OT_select_all_meshes(bpy.types.Operator):
    bl_idname = "ak.select_all_meshes"
    bl_label = "Select All Rig Meshes"
    bl_description = "Selects the Driver and all Target meshes in the Viewport."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.select_all(action='DESELECT')
        scene = context.scene
        objs = [t.obj for t in scene.ak_targets if t.obj]
        
        if scene.ak_driver_mesh:
            objs.append(scene.ak_driver_mesh)
            context.view_layer.objects.active = scene.ak_driver_mesh
            
        for o in objs:
            o.select_set(True)
            
        return {'FINISHED'}

class AK_OT_create_drivers(bpy.types.Operator):
    bl_idname = "ak.create_drivers"; bl_label = "Link Meshes"
    bl_description = "Create drivers on the secondary meshes controlled by the shared blendshapes with the main mesh."
    def execute(self, context):
        scene = context.scene
        src = scene.ak_driver_mesh
        if not src or not src.data.shape_keys: return {'CANCELLED'}
        for item in scene.ak_targets:
            tar = item.obj
            if not tar or tar == src: continue
            if not tar.data.shape_keys: tar.shape_key_add(name="Basis")
            for key in src.data.shape_keys.key_blocks:
                t_kb = tar.data.shape_keys.key_blocks.get(key.name)
                if not t_kb: continue
                t_kb.driver_remove("value")
                drv = t_kb.driver_add("value").driver
                drv.type = 'SUM'
                var = drv.variables.new()
                var.name = "src_val"
                var.type = 'SINGLE_PROP'
                var.targets[0].id_type = 'KEY'
                var.targets[0].id = src.data.shape_keys
                var.targets[0].data_path = f'key_blocks["{key.name}"].value'
        return {'FINISHED'}

class AK_OT_remove_drivers(bpy.types.Operator):
    bl_idname = "ak.remove_drivers"; bl_label = "Unlink Meshes"
    bl_description = "Remove the driver setup on the secondary meshes' blendshapes."
    def execute(self, context):
        for item in context.scene.ak_targets:
            tar = item.obj
            if not tar or not tar.data.shape_keys: continue
            for kb in tar.data.shape_keys.key_blocks: kb.driver_remove("value")
        return {'FINISHED'}

class AK_OT_select_basis(bpy.types.Operator):
    bl_idname = "ak.select_basis"; bl_label = "Select Basis"
    bl_description = 'Set all the "Basis" blendshapes as active.'
    def execute(self, context):
        scene = context.scene
        objs = [t.obj for t in scene.ak_targets if t.obj]
        if scene.ak_driver_mesh: objs.append(scene.ak_driver_mesh)
        for o in objs:
            if o.data.shape_keys: o.active_shape_key_index = 0
        return {'FINISHED'}

class AK_OT_global_zero(bpy.types.Operator):
    bl_idname = "ak.global_zero"; bl_label = "Zero Everything"
    bl_description = "Set all the blendshapes' values to 0."
    def execute(self, context):
        scene = context.scene
        objs = [t.obj for t in scene.ak_targets if t.obj]
        if scene.ak_driver_mesh: objs.append(scene.ak_driver_mesh)
        for o in objs:
            if o.data.shape_keys:
                for kb in o.data.shape_keys.key_blocks: 
                    kb.value = 0.0
        return {'FINISHED'}

class AK_OT_delete_all_shapes(bpy.types.Operator):
    bl_idname = "ak.delete_all_shapes"; bl_label = "Delete All Shapes"
    bl_description = "Deletes ALL blendshapes and folders on all the meshes, even your custom ones. Be careful."
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        obj = context.scene.ak_driver_mesh
        if obj and obj.data.shape_keys: obj.shape_key_clear()
        for t in context.scene.ak_targets:
            if t.obj and t.obj.data.shape_keys: t.obj.shape_key_clear()
        
        # Clear folders so it doesn't leave ghost items
        context.scene.ak_groups.clear()
        return {'FINISHED'}
    def invoke(self, context, event): return context.window_manager.invoke_confirm(self, event)

class AK_OT_target_add_selected(bpy.types.Operator):
    bl_idname = "ak.target_add_selected"; bl_label = "Add Selected"
    bl_description = "Adds the selected mesh or meshes to the list as secondary meshes."
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        for o in context.selected_objects:
            if o.type == 'MESH' and o != context.scene.ak_driver_mesh:
                if not any(t.obj == o for t in context.scene.ak_targets):
                    context.scene.ak_targets.add().obj = o
        return {'FINISHED'}

class AK_OT_target_remove(bpy.types.Operator):
    bl_idname = "ak.target_remove"; bl_label = "Remove"
    bl_description = "Removes the selected mesh or meshes to the list from secondary meshes."
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        if context.scene.ak_target_index >= 0: context.scene.ak_targets.remove(context.scene.ak_target_index)
        return {'FINISHED'}

class AK_OT_groups_toggle(bpy.types.Operator):
    bl_idname = "ak.groups_toggle"; bl_label = "Toggle All"
    def execute(self, context):
        s = not any(g.is_expanded for g in context.scene.ak_groups)
        for g in context.scene.ak_groups: g.is_expanded = s
        return {'FINISHED'}

class AK_OT_delete_single_shape(bpy.types.Operator):
    bl_idname = "ak.delete_single_shape"
    bl_label = "Delete Blendshape?"
    bl_description = "Delete this blendshape."
    bl_options = {'REGISTER', 'UNDO'}
    
    shape_name: bpy.props.StringProperty()

    def execute(self, context):
        scene = context.scene
        
        # 1. Clean up targets FIRST to safely kill the drivers
        for t in scene.ak_targets:
            tar = t.obj
            if tar and tar.data.shape_keys:
                kb = tar.data.shape_keys.key_blocks.get(self.shape_name)
                if kb:
                    kb.driver_remove("value")
                    tar.shape_key_remove(kb)
                    
        # 2. Clean up the master driver mesh
        master = scene.ak_driver_mesh
        if master and master.data.shape_keys:
            kb = master.data.shape_keys.key_blocks.get(self.shape_name)
            if kb:
                master.shape_key_remove(kb)
                    
        autosort_shapes_logic(context)
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)

class AK_OT_add_single_arkit_shape(bpy.types.Operator):
    bl_idname = "ak.add_single_arkit_shape"
    bl_label = "Add Shapekey"
    bl_description = "Adds the selected shapekey to all the secondary meshes, if they dont have it yet."
    bl_options = {'REGISTER', 'UNDO'}

    shape_name: bpy.props.StringProperty()

    def execute(self, context):
        scene = context.scene
        targets = [t.obj for t in scene.ak_targets if t.obj]
            
        if not targets:
            self.report({'WARNING'}, "Assign Driver/Driven meshes first.")
            return {'CANCELLED'}

        for ob in targets:
            if ob.type != 'MESH': continue
            if not ob.data.shape_keys: ob.shape_key_add(name="Basis")
            
            kb = ob.data.shape_keys.key_blocks
            if self.shape_name not in kb: ob.shape_key_add(name=self.shape_name)
            kb[self.shape_name].value = 0.0

            t_kb = kb.get(self.shape_name)
            
            t_kb.driver_remove("value")
            drv = t_kb.driver_add("value").driver
            drv.type = 'SUM'
            var = drv.variables.new()
            var.name = "src_val"
            var.type = 'SINGLE_PROP'
            # SAFELY TARGET THE OBJECT TO AVOID CRASHES
            var.targets[0].id_type = 'OBJECT'
            var.targets[0].id = scene.ak_driver_mesh
            var.targets[0].data_path = f'data.shape_keys.key_blocks["{self.shape_name}"].value'

        autosort_shapes_logic(context)
        return {'FINISHED'}

# --------------------------------------------------
# VRM INTEGRATION OPERATORS
# --------------------------------------------------

class AK_OT_add_custom_shape(bpy.types.Operator):
    bl_idname = "ak.add_custom_shape"
    bl_label = "Add Custom Blendshape"
    bl_description = "Add a single custom blendshape by name to the active mesh."
    bl_options = {'REGISTER', 'UNDO'}

    shape_name: bpy.props.StringProperty(name="Shape Name", default="custom_expression")

    @classmethod
    def poll(cls, context):
        return context.active_object and context.active_object.type == 'MESH'

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        self.layout.prop(self, "shape_name")

    def execute(self, context):
        obj = context.active_object
        name = self.shape_name.strip()
        if not name:
            self.report({'ERROR'}, "Name cannot be empty.")
            return {'CANCELLED'}
        if not obj.data.shape_keys:
            obj.shape_key_add(name="Basis", from_mix=False)
        if obj.data.shape_keys.key_blocks.get(name):
            self.report({'WARNING'}, f"'{name}' already exists.")
            return {'CANCELLED'}
        obj.shape_key_add(name=name, from_mix=False)
        self.report({'INFO'}, f"Created '{name}'.")
        return {'FINISHED'}


class AK_OT_add_multiple_custom_shapes(bpy.types.Operator):
    bl_idname = "ak.add_multiple_custom_shapes"
    bl_label = "Add Multiple Blendshapes"
    bl_description = "Add multiple blendshapes to the active mesh (comma-separated names)."
    bl_options = {'REGISTER', 'UNDO'}

    shape_names: bpy.props.StringProperty(name="Shape Names", default="")

    @classmethod
    def poll(cls, context):
        return context.active_object and context.active_object.type == 'MESH'

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=400)

    def draw(self, context):
        layout = self.layout
        layout.label(text="Comma-separated names:")
        layout.prop(self, "shape_names", text="")

    def execute(self, context):
        obj = context.active_object
        names = [n.strip() for n in self.shape_names.split(',') if n.strip()]
        if not names:
            self.report({'ERROR'}, "No valid names provided.")
            return {'CANCELLED'}
        if not obj.data.shape_keys:
            obj.shape_key_add(name="Basis", from_mix=False)
        created, skipped = 0, 0
        for n in names:
            if obj.data.shape_keys.key_blocks.get(n):
                skipped += 1
            else:
                obj.shape_key_add(name=n, from_mix=False)
                created += 1
        self.report({'INFO'}, f"Created {created}, skipped {skipped}.")
        return {'FINISHED'}


class AK_OT_create_arkit_expression_slots(bpy.types.Operator):
    bl_idname = "ak.create_arkit_expression_slots"
    bl_label = "Create ARKit Expression Slots"
    bl_description = "Create all ARKit blendshapes as empty VRM 1.0 custom expression slots on the armature."
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        arm, _, _ = get_vrm_armature_and_extension()
        return arm is not None

    def execute(self, context):
        arm, _, vrm_ext = get_vrm_armature_and_extension()
        if not arm:
            self.report({'ERROR'}, "VRM armature not found.")
            return {'CANCELLED'}
        expressions = vrm_ext.vrm1.expressions
        created, skipped = 0, 0
        for name in (s for g in ARKIT_DEFAULTS.values() for s in g):
            if vrm_expression_exists(expressions, name):
                skipped += 1
                continue
            bpy.ops.vrm.add_vrm1_expressions_custom_expression(
                armature_name=arm.name, custom_expression_name=name)
            created += 1
        self.report({'INFO'}, f"Created {created} slots, skipped {skipped}.")
        return {'FINISHED'}


class AK_OT_add_arkit_to_vrm(bpy.types.Operator):
    bl_idname = "ak.add_arkit_to_vrm"
    bl_label = "Add ARKit to VRM Expressions"
    bl_description = "Add all ARKit blendshapes as VRM 1.0 custom expressions bound to the active mesh."
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        arm, _, _ = get_vrm_armature_and_extension()
        return arm is not None and any(o.type == 'MESH' and o.data.shape_keys for o in bpy.data.objects)

    def execute(self, context):
        arm, _, vrm_ext = get_vrm_armature_and_extension()
        if not arm:
            self.report({'ERROR'}, "VRM armature not found.")
            return {'CANCELLED'}
        mesh_obj = get_vrm_mesh(context)
        if not mesh_obj:
            self.report({'ERROR'}, "No mesh with shape keys found.")
            return {'CANCELLED'}
        expressions = vrm_ext.vrm1.expressions
        kb = mesh_obj.data.shape_keys.key_blocks
        created, skipped = 0, 0
        for name in (s for g in ARKIT_DEFAULTS.values() for s in g):
            if name not in kb or vrm_expression_exists(expressions, name):
                skipped += 1
                continue
            if add_vrm_expression_with_bind(arm.name, expressions, mesh_obj, name):
                created += 1
            else:
                skipped += 1
        self.report({'INFO'}, f"Created {created} VRM expressions, skipped {skipped}.")
        return {'FINISHED'}


class AK_OT_add_custom_to_vrm(bpy.types.Operator):
    bl_idname = "ak.add_custom_to_vrm"
    bl_label = "Add Custom Shape to VRM"
    bl_description = "Add a specific shape key from the active mesh as a VRM 1.0 custom expression."
    bl_options = {'REGISTER', 'UNDO'}

    shape_name: bpy.props.StringProperty(name="Shape Key", default="")

    @classmethod
    def poll(cls, context):
        arm, _, _ = get_vrm_armature_and_extension()
        obj = context.active_object
        return arm and obj and obj.type == 'MESH' and obj.data.shape_keys

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        obj = context.active_object
        if obj and obj.data.shape_keys:
            self.layout.prop_search(self, "shape_name", obj.data.shape_keys, "key_blocks", text="Shape Key")
        else:
            self.layout.prop(self, "shape_name")

    def execute(self, context):
        name = self.shape_name.strip()
        if not name:
            self.report({'ERROR'}, "Name cannot be empty.")
            return {'CANCELLED'}
        mesh_obj = context.active_object
        arm, _, vrm_ext = get_vrm_armature_and_extension()
        if not arm:
            self.report({'ERROR'}, "VRM armature not found.")
            return {'CANCELLED'}
        if name not in mesh_obj.data.shape_keys.key_blocks:
            self.report({'ERROR'}, f"Shape key '{name}' not found.")
            return {'CANCELLED'}
        expressions = vrm_ext.vrm1.expressions
        if vrm_expression_exists(expressions, name):
            self.report({'WARNING'}, f"VRM expression '{name}' already exists.")
            return {'CANCELLED'}
        try:
            add_vrm_expression_with_bind(arm.name, expressions, mesh_obj, name)
        except Exception:
            pass
        self.report({'INFO'}, f"Added '{name}' to VRM expressions.")
        return {'FINISHED'}


def _assign_shapes_to_vrm(self, arm, expressions, mesh_obj, shape_names):
    """Shared bind logic for both assign operators. Returns (assigned, skipped)."""
    kb = mesh_obj.data.shape_keys.key_blocks
    assigned, skipped = 0, 0
    for name in shape_names:
        if name not in kb:
            skipped += 1
            continue
        expr = next((e for e in expressions.custom if e.custom_name == name), None)
        if not expr or vrm_bind_exists(expr, mesh_obj, name):
            skipped += 1
            continue
        try:
            before = len(expr.morph_target_binds)
            bpy.ops.vrm.add_vrm1_expression_morph_target_bind(
                armature_name=arm.name, expression_name=name)
            if len(expr.morph_target_binds) > before:
                bind = expr.morph_target_binds[-1]
                bind.node.bpy_object = mesh_obj
                bind.index = name
                assigned += 1
            else:
                skipped += 1
        except Exception:
            skipped += 1
    return assigned, skipped


class AK_OT_assign_to_vrm_proxies(bpy.types.Operator):
    bl_idname = "ak.assign_to_vrm_proxies"
    bl_label = "Assign to VRM Proxies"
    bl_description = "Assign ARKit shape keys from the best available mesh to matching VRM custom expressions."
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        arm, arm_obj, _ = get_vrm_armature_and_extension()
        return arm and arm_obj and any(o.type == 'MESH' and o.data.shape_keys for o in bpy.data.objects)

    def execute(self, context):
        arm, _, vrm_ext = get_vrm_armature_and_extension()
        if not arm:
            self.report({'ERROR'}, "VRM armature not found.")
            return {'CANCELLED'}
        mesh_obj = get_vrm_mesh(context)
        if not mesh_obj:
            self.report({'ERROR'}, "No mesh with shape keys found.")
            return {'CANCELLED'}
        all_arkit = [s for g in ARKIT_DEFAULTS.values() for s in g]
        assigned, skipped = _assign_shapes_to_vrm(self, arm, vrm_ext.vrm1.expressions, mesh_obj, all_arkit)
        self.report({'INFO'}, f"Assigned {assigned} binds, skipped {skipped}.")
        return {'FINISHED'}


class AK_OT_assign_selected_to_vrm_proxies(bpy.types.Operator):
    bl_idname = "ak.assign_selected_to_vrm_proxies"
    bl_label = "Assign Active Mesh to VRM Proxies"
    bl_description = "Assign ARKit shape keys from the active mesh to matching VRM custom expressions."
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        arm, arm_obj, _ = get_vrm_armature_and_extension()
        obj = context.active_object
        return arm and arm_obj and obj and obj.type == 'MESH' and obj.data.shape_keys

    def execute(self, context):
        arm, _, vrm_ext = get_vrm_armature_and_extension()
        if not arm:
            self.report({'ERROR'}, "VRM armature not found.")
            return {'CANCELLED'}
        all_arkit = [s for g in ARKIT_DEFAULTS.values() for s in g]
        assigned, skipped = _assign_shapes_to_vrm(
            self, arm, vrm_ext.vrm1.expressions, context.active_object, all_arkit)
        self.report({'INFO'}, f"Assigned {assigned} from active mesh, skipped {skipped}.")
        return {'FINISHED'}


class AK_OT_clean_stale_vrm_binds(bpy.types.Operator):
    bl_idname = "ak.clean_stale_vrm_binds"
    bl_label = "Clean Stale VRM Binds"
    bl_description = "Remove morph target binds in VRM expressions that reference deleted mesh objects."
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        arm, _, _ = get_vrm_armature_and_extension()
        return arm is not None

    def execute(self, context):
        arm, _, vrm_ext = get_vrm_armature_and_extension()
        if not arm:
            self.report({'ERROR'}, "VRM armature not found.")
            return {'CANCELLED'}
        expressions = vrm_ext.vrm1.expressions
        existing = set(bpy.data.objects.keys())
        all_exprs = list(expressions.custom)
        for preset_name in [
            "happy","angry","sad","relaxed","surprised","neutral",
            "aa","ih","ou","ee","oh",
            "blink","blinkLeft","blinkRight",
            "lookUp","lookDown","lookLeft","lookRight",
        ]:
            p = getattr(expressions, preset_name, None)
            if p:
                all_exprs.append(p)
        removed = 0
        for expr in all_exprs:
            stale = [i for i, b in enumerate(expr.morph_target_binds)
                     if b.node.bpy_object is None or b.node.bpy_object.name not in existing]
            for i in reversed(stale):
                expr.morph_target_binds.remove(i)
                removed += 1
        self.report({'INFO'}, f"Removed {removed} stale binds.")
        return {'FINISHED'}


# --------------------------------------------------
# UI PANELS
# --------------------------------------------------

class AK_UL_targets(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if item.obj: layout.label(text=item.obj.name, icon='MESH_DATA')

class AK_PT_panel(bpy.types.Panel):
    bl_label = "ARKit Blendshape Helper"
    bl_idname = "AK_PT_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "ARKit H"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        master_obj = scene.ak_driver_mesh

        # 1. Mesh Setup
        m_box = layout.box()
        m_box.prop(scene, "ak_show_mesh_setup", icon='TRIA_DOWN' if scene.ak_show_mesh_setup else 'TRIA_RIGHT', text="Mesh Setup", emboss=False)
        if scene.ak_show_mesh_setup:
            meshCol = m_box.column(align=True)
            meshCol.prop(scene, "ak_driver_mesh", text="Driver")
            row = meshCol.row()
            row.template_list("AK_UL_targets", "", scene, "ak_targets", scene, "ak_target_index")
            col = row.column(align=True)
            col.operator("ak.target_add_selected", icon="ADD", text="")
            col.operator("ak.target_remove", icon="REMOVE", text="")
            
            row = meshCol.row(align=True)
            row.operator("ak.add_arkit_shapes", icon='SHAPEKEY_DATA', text="Add ARKit")
            row.operator("ak.add_vrm_shapes", icon='OUTLINER_OB_ARMATURE', text="Add VRM")
            row.operator("ak.delete_all_shapes", icon='ERROR', text="")
            row = meshCol.row(align=True)
            row.operator("ak.add_vrchat_shapes", icon='COMMUNITY', text="Add VRChat")
            row.operator("ak.add_mmd_shapes", icon='ANIM_DATA', text="Add MMD")

            # Conversion buttons — only shown when the source standard exists but the target doesn't
            if master_obj and master_obj.data.shape_keys:
                kb_names = {k.name for k in master_obj.data.shape_keys.key_blocks}
                has_arkit     = any(s in kb_names for g in ARKIT_DEFAULTS.values() for s in g)
                has_vrm_vis   = any(s in kb_names for s in VRM_DEFAULTS["Visemes"])
                has_vrm_blink = any(s in kb_names for s in VRM_DEFAULTS["Blink"])
                has_vrchat    = any(s in kb_names for g in VRCHAT_DEFAULTS.values() for s in g)
                has_vrc_vis   = any(s in kb_names for s in VRCHAT_DEFAULTS["VRC_Visemes"])
                has_mmd_vis   = any(s in kb_names for s in MMD_DEFAULTS["MMD_Visemes"])
                has_mmd_expr  = any(s in kb_names for s in MMD_DEFAULTS["MMD_Expressions"])

                show_arkit_to_vrc    = has_arkit     and not has_vrchat
                show_vrm_to_vrcvis   = has_vrm_vis   and not has_vrc_vis
                show_vrm_to_mmd      = has_vrm_vis   and not has_mmd_vis
                show_vrm_blink_to_mmd = has_vrm_blink and not has_mmd_expr

                if show_arkit_to_vrc or show_vrm_to_vrcvis or show_vrm_to_mmd or show_vrm_blink_to_mmd:
                    conv_box = m_box.box()
                    conv_box.label(text="Generate from existing shapes:", icon='FORWARD')
                    row = conv_box.row(align=True)
                    if show_arkit_to_vrc:
                        row.operator("ak.copy_arkit_to_vrchat", icon='COMMUNITY', text="VRC from ARKit")
                    if show_vrm_to_vrcvis:
                        row.operator("ak.copy_vrm_to_vrc_visemes", icon='COMMUNITY', text="VRC Visemes from VRM")
                    if show_vrm_to_mmd:
                        row.operator("ak.copy_vrm_to_mmd", icon='ANIM_DATA', text="MMD from VRM")
                    if show_vrm_blink_to_mmd:
                        row.operator("ak.copy_vrm_blink_to_mmd", icon='ANIM_DATA', text="MMD Eyes from VRM")

        # 2. General Global Controls
        row = layout.row(align=True)
        row.operator("ak.create_drivers", icon='CONSTRAINT', text="Driver Link")
        row.operator("ak.remove_drivers", icon='CANCEL', text="Driver Unlink")
        row = layout.row(align=True)
        row.operator("ak.select_all_meshes", icon='RESTRICT_SELECT_OFF', text="Select")
        row.operator("ak.select_basis", icon='SHAPEKEY_DATA', text="Basis")
        row.operator("ak.global_zero", icon='FILE_REFRESH', text="Zero All")
        
        if not master_obj or not master_obj.data.shape_keys:
            layout.label(text="Assign a Driver Mesh with shapes to see folders.", icon='INFO')
            return
        
        # 3. Blendshape Folders
        f_box = layout.box()
        header = f_box.row()
        header.prop(scene, "ak_show_folders_setup", icon='TRIA_DOWN' if scene.ak_show_folders_setup else 'TRIA_RIGHT', text="Blendshape Folders", emboss=False)
        
        tools = header.row(align=True)
        tools.operator("ak.autosort_shapes", icon='FILE_REFRESH', text="") 
        
        if scene.ak_show_folders_setup:
            for i, group in enumerate(scene.ak_groups):
                g_box = f_box.box()
                header = g_box.row(align=True)
                header.prop(group, "is_expanded", icon='TRIA_DOWN' if group.is_expanded else 'TRIA_RIGHT', text=group.name, emboss=False)
                
                if group.is_expanded:
                    col = g_box.column(align=True)
                    for s_n in group.shapes_csv.split(","):
                        if not s_n: continue
                        
                        # GRAB THE NATIVE KEYBLOCK DIRECTLY
                        kb = master_obj.data.shape_keys.key_blocks.get(s_n)
                        
                        if kb:
                            # Check if it's currently selected on the driver
                            is_active = (master_obj.active_shape_key_index == master_obj.data.shape_keys.key_blocks.find(s_n))
                            
                            row = col.row(align=True)
                            
                            if s_n.endswith("Left"):
                                row.separator(factor=1.6)
                                row.label(icon='EVENT_L')
                                fix_op = row.operator("ak.swap_lr_names", text="", icon='UV_SYNC_SELECT')
                                fix_op.shape_name = s_n
                            elif s_n.endswith("Right"):
                                row.separator(factor=1.6)
                                row.label(icon='EVENT_R')
                                fix_op = row.operator("ak.swap_lr_names", text="", icon='UV_SYNC_SELECT')
                                fix_op.shape_name = s_n
                            else:
                                split_op = row.operator("ak.mirror_blendshape", text="", icon='MOD_MIRROR')
                                split_op.shape_name = s_n
                                kb_all = master_obj.data.shape_keys.key_blocks
                                if (s_n + "Left") in kb_all and (s_n + "Right") in kb_all:
                                    swap_op = row.operator("ak.swap_lr_blendshape", text="", icon='ARROW_LEFTRIGHT')
                                    swap_op.shape_name = s_n
                                    merge_op = row.operator("ak.merge_lr_blendshape", text="", icon='AUTOMERGE_ON')
                                    merge_op.shape_name = s_n

                            # PASS THE KEYBLOCK DIRECTLY TO THE UI
                            row.prop(kb, "value", text=s_n)
                            
                            # ADD BUTTON
                            add_op = row.operator("ak.add_single_arkit_shape", text="", icon='ADD')
                            add_op.shape_name = s_n

                            # THE SELECT BUTTON
                            sel_icon = 'RESTRICT_SELECT_OFF' if is_active else 'RESTRICT_SELECT_ON'
                            sel_op = row.operator("ak.select_shape_key", text="", icon=sel_icon)
                            sel_op.shape_name = s_n
                            
                            # THE DELETE BUTTON
                            del_op = row.operator("ak.delete_single_shape", text="", icon='X')
                            del_op.shape_name = s_n
                
class AK_PT_vrm_panel(bpy.types.Panel):
    bl_label = "VRM Tools"
    bl_idname = "AK_PT_vrm_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "ARKit H"

    def draw(self, context):
        layout = self.layout
        arm, _, _ = get_vrm_armature_and_extension()
        vrm_ok = arm is not None

        # Custom blendshapes
        box = layout.box()
        box.label(text="Custom Blendshapes", icon='EDITMODE_HLT')
        row = box.row(align=True)
        row.operator("ak.add_custom_shape", icon='SOLO_ON', text="Add One")
        row.operator("ak.add_multiple_custom_shapes", icon='PRESET_NEW', text="Add Multiple")

        # VRM Expression setup
        box = layout.box()
        box.label(text="VRM Expression Setup", icon='ARMATURE_DATA')
        if not vrm_ok:
            box.label(text="No VRM armature found", icon='ERROR')
        box.operator("ak.create_arkit_expression_slots", icon='ARMATURE_DATA')
        box.operator("ak.add_arkit_to_vrm", icon='EXPORT')
        box.operator("ak.add_custom_to_vrm", icon='PLUS')

        # Assignment
        box = layout.box()
        box.label(text="Assign to VRM Proxies", icon='LINKED')
        box.operator("ak.assign_to_vrm_proxies", icon='CONSTRAINT')
        box.operator("ak.assign_selected_to_vrm_proxies", icon='MESH_DATA')

        # Utilities
        box = layout.box()
        box.label(text="Utilities", icon='TOOL_SETTINGS')
        box.operator("ak.clean_stale_vrm_binds", icon='TRASH')


# --------------------------------------------------
# REGISTER
# --------------------------------------------------

classes = [
    AK_GroupItem, AK_Target, AK_UL_targets, AK_PT_panel, AK_PT_vrm_panel,
    AK_OT_add_arkit_shapes, AK_OT_add_vrm_shapes, AK_OT_add_vrchat_shapes, AK_OT_add_mmd_shapes,
    AK_OT_copy_arkit_to_vrchat, AK_OT_copy_vrm_to_vrc_visemes, AK_OT_copy_vrm_to_mmd, AK_OT_copy_vrm_blink_to_mmd,
    AK_OT_create_drivers, AK_OT_remove_drivers,
    AK_OT_select_basis, AK_OT_global_zero, AK_OT_delete_all_shapes,
    AK_OT_target_add_selected, AK_OT_target_remove,
    AK_OT_groups_toggle, AK_OT_mirror_blendshape, AK_OT_swap_lr_blendshape, AK_OT_swap_lr_names, AK_OT_merge_lr_blendshape,
    AK_OT_select_all_meshes, AK_OT_autosort_shapes, AK_OT_delete_single_shape,
    AK_OT_select_shape_key, AK_OT_add_single_arkit_shape,
    AK_OT_add_custom_shape, AK_OT_add_multiple_custom_shapes,
    AK_OT_create_arkit_expression_slots, AK_OT_add_arkit_to_vrm, AK_OT_add_custom_to_vrm,
    AK_OT_assign_to_vrm_proxies, AK_OT_assign_selected_to_vrm_proxies,
    AK_OT_clean_stale_vrm_binds,
    ]

def register():
    for c in classes: 
        bpy.utils.register_class(c)
    
    
    s = bpy.types.Scene
    s.ak_targets = bpy.props.CollectionProperty(type=AK_Target)
    s.ak_target_index = bpy.props.IntProperty()
    s.ak_groups = bpy.props.CollectionProperty(type=AK_GroupItem)
    s.ak_driver_mesh = bpy.props.PointerProperty(type=bpy.types.Object, name="Driver")
    s.ak_show_mesh_setup = bpy.props.BoolProperty(default=True)
    s.ak_show_folders_setup = bpy.props.BoolProperty(default=True)
    

def unregister():
    s = bpy.types.Scene
    del s.ak_targets
    del s.ak_target_index
    del s.ak_groups
    del s.ak_driver_mesh
    del s.ak_show_mesh_setup
    del s.ak_show_folders_setup

    for c in classes: 
        bpy.utils.unregister_class(c)
    
if __name__ == "__main__":
    register()

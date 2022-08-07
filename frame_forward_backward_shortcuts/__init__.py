
import bpy

# Version History
# 1.0.0 - 2020-06-25: Original version

bl_info = {
    "name": "Frame Forward Backward Shortcuts",
    "author": "Jeff Boller",
    "version": (1, 0, 0),
    "blender": (2, 93, 0),
    "location": "",
    "description": "This add-on provides the ability to set up keyboard shortcuts to jump forward or backward a specific number of frames. " \
                   "To run this, make a Blender keyboard shortcut and put one of these for the action: " \
                    " wm.frame_forward_backward_shortcuts_plus_1 " \
                    " wm.frame_forward_backward_shortcuts_plus_2 " \
                    " wm.frame_forward_backward_shortcuts_plus_3 " \
                    " wm.frame_forward_backward_shortcuts_plus_4 " \
                    " wm.frame_forward_backward_shortcuts_plus_5 " \
                    " wm.frame_forward_backward_shortcuts_plus_6 " \
                    " wm.frame_forward_backward_shortcuts_plus_7 " \
                    " wm.frame_forward_backward_shortcuts_plus_8 " \
                    " wm.frame_forward_backward_shortcuts_plus_12 " \
                    " wm.frame_forward_backward_shortcuts_plus_24 " \
                    " wm.frame_forward_backward_shortcuts_minus_1 " \
                    " wm.frame_forward_backward_shortcuts_minus_2 " \
                    " wm.frame_forward_backward_shortcuts_minus_3 " \
                    " wm.frame_forward_backward_shortcuts_minus_4 " \
                    " wm.frame_forward_backward_shortcuts_minus_5 " \
                    " wm.frame_forward_backward_shortcuts_minus_6 " \
                    " wm.frame_forward_backward_shortcuts_minus_7 " \
                    " wm.frame_forward_backward_shortcuts_minus_8 " \
                    " wm.frame_forward_backward_shortcuts_minus_12 " \
                    " wm.frame_forward_backward_shortcuts_minus_24 " \
                    "To call this add-on manually from Python, use these commands: " \
                    " bpy.ops.wm.frame_forward_backward_shortcuts_plus_1() " \
                    " bpy.ops.wm.frame_forward_backward_shortcuts_plus_2() " \
                    " bpy.ops.wm.frame_forward_backward_shortcuts_plus_3() " \
                    " bpy.ops.wm.frame_forward_backward_shortcuts_plus_4() " \
                    " bpy.ops.wm.frame_forward_backward_shortcuts_plus_5() " \
                    " bpy.ops.wm.frame_forward_backward_shortcuts_plus_6() " \
                    " bpy.ops.wm.frame_forward_backward_shortcuts_plus_7() " \
                    " bpy.ops.wm.frame_forward_backward_shortcuts_plus_8() " \
                    " bpy.ops.wm.frame_forward_backward_shortcuts_plus_12() " \
                    " bpy.ops.wm.frame_forward_backward_shortcuts_plus_24() " \
                    " bpy.ops.wm.frame_forward_backward_shortcuts_minus_1() " \
                    " bpy.ops.wm.frame_forward_backward_shortcuts_minus_2() " \
                    " bpy.ops.wm.frame_forward_backward_shortcuts_minus_3() " \
                    " bpy.ops.wm.frame_forward_backward_shortcuts_minus_4() " \
                    " bpy.ops.wm.frame_forward_backward_shortcuts_minus_5() " \
                    " bpy.ops.wm.frame_forward_backward_shortcuts_minus_6() " \
                    " bpy.ops.wm.frame_forward_backward_shortcuts_minus_7() " \
                    " bpy.ops.wm.frame_forward_backward_shortcuts_minus_8() " \
                    " bpy.ops.wm.frame_forward_backward_shortcuts_minus_12() " \
                    " bpy.ops.wm.frame_forward_backward_shortcuts_minus_24() ",
    "wiki_url": "https://github.com/sundriftproductions/blenderaddon-frame-forward-backward-shortcuts/wiki",
    "tracker_url": "https://github.com/sundriftproductions/blenderaddon-frame-forward-backward-shortcuts",
    "category": "System"}

class WM_OT_frame_forward_backward_shortcuts_plus_1(bpy.types.Operator):
    bl_idname = 'wm.frame_forward_backward_shortcuts_plus_1'
    bl_label = 'Frame Forward Backward Shortcuts'
    bl_description = 'Call bpy.ops.wm.frame_forward_backward_shortcuts_plus_1()'
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.context.scene.frame_current += 1
        self.report({'INFO'}, 'Moved +1 frame: ' + str(bpy.context.scene.frame_current))
        return {'FINISHED'}

class WM_OT_frame_forward_backward_shortcuts_plus_2(bpy.types.Operator):
    bl_idname = 'wm.frame_forward_backward_shortcuts_plus_2'
    bl_label = 'Frame Forward Backward Shortcuts'
    bl_description = 'Call bpy.ops.wm.frame_forward_backward_shortcuts_plus_2()'
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.context.scene.frame_current += 2
        self.report({'INFO'}, 'Moved +2 frames: ' + str(bpy.context.scene.frame_current))
        return {'FINISHED'}

class WM_OT_frame_forward_backward_shortcuts_plus_3(bpy.types.Operator):
    bl_idname = 'wm.frame_forward_backward_shortcuts_plus_3'
    bl_label = 'Frame Forward Backward Shortcuts'
    bl_description = 'Call bpy.ops.wm.frame_forward_backward_shortcuts_plus_3()'
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.context.scene.frame_current += 3
        self.report({'INFO'}, 'Moved +3 frames: ' + str(bpy.context.scene.frame_current))
        return {'FINISHED'}

class WM_OT_frame_forward_backward_shortcuts_plus_4(bpy.types.Operator):
    bl_idname = 'wm.frame_forward_backward_shortcuts_plus_4'
    bl_label = 'Frame Forward Backward Shortcuts'
    bl_description = 'Call bpy.ops.wm.frame_forward_backward_shortcuts_plus_4()'
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.context.scene.frame_current += 4
        self.report({'INFO'}, 'Moved +4 frames: ' + str(bpy.context.scene.frame_current))
        return {'FINISHED'}

class WM_OT_frame_forward_backward_shortcuts_plus_5(bpy.types.Operator):
    bl_idname = 'wm.frame_forward_backward_shortcuts_plus_5'
    bl_label = 'Frame Forward Backward Shortcuts'
    bl_description = 'Call bpy.ops.wm.frame_forward_backward_shortcuts_plus_5()'
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.context.scene.frame_current += 5
        self.report({'INFO'}, 'Moved +5 frames: ' + str(bpy.context.scene.frame_current))
        return {'FINISHED'}

class WM_OT_frame_forward_backward_shortcuts_plus_6(bpy.types.Operator):
    bl_idname = 'wm.frame_forward_backward_shortcuts_plus_6'
    bl_label = 'Frame Forward Backward Shortcuts'
    bl_description = 'Call bpy.ops.wm.frame_forward_backward_shortcuts_plus_6()'
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.context.scene.frame_current += 6
        self.report({'INFO'}, 'Moved +6 frames: ' + str(bpy.context.scene.frame_current))
        return {'FINISHED'}

class WM_OT_frame_forward_backward_shortcuts_plus_7(bpy.types.Operator):
    bl_idname = 'wm.frame_forward_backward_shortcuts_plus_7'
    bl_label = 'Frame Forward Backward Shortcuts'
    bl_description = 'Call bpy.ops.wm.frame_forward_backward_shortcuts_plus_7()'
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.context.scene.frame_current += 7
        self.report({'INFO'}, 'Moved +7 frames: ' + str(bpy.context.scene.frame_current))
        return {'FINISHED'}

class WM_OT_frame_forward_backward_shortcuts_plus_8(bpy.types.Operator):
    bl_idname = 'wm.frame_forward_backward_shortcuts_plus_8'
    bl_label = 'Frame Forward Backward Shortcuts'
    bl_description = 'Call bpy.ops.wm.frame_forward_backward_shortcuts_plus_8()'
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.context.scene.frame_current += 8
        self.report({'INFO'}, 'Moved +8 frames: ' + str(bpy.context.scene.frame_current))
        return {'FINISHED'}

class WM_OT_frame_forward_backward_shortcuts_plus_12(bpy.types.Operator):
    bl_idname = 'wm.frame_forward_backward_shortcuts_plus_12'
    bl_label = 'Frame Forward Backward Shortcuts'
    bl_description = 'Call bpy.ops.wm.frame_forward_backward_shortcuts_plus_12()'
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.context.scene.frame_current += 12
        self.report({'INFO'}, 'Moved +12 frames: ' + str(bpy.context.scene.frame_current))
        return {'FINISHED'}

class WM_OT_frame_forward_backward_shortcuts_plus_24(bpy.types.Operator):
    bl_idname = 'wm.frame_forward_backward_shortcuts_plus_24'
    bl_label = 'Frame Forward Backward Shortcuts'
    bl_description = 'Call bpy.ops.wm.frame_forward_backward_shortcuts_plus_24()'
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.context.scene.frame_current += 24
        self.report({'INFO'}, 'Moved +24 frames: ' + str(bpy.context.scene.frame_current))
        return {'FINISHED'}

class WM_OT_frame_forward_backward_shortcuts_minus_1(bpy.types.Operator):
    bl_idname = 'wm.frame_forward_backward_shortcuts_minus_1'
    bl_label = 'Frame Forward Backward Shortcuts'
    bl_description = 'Call bpy.ops.wm.frame_forward_backward_shortcuts_minus_1()'
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.context.scene.frame_current -= 1
        self.report({'INFO'}, 'Moved -1 frame: ' + str(bpy.context.scene.frame_current))
        return {'FINISHED'}

class WM_OT_frame_forward_backward_shortcuts_minus_2(bpy.types.Operator):
    bl_idname = 'wm.frame_forward_backward_shortcuts_minus_2'
    bl_label = 'Frame Forward Backward Shortcuts'
    bl_description = 'Call bpy.ops.wm.frame_forward_backward_shortcuts_minus_2()'
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.context.scene.frame_current -= 2
        self.report({'INFO'}, 'Moved -2 frames: ' + str(bpy.context.scene.frame_current))
        return {'FINISHED'}

class WM_OT_frame_forward_backward_shortcuts_minus_3(bpy.types.Operator):
    bl_idname = 'wm.frame_forward_backward_shortcuts_minus_3'
    bl_label = 'Frame Forward Backward Shortcuts'
    bl_description = 'Call bpy.ops.wm.frame_forward_backward_shortcuts_minus_3()'
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.context.scene.frame_current -= 3
        self.report({'INFO'}, 'Moved -3 frames: ' + str(bpy.context.scene.frame_current))
        return {'FINISHED'}

class WM_OT_frame_forward_backward_shortcuts_minus_4(bpy.types.Operator):
    bl_idname = 'wm.frame_forward_backward_shortcuts_minus_4'
    bl_label = 'Frame Forward Backward Shortcuts'
    bl_description = 'Call bpy.ops.wm.frame_forward_backward_shortcuts_minus_4()'
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.context.scene.frame_current -= 4
        self.report({'INFO'}, 'Moved -4 frames: ' + str(bpy.context.scene.frame_current))
        return {'FINISHED'}

class WM_OT_frame_forward_backward_shortcuts_minus_5(bpy.types.Operator):
    bl_idname = 'wm.frame_forward_backward_shortcuts_minus_5'
    bl_label = 'Frame Forward Backward Shortcuts'
    bl_description = 'Call bpy.ops.wm.frame_forward_backward_shortcuts_minus_5()'
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.context.scene.frame_current -= 5
        self.report({'INFO'}, 'Moved -5 frames: ' + str(bpy.context.scene.frame_current))
        return {'FINISHED'}

class WM_OT_frame_forward_backward_shortcuts_minus_6(bpy.types.Operator):
    bl_idname = 'wm.frame_forward_backward_shortcuts_minus_6'
    bl_label = 'Frame Forward Backward Shortcuts'
    bl_description = 'Call bpy.ops.wm.frame_forward_backward_shortcuts_minus_6()'
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.context.scene.frame_current -= 6
        self.report({'INFO'}, 'Moved -6 frames: ' + str(bpy.context.scene.frame_current))
        return {'FINISHED'}

class WM_OT_frame_forward_backward_shortcuts_minus_7(bpy.types.Operator):
    bl_idname = 'wm.frame_forward_backward_shortcuts_minus_7'
    bl_label = 'Frame Forward Backward Shortcuts'
    bl_description = 'Call bpy.ops.wm.frame_forward_backward_shortcuts_minus_7()'
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.context.scene.frame_current -= 7
        self.report({'INFO'}, 'Moved -7 frames: ' + str(bpy.context.scene.frame_current))
        return {'FINISHED'}

class WM_OT_frame_forward_backward_shortcuts_minus_8(bpy.types.Operator):
    bl_idname = 'wm.frame_forward_backward_shortcuts_minus_8'
    bl_label = 'Frame Forward Backward Shortcuts'
    bl_description = 'Call bpy.ops.wm.frame_forward_backward_shortcuts_minus_8()'
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.context.scene.frame_current -= 8
        self.report({'INFO'}, 'Moved -8 frames: ' + str(bpy.context.scene.frame_current))
        return {'FINISHED'}

class WM_OT_frame_forward_backward_shortcuts_minus_12(bpy.types.Operator):
    bl_idname = 'wm.frame_forward_backward_shortcuts_minus_12'
    bl_label = 'Frame Forward Backward Shortcuts'
    bl_description = 'Call bpy.ops.wm.frame_forward_backward_shortcuts_minus_12()'
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.context.scene.frame_current -= 12
        self.report({'INFO'}, 'Moved -12 frames: ' + str(bpy.context.scene.frame_current))
        return {'FINISHED'}

class WM_OT_frame_forward_backward_shortcuts_minus_24(bpy.types.Operator):
    bl_idname = 'wm.frame_forward_backward_shortcuts_minus_24'
    bl_label = 'Frame Forward Backward Shortcuts'
    bl_description = 'Call bpy.ops.wm.frame_forward_backward_shortcuts_minus_24()'
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.context.scene.frame_current -= 24
        self.report({'INFO'}, 'Moved -24 frames: ' + str(bpy.context.scene.frame_current))
        return {'FINISHED'}

def register():
    bpy.utils.register_class(WM_OT_frame_forward_backward_shortcuts_plus_1)
    bpy.utils.register_class(WM_OT_frame_forward_backward_shortcuts_plus_2)
    bpy.utils.register_class(WM_OT_frame_forward_backward_shortcuts_plus_3)
    bpy.utils.register_class(WM_OT_frame_forward_backward_shortcuts_plus_4)
    bpy.utils.register_class(WM_OT_frame_forward_backward_shortcuts_plus_5)
    bpy.utils.register_class(WM_OT_frame_forward_backward_shortcuts_plus_6)
    bpy.utils.register_class(WM_OT_frame_forward_backward_shortcuts_plus_7)
    bpy.utils.register_class(WM_OT_frame_forward_backward_shortcuts_plus_8)
    bpy.utils.register_class(WM_OT_frame_forward_backward_shortcuts_plus_12)
    bpy.utils.register_class(WM_OT_frame_forward_backward_shortcuts_plus_24)
    bpy.utils.register_class(WM_OT_frame_forward_backward_shortcuts_minus_1)
    bpy.utils.register_class(WM_OT_frame_forward_backward_shortcuts_minus_2)
    bpy.utils.register_class(WM_OT_frame_forward_backward_shortcuts_minus_3)
    bpy.utils.register_class(WM_OT_frame_forward_backward_shortcuts_minus_4)
    bpy.utils.register_class(WM_OT_frame_forward_backward_shortcuts_minus_5)
    bpy.utils.register_class(WM_OT_frame_forward_backward_shortcuts_minus_6)
    bpy.utils.register_class(WM_OT_frame_forward_backward_shortcuts_minus_7)
    bpy.utils.register_class(WM_OT_frame_forward_backward_shortcuts_minus_8)
    bpy.utils.register_class(WM_OT_frame_forward_backward_shortcuts_minus_12)
    bpy.utils.register_class(WM_OT_frame_forward_backward_shortcuts_minus_24)

def unregister():
    bpy.utils.unregister_class(WM_OT_frame_forward_backward_shortcuts_minus_24)
    bpy.utils.unregister_class(WM_OT_frame_forward_backward_shortcuts_minus_12)
    bpy.utils.unregister_class(WM_OT_frame_forward_backward_shortcuts_minus_8)
    bpy.utils.unregister_class(WM_OT_frame_forward_backward_shortcuts_minus_7)
    bpy.utils.unregister_class(WM_OT_frame_forward_backward_shortcuts_minus_6)
    bpy.utils.unregister_class(WM_OT_frame_forward_backward_shortcuts_minus_5)
    bpy.utils.unregister_class(WM_OT_frame_forward_backward_shortcuts_minus_4)
    bpy.utils.unregister_class(WM_OT_frame_forward_backward_shortcuts_minus_3)
    bpy.utils.unregister_class(WM_OT_frame_forward_backward_shortcuts_minus_2)
    bpy.utils.unregister_class(WM_OT_frame_forward_backward_shortcuts_minus_1)
    bpy.utils.unregister_class(WM_OT_frame_forward_backward_shortcuts_plus_24)
    bpy.utils.unregister_class(WM_OT_frame_forward_backward_shortcuts_plus_12)
    bpy.utils.unregister_class(WM_OT_frame_forward_backward_shortcuts_plus_8)
    bpy.utils.unregister_class(WM_OT_frame_forward_backward_shortcuts_plus_7)
    bpy.utils.unregister_class(WM_OT_frame_forward_backward_shortcuts_plus_6)
    bpy.utils.unregister_class(WM_OT_frame_forward_backward_shortcuts_plus_5)
    bpy.utils.unregister_class(WM_OT_frame_forward_backward_shortcuts_plus_4)
    bpy.utils.unregister_class(WM_OT_frame_forward_backward_shortcuts_plus_3)
    bpy.utils.unregister_class(WM_OT_frame_forward_backward_shortcuts_plus_2)
    bpy.utils.unregister_class(WM_OT_frame_forward_backward_shortcuts_plus_1)

if __name__ == "__main__":
    register()

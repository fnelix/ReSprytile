import platform
import bpy

# Defines system architechture
def detect_system():
    system_info = {
        'is_apple_silicon': False,
        'is_windows_32bit': False,
        'is_windows_64bit': False
    }
    OSTypes = {'windowspe','windows'}    
    machine = platform.machine()
    architecture, OSName = platform.architecture()

    if machine == 'arm64':
        system_info['is_apple_silicon'] = True
    elif architecture == '32bit' and OSName.lower() in OSTypes:
        system_info['is_windows_32bit'] = True
    elif architecture == '64bit' and OSName.lower() in OSTypes:
        system_info['is_windows_64bit'] = True
    
    return system_info

system_info = detect_system()

if system_info['is_apple_silicon']:
    #could do something different here
    pass
else:
    #could do something different here
    #print("Unknown system architecture.")
    pass

#
import spryTile_OS_EverythingElse
classes = (spryTile_OS_EverythingElse)

classe = classes
def register():
    for c in classe.classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classe.classes:
        bpy.utils.unregister_class(c)


if __name__ == '__main__':
    register()

# WizIO 2021 Georgi Angelov
#   http://www.wizio.eu/
#   https://github.com/Wiz-IO/wizio-pico

from __future__ import print_function
from os.path import join
from SCons.Script import (AlwaysBuild, Builder, COMMAND_LINE_TARGETS, Default, DefaultEnvironment)
from colorama import Fore
from wpioasm import dev_pioasm # https://github.com/Wiz-IO/wizio-pico/issues/98#issuecomment-1128747885

env = DefaultEnvironment()
print( '<<<<<<<<<<<< ' + env.BoardConfig().get("name").upper() + " 2021 Georgi Angelov >>>>>>>>>>>>" )

dev_pioasm(env)

elf = env.BuildProgram()
src = env.ElfToBin( join("$BUILD_DIR", "${PROGNAME}"), elf )
prg = env.Alias( "buildprog", src, [ env.VerboseAction("", "DONE") ] )
AlwaysBuild( prg )

def generate_uf2(target, source, env):
    elf_file = target[0].get_path()
    env.Execute(
        " ".join(
            [
                "elf2uf2",
                '"%s"' % elf_file,
                '"%s"' % elf_file.replace(".elf", ".uf2"),
            ]
        )
    )

env.AddPostAction(
    elf, env.VerboseAction(generate_uf2, "Generating UF2 image")
)

upload = env.Alias("upload", prg, [ 
    env.VerboseAction("$UPLOADCMD", "Uploading..."),
    env.VerboseAction("", ""),
])
AlwaysBuild( upload )    

debug_tool = env.GetProjectOption("debug_tool")
if None == debug_tool:
    Default( prg )
else:   
    if 'cmsis-dap' in debug_tool:
        Default( upload )
    else:
        Default( prg )


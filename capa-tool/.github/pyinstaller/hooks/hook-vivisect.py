# Copyright (C) 2020 Mandiant, Inc. All Rights Reserved.

from PyInstaller.utils.hooks import copy_metadata

# in order for viv-utils to use pkg_resources to fetch
# the installed version of vivisect,
# we need to instruct pyinstaller to embed this metadata.
#
# so we set the pyinstaller.spec/hookspath to reference
#  the directory with this hook.
#
# this hook runs at analysis time and updates the embedded metadata.
#
# ref: https://github.com/pyinstaller/pyinstaller/issues/1713#issuecomment-162682084
datas = copy_metadata("vivisect")

excludedimports = [
    # viv gui requires these heavy libraries,
    # but viv as a library doesn't.
    # they shouldn't be installed in our configuration,
    # but we'll ensure they don't slip in here (such as on developers' systems).
    "PyQt5",
    "qt5",
    "pyqtwebengine",
    # the above are imported by these viv modules.
    # so really, we'd want to exclude these submodules of viv.
    # but i don't think this works.
    "vqt",
    "vdb.qt",
    "envi.qt",
    # unused by capa
    "pyasn1",
]

hiddenimports = [
    # vivisect does manual/runtime importing of its modules,
    # so declare the things that could be imported here.
    "vivisect",
    "vivisect.analysis",
    "vivisect.analysis.amd64",
    "vivisect.analysis.amd64.emulation",
    "vivisect.analysis.amd64.golang",
    "vivisect.analysis.crypto",
    "vivisect.analysis.crypto.constants",
    "vivisect.analysis.elf",
    "vivisect.analysis.elf.elfplt",
    "vivisect.analysis.elf.elfplt_late",
    "vivisect.analysis.elf.libc_start_main",
    "vivisect.analysis.generic",
    "vivisect.analysis.generic.codeblocks",
    "vivisect.analysis.generic.emucode",
    "vivisect.analysis.generic.entrypoints",
    "vivisect.analysis.generic.funcentries",
    "vivisect.analysis.generic.impapi",
    "vivisect.analysis.generic.linker",
    "vivisect.analysis.generic.mkpointers",
    "vivisect.analysis.generic.noret",
    "vivisect.analysis.generic.pointers",
    "vivisect.analysis.generic.pointertables",
    "vivisect.analysis.generic.relocations",
    "vivisect.analysis.generic.strconst",
    "vivisect.analysis.generic.switchcase",
    "vivisect.analysis.generic.symswitchcase",
    "vivisect.analysis.generic.thunks",
    "vivisect.analysis.i386",
    "vivisect.analysis.i386.calling",
    "vivisect.analysis.i386.golang",
    "vivisect.analysis.i386.importcalls",
    "vivisect.analysis.i386.instrhook",
    "vivisect.analysis.i386.thunk_reg",
    "vivisect.analysis.ms",
    "vivisect.analysis.ms.hotpatch",
    "vivisect.analysis.ms.localhints",
    "vivisect.analysis.ms.msvc",
    "vivisect.analysis.ms.msvcfunc",
    "vivisect.analysis.ms.vftables",
    "vivisect.analysis.pe",
    "vivisect.impapi.posix.amd64",
    "vivisect.impapi.posix.i386",
    "vivisect.impapi.windows",
    "vivisect.impapi.windows.advapi_32",
    "vivisect.impapi.windows.advapi_64",
    "vivisect.impapi.windows.amd64",
    "vivisect.impapi.windows.gdi_32",
    "vivisect.impapi.windows.gdi_64",
    "vivisect.impapi.windows.i386",
    "vivisect.impapi.windows.kernel_32",
    "vivisect.impapi.windows.kernel_64",
    "vivisect.impapi.windows.msvcr100_32",
    "vivisect.impapi.windows.msvcr100_64",
    "vivisect.impapi.windows.msvcr110_32",
    "vivisect.impapi.windows.msvcr110_64",
    "vivisect.impapi.windows.msvcr120_32",
    "vivisect.impapi.windows.msvcr120_64",
    "vivisect.impapi.windows.msvcr71_32",
    "vivisect.impapi.windows.msvcr80_32",
    "vivisect.impapi.windows.msvcr80_64",
    "vivisect.impapi.windows.msvcr90_32",
    "vivisect.impapi.windows.msvcr90_64",
    "vivisect.impapi.windows.msvcrt_32",
    "vivisect.impapi.windows.msvcrt_64",
    "vivisect.impapi.windows.ntdll_32",
    "vivisect.impapi.windows.ntdll_64",
    "vivisect.impapi.windows.ole_32",
    "vivisect.impapi.windows.ole_64",
    "vivisect.impapi.windows.rpcrt4_32",
    "vivisect.impapi.windows.rpcrt4_64",
    "vivisect.impapi.windows.shell_32",
    "vivisect.impapi.windows.shell_64",
    "vivisect.impapi.windows.user_32",
    "vivisect.impapi.windows.user_64",
    "vivisect.impapi.windows.ws2plus_32",
    "vivisect.impapi.windows.ws2plus_64",
    "vivisect.impapi.winkern",
    "vivisect.impapi.winkern.i386",
    "vivisect.impapi.winkern.amd64",
    "vivisect.parsers.blob",
    "vivisect.parsers.elf",
    "vivisect.parsers.ihex",
    "vivisect.parsers.macho",
    "vivisect.parsers.pe",
    "vivisect.storage",
    "vivisect.storage.basicfile",
    "vstruct.constants",
    "vstruct.constants.ntstatus",
    "vstruct.defs",
    "vstruct.defs.arm7",
    "vstruct.defs.bmp",
    "vstruct.defs.dns",
    "vstruct.defs.elf",
    "vstruct.defs.gif",
    "vstruct.defs.ihex",
    "vstruct.defs.inet",
    "vstruct.defs.java",
    "vstruct.defs.kdcom",
    "vstruct.defs.macho",
    "vstruct.defs.macho.const",
    "vstruct.defs.macho.fat",
    "vstruct.defs.macho.loader",
    "vstruct.defs.macho.stabs",
    "vstruct.defs.minidump",
    "vstruct.defs.pcap",
    "vstruct.defs.pe",
    "vstruct.defs.pptp",
    "vstruct.defs.rar",
    "vstruct.defs.swf",
    "vstruct.defs.win32",
    "vstruct.defs.windows",
    "vstruct.defs.windows.win_5_1_i386",
    "vstruct.defs.windows.win_5_1_i386.ntdll",
    "vstruct.defs.windows.win_5_1_i386.ntoskrnl",
    "vstruct.defs.windows.win_5_1_i386.win32k",
    "vstruct.defs.windows.win_5_2_i386",
    "vstruct.defs.windows.win_5_2_i386.ntdll",
    "vstruct.defs.windows.win_5_2_i386.ntoskrnl",
    "vstruct.defs.windows.win_5_2_i386.win32k",
    "vstruct.defs.windows.win_6_1_amd64",
    "vstruct.defs.windows.win_6_1_amd64.ntdll",
    "vstruct.defs.windows.win_6_1_amd64.ntoskrnl",
    "vstruct.defs.windows.win_6_1_amd64.win32k",
    "vstruct.defs.windows.win_6_1_i386",
    "vstruct.defs.windows.win_6_1_i386.ntdll",
    "vstruct.defs.windows.win_6_1_i386.ntoskrnl",
    "vstruct.defs.windows.win_6_1_i386.win32k",
    "vstruct.defs.windows.win_6_1_wow64",
    "vstruct.defs.windows.win_6_1_wow64.ntdll",
    "vstruct.defs.windows.win_6_2_amd64",
    "vstruct.defs.windows.win_6_2_amd64.ntdll",
    "vstruct.defs.windows.win_6_2_amd64.ntoskrnl",
    "vstruct.defs.windows.win_6_2_amd64.win32k",
    "vstruct.defs.windows.win_6_2_i386",
    "vstruct.defs.windows.win_6_2_i386.ntdll",
    "vstruct.defs.windows.win_6_2_i386.ntoskrnl",
    "vstruct.defs.windows.win_6_2_i386.win32k",
    "vstruct.defs.windows.win_6_2_wow64",
    "vstruct.defs.windows.win_6_2_wow64.ntdll",
    "vstruct.defs.windows.win_6_3_amd64",
    "vstruct.defs.windows.win_6_3_amd64.ntdll",
    "vstruct.defs.windows.win_6_3_amd64.ntoskrnl",
    "vstruct.defs.windows.win_6_3_i386",
    "vstruct.defs.windows.win_6_3_i386.ntdll",
    "vstruct.defs.windows.win_6_3_i386.ntoskrnl",
    "vstruct.defs.windows.win_6_3_wow64",
    "vstruct.defs.windows.win_6_3_wow64.ntdll",
]
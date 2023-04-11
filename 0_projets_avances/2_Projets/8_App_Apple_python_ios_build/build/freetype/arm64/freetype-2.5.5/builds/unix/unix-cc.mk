#
# FreeType 2 template for Unix-specific compiler definitions
#

# Copyright 1996-2000, 2002, 2003, 2005, 2006 by
# David Turner, Robert Wilhelm, and Werner Lemberg.
#
# This file is part of the FreeType project, and may only be used, modified,
# and distributed under the terms of the FreeType project license,
# LICENSE.TXT.  By continuing to use, modify, or distribute this file you
# indicate that you have read the license and understand and accept it
# fully.


CC           := /var/folders/hd/vkm9tzmx2233jds9nsvllf980000gp/T/tmpauxiujmm
COMPILER_SEP := $(SEP)
FT_LIBTOOL_DIR ?= $(BUILD_DIR)

LIBTOOL := $(FT_LIBTOOL_DIR)/libtool


# The object file extension (for standard and static libraries).  This can be
# .o, .tco, .obj, etc., depending on the platform.
#
O  := lo
SO := o


# The executable file extension.  Although most Unix platforms use no
# extension, we copy the extension detected by autoconf.  Useful for cross
# building on Unix systems for non-Unix systems.
#
E := 


# The library file extension (for standard and static libraries).  This can
# be .a, .lib, etc., depending on the platform.
#
A  := la
SA := a


# The name of the final library file.  Note that the DOS-specific Makefile
# uses a shorter (8.3) name.
#
LIBRARY := lib$(PROJECT)


# Path inclusion flag.  Some compilers use a different flag than `-I' to
# specify an additional include path.  Examples are `/i=' or `-J'.
#
I := -I


# C flag used to define a macro before the compilation of a given source
# object.  Usually it is `-D' like in `-DDEBUG'.
#
D := -D


# The link flag used to specify a given library file on link.  Note that
# this is only used to compile the demo programs, not the library itself.
#
L := -l


# Target flag.
#
T := -o$(space)


# C flags
#
#   These should concern: debug output, optimization & warnings.
#
#   Use the ANSIFLAGS variable to define the compiler flags used to enfore
#   ANSI compliance.
#
#   We use our own FreeType configuration file.
#
CPPFLAGS := 
CFLAGS   := -c -Wall -O3 -miphoneos-version-min=8.0 -I/Users/Jonathan/Desktop/FORMATION_PYTHON/EXTERNALS/kivy/examples/demo/touchtracer/kivy-ios/dist/include/arm64/freetype -I/Users/Jonathan/Desktop/FORMATION_PYTHON/EXTERNALS/kivy/examples/demo/touchtracer/kivy-ios/dist/include/arm64/ffi -I/Users/Jonathan/Desktop/FORMATION_PYTHON/EXTERNALS/kivy/examples/demo/touchtracer/kivy-ios/dist/include/arm64/openssl -I/Users/Jonathan/Desktop/FORMATION_PYTHON/EXTERNALS/kivy/examples/demo/touchtracer/kivy-ios/dist/include/common/sdl2 -I/Users/Jonathan/Desktop/FORMATION_PYTHON/EXTERNALS/kivy/examples/demo/touchtracer/kivy-ios/dist/include/common/sdl2_image -I/Users/Jonathan/Desktop/FORMATION_PYTHON/EXTERNALS/kivy/examples/demo/touchtracer/kivy-ios/dist/include/common/sdl2_mixer -I/Users/Jonathan/Desktop/FORMATION_PYTHON/EXTERNALS/kivy/examples/demo/touchtracer/kivy-ios/dist/include/common/sdl2_ttf -I/Users/Jonathan/Desktop/FORMATION_PYTHON/EXTERNALS/kivy/examples/demo/touchtracer/kivy-ios/dist/include/arm64 -DDARWIN_NO_CARBON -DHAVE_FSSPEC=0 -I$(TOP_DIR)/builds/mac/ -I/opt/local/include -DFT_CONFIG_OPTION_SYSTEM_ZLIB -DFT_CONFIG_CONFIG_H="<ftconfig.h>"

# ANSIFLAGS: Put there the flags used to make your compiler ANSI-compliant.
#
ANSIFLAGS :=  -pedantic -ansi

# C compiler to use -- we use libtool!
#
#
CCraw := $(CC)
CC    := $(LIBTOOL) --mode=compile $(CCraw)

# Linker flags.
#
LDFLAGS := -arch arm64 -L/Users/Jonathan/Desktop/FORMATION_PYTHON/EXTERNALS/kivy/examples/demo/touchtracer/kivy-ios/dist/lib -L/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS13.4.sdk/usr/lib -miphoneos-version-min=8.0 -L/opt/local/lib -lz


# export symbols
#
CCraw_build  := gcc	# native CC of building system
E_BUILD      := 	# extension for exexutable on building system
EXPORTS_LIST := $(OBJ_DIR)/ftexport.sym
CCexe        := $(CCraw_build)	# used to compile `apinames' only


# Library linking
#
LINK_LIBRARY = $(LIBTOOL) --mode=link $(CCraw) -o $@ $(OBJECTS_LIST) \
                          -rpath $(libdir) -version-info $(version_info) \
                          $(LDFLAGS) -no-undefined \
                          # -export-symbols $(EXPORTS_LIST)

# EOF
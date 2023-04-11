#!/bin/sh

# Keep this script in sync with python-config.in

exit_with_usage ()
{
    echo "Usage: $0 --prefix|--exec-prefix|--includes|--libs|--cflags|--ldflags|--extension-suffix|--help|--abiflags|--configdir"
    exit $1
}

if [ "$1" = "" ] ; then
    exit_with_usage 1
fi

# Returns the actual prefix where this script was installed to.
installed_prefix ()
{
    RESULT=$(dirname $(cd $(dirname "$1") && pwd -P))
    if which readlink >/dev/null 2>&1 ; then
        if readlink -f "$RESULT" >/dev/null 2>&1; then
          RESULT=$(readlink -f "$RESULT")
        fi
    fi
    echo $RESULT
}

prefix_real=$(installed_prefix "$0")

# Use sed to fix paths from their built-to locations to their installed-to
# locations. Keep prefix & exec_prefix using their original values in case
# they are referenced in other configure variables, to prevent double
# substitution, issue #22140.
prefix="/Users/Jonathan/Desktop/FORMATION_PYTHON/EXTERNALS/kivy/examples/demo/touchtracer/kivy-ios/dist/root/python3"
exec_prefix="${prefix}"
exec_prefix_real=${prefix_real}
includedir=$(echo "${prefix}/include" | sed "s#$prefix#$prefix_real#")
libdir=$(echo "${exec_prefix}/lib" | sed "s#$prefix#$prefix_real#")
CFLAGS=$(echo "-O3 -miphoneos-version-min=8.0 -I/Users/Jonathan/Desktop/FORMATION_PYTHON/EXTERNALS/kivy/examples/demo/touchtracer/kivy-ios/dist/include/x86_64/freetype -I/Users/Jonathan/Desktop/FORMATION_PYTHON/EXTERNALS/kivy/examples/demo/touchtracer/kivy-ios/dist/include/x86_64/ffi -I/Users/Jonathan/Desktop/FORMATION_PYTHON/EXTERNALS/kivy/examples/demo/touchtracer/kivy-ios/dist/include/x86_64/openssl -I/Users/Jonathan/Desktop/FORMATION_PYTHON/EXTERNALS/kivy/examples/demo/touchtracer/kivy-ios/dist/include/common/sdl2 -I/Users/Jonathan/Desktop/FORMATION_PYTHON/EXTERNALS/kivy/examples/demo/touchtracer/kivy-ios/dist/include/common/sdl2_image -I/Users/Jonathan/Desktop/FORMATION_PYTHON/EXTERNALS/kivy/examples/demo/touchtracer/kivy-ios/dist/include/common/sdl2_mixer -I/Users/Jonathan/Desktop/FORMATION_PYTHON/EXTERNALS/kivy/examples/demo/touchtracer/kivy-ios/dist/include/common/sdl2_ttf -I/Users/Jonathan/Desktop/FORMATION_PYTHON/EXTERNALS/kivy/examples/demo/touchtracer/kivy-ios/dist/include/x86_64 --sysroot=/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator13.4.sdk" | sed "s#$prefix#$prefix_real#")
VERSION="3.7"
LIBM="-lm"
LIBC=""
SYSLIBS="$LIBM $LIBC"
ABIFLAGS="m"
LIBS="-lpython${VERSION}${ABIFLAGS} -ldl  $SYSLIBS"
BASECFLAGS=" -Wno-unused-result -Wsign-compare -Wunreachable-code"
LDLIBRARY="libpython$(VERSION)$(ABIFLAGS).a"
LINKFORSHARED=""
OPT="-DNDEBUG -g -fwrapv -O3 -Wall"
PY_ENABLE_SHARED="0"
LDVERSION="$(VERSION)$(ABIFLAGS)"
LIBDEST=${prefix_real}/lib/python${VERSION}
LIBPL=$(echo "$(prefix)/lib/python3.7/config-$(VERSION)$(ABIFLAGS)-darwin" | sed "s#$prefix#$prefix_real#")
SO=".so"
PYTHONFRAMEWORK=""
INCDIR="-I$includedir/python${VERSION}${ABIFLAGS}"
PLATINCDIR="-I$includedir/python${VERSION}${ABIFLAGS}"

# Scan for --help or unknown argument.
for ARG in $*
do
    case $ARG in
        --help)
            exit_with_usage 0
        ;;
        --prefix|--exec-prefix|--includes|--libs|--cflags|--ldflags|--extension-suffix|--abiflags|--configdir)
        ;;
        *)
            exit_with_usage 1
        ;;
    esac
done

for ARG in "$@"
do
    case "$ARG" in
        --prefix)
            echo "$prefix_real"
        ;;
        --exec-prefix)
            echo "$exec_prefix_real"
        ;;
        --includes)
            echo "$INCDIR $PLATINCDIR"
        ;;
        --cflags)
            echo "$INCDIR $PLATINCDIR $BASECFLAGS $CFLAGS $OPT"
        ;;
        --libs)
            echo "$LIBS"
        ;;
        --ldflags)
            LINKFORSHAREDUSED=
            if [ -z "$PYTHONFRAMEWORK" ] ; then
                LINKFORSHAREDUSED=$LINKFORSHARED
            fi
            LIBPLUSED=
            if [ "$PY_ENABLE_SHARED" = "0" ] ; then
                LIBPLUSED="-L$LIBPL"
            fi
            echo "$LIBPLUSED -L$libdir $LIBS $LINKFORSHAREDUSED"
        ;;
        --extension-suffix)
            echo "$SO"
        ;;
        --abiflags)
            echo "$ABIFLAGS"
        ;;
        --configdir)
            echo "$LIBPL"
        ;;
esac
done

# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.26

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "E:\CLion 2023.2.2\bin\cmake\win\x64\bin\cmake.exe"

# The command to remove a file.
RM = "E:\CLion 2023.2.2\bin\cmake\win\x64\bin\cmake.exe" -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = D:\1-Git\Code

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = D:\1-Git\Code\cmake-build-release

# Include any dependencies generated for this target.
include CMakeFiles/new_target.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/new_target.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/new_target.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/new_target.dir/flags.make

CMakeFiles/new_target.dir/_C++Learn/02_Operator.cpp.obj: CMakeFiles/new_target.dir/flags.make
CMakeFiles/new_target.dir/_C++Learn/02_Operator.cpp.obj: D:/1-Git/Code/_C++Learn/02_Operator.cpp
CMakeFiles/new_target.dir/_C++Learn/02_Operator.cpp.obj: CMakeFiles/new_target.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\1-Git\Code\cmake-build-release\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/new_target.dir/_C++Learn/02_Operator.cpp.obj"
	"E:\CLion 2023.2.2\bin\mingw\bin\g++.exe" $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/new_target.dir/_C++Learn/02_Operator.cpp.obj -MF CMakeFiles\new_target.dir\_C++Learn\02_Operator.cpp.obj.d -o CMakeFiles\new_target.dir\_C++Learn\02_Operator.cpp.obj -c D:\1-Git\Code\_C++Learn\02_Operator.cpp

CMakeFiles/new_target.dir/_C++Learn/02_Operator.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/new_target.dir/_C++Learn/02_Operator.cpp.i"
	"E:\CLion 2023.2.2\bin\mingw\bin\g++.exe" $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E D:\1-Git\Code\_C++Learn\02_Operator.cpp > CMakeFiles\new_target.dir\_C++Learn\02_Operator.cpp.i

CMakeFiles/new_target.dir/_C++Learn/02_Operator.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/new_target.dir/_C++Learn/02_Operator.cpp.s"
	"E:\CLion 2023.2.2\bin\mingw\bin\g++.exe" $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S D:\1-Git\Code\_C++Learn\02_Operator.cpp -o CMakeFiles\new_target.dir\_C++Learn\02_Operator.cpp.s

CMakeFiles/new_target.dir/_C++Learn/00_test.cpp.obj: CMakeFiles/new_target.dir/flags.make
CMakeFiles/new_target.dir/_C++Learn/00_test.cpp.obj: D:/1-Git/Code/_C++Learn/00_test.cpp
CMakeFiles/new_target.dir/_C++Learn/00_test.cpp.obj: CMakeFiles/new_target.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\1-Git\Code\cmake-build-release\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/new_target.dir/_C++Learn/00_test.cpp.obj"
	"E:\CLion 2023.2.2\bin\mingw\bin\g++.exe" $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/new_target.dir/_C++Learn/00_test.cpp.obj -MF CMakeFiles\new_target.dir\_C++Learn\00_test.cpp.obj.d -o CMakeFiles\new_target.dir\_C++Learn\00_test.cpp.obj -c D:\1-Git\Code\_C++Learn\00_test.cpp

CMakeFiles/new_target.dir/_C++Learn/00_test.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/new_target.dir/_C++Learn/00_test.cpp.i"
	"E:\CLion 2023.2.2\bin\mingw\bin\g++.exe" $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E D:\1-Git\Code\_C++Learn\00_test.cpp > CMakeFiles\new_target.dir\_C++Learn\00_test.cpp.i

CMakeFiles/new_target.dir/_C++Learn/00_test.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/new_target.dir/_C++Learn/00_test.cpp.s"
	"E:\CLion 2023.2.2\bin\mingw\bin\g++.exe" $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S D:\1-Git\Code\_C++Learn\00_test.cpp -o CMakeFiles\new_target.dir\_C++Learn\00_test.cpp.s

# Object files for target new_target
new_target_OBJECTS = \
"CMakeFiles/new_target.dir/_C++Learn/02_Operator.cpp.obj" \
"CMakeFiles/new_target.dir/_C++Learn/00_test.cpp.obj"

# External object files for target new_target
new_target_EXTERNAL_OBJECTS =

new_target.exe: CMakeFiles/new_target.dir/_C++Learn/02_Operator.cpp.obj
new_target.exe: CMakeFiles/new_target.dir/_C++Learn/00_test.cpp.obj
new_target.exe: CMakeFiles/new_target.dir/build.make
new_target.exe: CMakeFiles/new_target.dir/linkLibs.rsp
new_target.exe: CMakeFiles/new_target.dir/objects1.rsp
new_target.exe: CMakeFiles/new_target.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=D:\1-Git\Code\cmake-build-release\CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable new_target.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\new_target.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/new_target.dir/build: new_target.exe
.PHONY : CMakeFiles/new_target.dir/build

CMakeFiles/new_target.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\new_target.dir\cmake_clean.cmake
.PHONY : CMakeFiles/new_target.dir/clean

CMakeFiles/new_target.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" D:\1-Git\Code D:\1-Git\Code D:\1-Git\Code\cmake-build-release D:\1-Git\Code\cmake-build-release D:\1-Git\Code\cmake-build-release\CMakeFiles\new_target.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/new_target.dir/depend

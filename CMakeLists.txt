cmake_minimum_required(VERSION 3.14)
project(ConanWorld CXX)

list(INSERT CMAKE_MODULE_PATH 0
        "${CMAKE_SOURCE_DIR}/cmake"
        "${CMAKE_BINARY_DIR}"
        )

include(ProjectSettings)

enable_testing()

conan_cmake_run(CONANFILE conanfile.py
        NO_LOAD
        OPTIONS ${CONAN_RUN_OPTIONS}
        BUILD missing)

include(conan_paths)

add_library(libworld STATIC src/world.cpp include/world.h)
target_compile_definitions(libworld
        PUBLIC
        ${PROJECT_COMPILE_DEFINITIONS}
        )
target_link_options(libworld
        PUBLIC
        ${PROJECT_LINK_OPTIONS}
        )
target_include_directories(libworld
        PUBLIC
        $<INSTALL_INTERFACE:include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}/include>
        PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
        )

add_executable(world src/main.cpp)
target_link_options(world
        PRIVATE
        ${PROJECT_LINK_OPTIONS}
        )
target_link_libraries(world
        PRIVATE
        libworld
        )

add_subdirectory(testsuite)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_DEBUG_POSTFIX "d")
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

#set(PROJECT_COMPILE_DEFINITIONS)
#set(PROJECT_LINK_OPTIONS)
# if(WIN32)
#     # Enable unicode for windows builds
#     list(APPEND PROJECT_COMPILE_DEFINITIONS -DUNICODE -D_UNICODE)
#     if(MINGW)
#         list(APPEND PROJECT_LINK_OPTIONS -municode)
#     endif(MINGW)
# endif(WIN32)


option(CMAKE_ENABLE_CONAN  "Enable support for Conan within CMake" ON)

if(CMAKE_ENABLE_CONAN)
    # Download automatically, you can also just copy the conan.cmake file
    if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
        message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
        file(DOWNLOAD "https://github.com/conan-io/cmake-conan/raw/v0.16.1/conan.cmake"
                "${CMAKE_BINARY_DIR}/conan.cmake")
    endif()

    include(${CMAKE_BINARY_DIR}/conan.cmake)
endif(CMAKE_ENABLE_CONAN)

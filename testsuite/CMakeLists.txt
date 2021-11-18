find_package(GTest REQUIRED CONFIG)

file(GLOB HEADERS src/*.h)
file(GLOB SOURCES src/*.cpp)

add_executable(world_test ${SOURCES} ${HEADERS})

target_include_directories(world_test
        PRIVATE
        ${world_SOURCE_DIR}/src
        ${CMAKE_CURRENT_SOURCE_DIR}/src
        )

target_compile_definitions(world_test
        PRIVATE
        -DTEST_WORKING_DIR=\"${CMAKE_CURRENT_SOURCE_DIR}\"
        )

target_link_options(world_test
        PRIVATE
        ${PROJECT_LINK_OPTIONS}
        )

target_link_libraries(world_test
        PRIVATE
        GTest::gtest_main libworld
        )

add_test(NAME world_test WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} COMMAND $<TARGET_FILE:world_test>)

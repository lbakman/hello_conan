from conans import ConanFile, CMake


class WorldConan(ConanFile):
    name = "world"
    version = "1.0.0"
    url = "none"
    license = "none"
    author = "Lau Bakman"
    description = "World"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake", "cmake_paths"
    exports_sources = ["CMakeLists.txt", "src/*", "include/*", "testsuite/*", "cmake/*"]
    build_requires = ["gtest/cci.20210126@lau/stable"]

    def build(self):
        cmake = CMake(self)
        # cmake = CMake(self, generator="Ninja")
        cmake.configure(build_folder=".", source_folder=".")
        cmake.build()
        cmake.test()

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["world"]

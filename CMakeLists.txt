cmake_minimum_required(VERSION 3.12)
project(example)

find_package(pybind11 CONFIG)

pybind11_add_module(_example cc/src/_example.cpp cc/src/example.cpp)
install(TARGETS _example LIBRARY DESTINATION .)

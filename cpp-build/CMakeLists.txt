cmake_minimum_required(VERSION 3.10)

project(MyCMakeProject VERSION 1.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(my_app main.cpp)

# Показываем, что собираем
message(STATUS "Project name: ${PROJECT_NAME}")
message(STATUS "C++ Standard: ${CMAKE_CXX_STANDARD}")

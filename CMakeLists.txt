cmake_minimum_required(VERSION 2.8)
project( MADIZ )


FIND_PACKAGE( OpenMP)
      if(OPENMP_FOUND)
         message("OPENMP FOUND")
         set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
         set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
         set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${OpenMP_EXE_LINKER_FLAGS}")
      endif()
     include_directories(SYSTEM ${OpenMP_INCLUDE_PATH})


add_compile_options(-O2 -Ofast -fopenmp -lstdc++fs)
add_compile_options(-Wl,--as-needed -lfoo -Wl,--as-needed)

add_executable( MADIZ MADIZ.cpp serv.cpp util.cpp obr.cpp)
target_link_libraries(${PROJECT_NAME} stdc++fs)
set_property(TARGET MADIZ PROPERTY CXX_STANDARD 17)
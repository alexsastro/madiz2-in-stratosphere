#ifndef serv_hpp__
#define serv_hpp__

#include <chrono>
#include <ctime>
#include <string>

void process_mem_usage();

std::chrono::time_point<std::chrono::system_clock> start_time();

void get_time(std::chrono::time_point<std::chrono::system_clock> &start, string comment);

#endif

#include "runner.hpp"
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <cassert>
#include <cstring>

#include <unistd.h>
using namespace std;

int main(int argc, char**argv) {
  //rankFeatures();
  //evalNormalizeRigid();
  //evalTasks();
  //bruteSubmission();
  //bruteSolve();
  int only_sid = -1;
  string directory(argv[1]); // VICHANGE add directory argument
  cout << "The directory is " << directory << endl;

  if (argc >= 3) { // VICHANGE: push arguments up by one
    only_sid = atoi(argv[2]); // VICHANGE
    printf("Running only task # %d\n", only_sid);
  }
  int maxdepth = -1;
  if (argc >= 4) { // VICHANGE
    maxdepth = atoi(argv[3]); // VICHANGE
    printf("Using max depth %d\n", maxdepth);
  }
  run(only_sid, maxdepth, directory);
}

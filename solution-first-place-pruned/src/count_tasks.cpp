#include "precompiled_stl.hpp"

using namespace std;

#include "utils.hpp"
#include "core_functions.hpp"
#include "image_functions.hpp"
#include "visu.hpp"
#include "read.hpp"

int main(int argc, char**argv) {
  string directory(argv[1]);
  vector<Sample> sample = readAll(directory, -1);
  cout << sample.size() << endl;
}

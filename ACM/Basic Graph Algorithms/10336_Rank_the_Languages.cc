#include <iostream>
#include <vector>
#include <map>
#include <utility>
#include <list>

using namespace std;

typedef long long ll;
typedef vector<char> vi;
typedef vector<vi> vvi;
typedef map<char, ll> dict;
typedef pair<int,int> p;
typedef pair<char,ll> keyVal;
typedef list<p> lst;

void BFS_helper(vvi* map, int i, int j, lst* frontier, char c) {
  if ((*map)[i][j] == c ) {
    p aPair;
    aPair.first = i;
    aPair.second = j;
    (*frontier).push_back(aPair);
  }
}

void BFS(vvi* map, int i, int j) {
  lst frontier;
  p aPair;
  aPair.first = i;
  aPair.second = j;
  frontier.push_back(aPair);
  char c = (*map)[i][j];
  while (!frontier.empty()) {
    p aPair = frontier.front();
    int cur_i = aPair.first;
    int cur_j = aPair.second;
    frontier.pop_front();
    (*map)[cur_i][cur_j] = 'V';
    BFS_helper(map, cur_i+1, cur_j, &frontier, c);
    BFS_helper(map, cur_i-1, cur_j, &frontier, c);
    BFS_helper(map, cur_i, cur_j+1, &frontier, c);
    BFS_helper(map, cur_i, cur_j-1, &frontier, c);
  }
}

bool keyValSort(const keyVal& first, const keyVal& second) {
  if (first.second == second.second) { // first compare value
    return first.first < second.first; // then compare key
  } else {
    return first.second > second.second;
  }
}

int main() {
  ll N, H, W; // number of test cases, height and width of the map
  cin >> N;
  for (ll cs = 1; cin >> H >> W; ++cs) {
    /** Step 1: read in map
      add dummpy borders surrounding the real map
      for example: 
      if the map is :
        tt
        dd
      we will store it as:
        VVVV
        VttV
        VddV
        VVVV
      The reason doing this is we want to avoid index-out-of-range check in 
        Step 2
    **/
    vvi map(H+2, vi(W+2,'V'));
    for (ll i = 1; i < H+1; ++i) {
      for (ll j = 1; j < W+1; ++j) {
        cin >> map[i][j];
      }
    }

    // Step 2: BFS
    dict output;
    for (ll i = 1; i < H+1; ++i) {
      for (ll j = 1; j < W+1; ++j) {
        char c = map[i][j];
        if (c != 'V') { // if not visited yet
          // a) mark all connected cell with same language to visited
          BFS(&map, i, j);
          // b) increse key value in the dictionary
          ++output[c];
        }
      }
    }

    // step 3: print result
    cout << "World #" << cs << endl;
    list<keyVal> items;
    for (dict::iterator it = output.begin(); it != output.end(); it++ ) {
      pair<char, ll> aPair;
      aPair.first = it->first;
      aPair.second = it->second;
      items.push_back(aPair);
    }
    items.sort(keyValSort); // sort
    for (list<keyVal>::iterator it = items.begin(); it != items.end(); it++ ) {
      cout << it->first << ": " << it->second << endl;
    }
  }

  return 0;
}
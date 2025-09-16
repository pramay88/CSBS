#include <bits/stdc++.h>
using namespace std;

// Recursive DFS function
void dfs_recursive(unordered_map<int, vector<int>>& graph, int node, unordered_set<int>& visited) {
    if (visited.find(node) != visited.end()) return; // already visited

    cout << node << " ";           // process current node
    visited.insert(node);          // mark as visited

    for (int neighbor : graph[node]) {
        dfs_recursive(graph, neighbor, visited);  // recursive call
    }
}

int main() {
    // Graph represented as adjacency list
    unordered_map<int, vector<int>> graph = {
        {1, {2, 3}},
        {2, {4, 5}},
        {3, {6}},
        {4, {}},
        {5, {6}},
        {6, {}}
    };

    unordered_set<int> visited;

    cout << "DFS traversal starting from node 1:\n";
    dfs_recursive(graph, 1, visited);

    return 0;
}

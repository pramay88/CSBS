#include <bits/stdc++.h>
using namespace std;

void bfs(unordered_map<string, vector<string>>& graph, string start) {
    unordered_set<string> visited;
    queue<string> q;
    q.push(start);

    while (!q.empty()) {
        string node = q.front();
        q.pop();

        if (visited.find(node) == visited.end()) {
            cout << node << " ";
            visited.insert(node);

            for (auto& neighbor : graph[node]) {
                q.push(neighbor);
            }
        }
    }
}

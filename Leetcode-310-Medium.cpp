class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if (n == 1) {
            return {0}; // Single node is already the MHT root
        }

        // Build adjacency list
        std::vector<std::vector<int>> adj(n);
        std::vector<int> degree(n, 0);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
            degree[edge[0]]++;
            degree[edge[1]]++;
        }

        // Initialize queue for BFS
        std::queue<int> q;
        for (int i = 0; i < n; ++i) {
            if (degree[i] == 1) {
                q.push(i); // Start BFS from leaf nodes
            }
        }

        // BFS to remove nodes level by level
        while (n > 2) {
            int size = q.size();
            n -= size; // Update total number of nodes
            for (int i = 0; i < size; ++i) {
                int node = q.front();
                q.pop();
                for (int neighbor : adj[node]) {
                    if (--degree[neighbor] == 1) {
                        // If neighbor becomes a leaf node, add it to the queue
                        q.push(neighbor);
                    }
                }
            }
        }

        // Remaining nodes in the queue are centroids
        std::vector<int> centroids;
        while (!q.empty()) {
            centroids.push_back(q.front());
            q.pop();
        }

        return centroids;
    }
};
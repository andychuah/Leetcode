class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        sort(deck.begin(), deck.end());

        int n = deck.size();
        vector<int> result(n);
        deque<int> index;

        for(int i=0 ; i<n ; i++)
        {
            index.push_back(i);
        }

        for(int card: deck)
        {
            int idx = index.front();
            result[idx] = card;
            index.pop_front();
            if(!index.empty())
            {
                index.push_back(index.front());
                index.pop_front();
            }
        }
        return result;
    }
};
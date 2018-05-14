
class Student {
    private:
    vector<int> scores = vector<int>(5);
    
    public:
    void input() {
        for (int i = 0; i < 5; i++)
            cin >> scores[i];
    }
    
    int calculateTotalScore() {
        int sum = 0;
        for (int i = 0; i < 5; i++)
            sum += scores[i];
        return sum;
    }
};
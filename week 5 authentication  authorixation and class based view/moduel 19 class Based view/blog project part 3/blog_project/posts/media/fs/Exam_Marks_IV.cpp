#include <bits/stdc++.h>
using namespace std;
int const mod = 1e9+7;
int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        int n, x;
        cin >> n >> x;
        int s = 1000 - x;
        int val[n];
        long long dp[n + 1][s + 1];
        for (int i = 0; i < n; i++)
            cin >> val[i];
        dp[0][0] = 1;
        for (int i = 1; i <= s; i++)
            dp[0][i] = 0;
        for (int i = 1; i <= n; i++)
        {
            for (int j = 0; j <= s; j++)
            {
                if (val[i - 1] <= j)
                {
                    dp[i][j] = (dp[i][j - val[i - 1]] + dp[i - 1][j]) % mod;
                }
                else
                {
                    dp[i][j] = (dp[i - 1][j]) % mod;
                }
            }
        }
        cout<<dp[n][s]<<endl;
    }

    return 0;
}

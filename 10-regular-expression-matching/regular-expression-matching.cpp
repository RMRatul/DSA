class Solution {
public:

string s,p;
int dp[25][25];

bool dfs(int i,int j)
{
    if(dp[i][j] != -1)
    {
        return dp[i][j];
    }

    if(i==s.size() && j==p.size())
    {
        return dp[i][j]=1;
    }

     if( j==p.size())
    {
        return dp[i][j]=0;
    }

    bool match= (i<s.size() && (s[i]==p[j] || p[j]=='.'));

    if(j+1<p.size() && p[j+1]=='*')
    {
        bool ans= dfs(i,j+2) || (match && dfs(i+1,j));

        return dp[i][j]=ans;
    }

    if(match)
    {
        return dp[i][j]=dfs(i+1,j+1);
    }

    return dp[i][j]=0;


}
    bool isMatch(string st, string pt) {

        s=st;
        p=pt;

        memset(dp,-1,sizeof(dp));

        return dfs(0,0);

        
    }
};
class Solution {
public:
int n,m;
bool dfs(vector<vector<char>>& board,string& word,int i,int j,int k)
{
    if(k==word.size())
    return true;

    if(i<0 || j<0 || i>=m || j>=n || board[i][j]!=word[k])
    return false;

    char temp=board[i][j];
    board[i][j]='#';

    bool ans=dfs(board,word,i+1,j,k+1) || dfs(board,word,i-1,j,k+1) || dfs(board,word,i,j+1,k+1) || dfs(board,word,i,j-1,k+1);


    board[i][j]=temp;

    return ans;
}





    bool exist(vector<vector<char>>& board, string word) {

         m=board.size();
         n=board[0].size();

         int count[256]={0};

          for(int i=0;i<m;i++)
        {
            
        for(int j=0;j<n;j++)
        {
            count[board[i][j]]++;
            
        }

        }

        for(int i=0;i<word.size();i++)
        {
            count[word[i]]--;

            if(count[word[i]]<0)
            return false;
        }


        for(int i=0;i<m;i++)
        {
            
        for(int j=0;j<n;j++)
        {
            if(dfs(board,word,i,j,0))
            return true;
            
        }

        }
        return false;
        
    }
};
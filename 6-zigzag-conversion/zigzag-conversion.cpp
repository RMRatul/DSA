class Solution {
public:
    string convert(string s, int numRows) {

        if(numRows==1 || numRows>= s.size())
    {
        return s;
    }

    vector<string>rows(numRows);

    int currentRow=0;
    bool goingDown=0;

    for(char c:s)
    {
        rows[currentRow]=rows[currentRow]+c;

        if(currentRow==0 || currentRow==(numRows-1))
        {
            goingDown=!goingDown;
        }
        if(goingDown)
        {
            currentRow++;
        }
        else
        {
            currentRow--;
        }
    }

    string res="";

    for(string row:rows)
    {
        res=res+row;
    }

    return res;
        
    }
};
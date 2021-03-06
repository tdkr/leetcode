#include <iostream>
#include <vector>
using namespace std;

class NumMatrix {
public:
    NumMatrix(vector<vector<int>> &matrix) {
        int rows = (int)matrix.size();
        if(rows == 0) {
            return;
        }
        int cols = (int)matrix[0].size();
        sumMatrix = vector<vector<int>>(rows, vector<int>(cols, 0));
        for(int i = 0; i < rows; i++) {
            for(int j = 0; j < cols; j++) {
                if(i >= 1 && j >= 1) {
                    sumMatrix[i][j] = sumMatrix[i-1][j] + sumMatrix[i][j-1] + matrix[i][j] - sumMatrix[i-1][j-1];
                }
                else if(i >= 1) {
                    sumMatrix[i][j] = sumMatrix[i-1][j] + matrix[i][j];
                }
                else if(j >= 1) {
                    sumMatrix[i][j] = sumMatrix[i][j-1] + matrix[i][j];
                }
                else {
                    sumMatrix[i][j] = matrix[i][j];
                }
            }
        }
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        int result = 0;
        if(row1 >= 1 && col1 >= 1) {
            result = sumMatrix[row2][col2] - sumMatrix[row1-1][col2] - sumMatrix[row2][col1-1] + sumMatrix[row1-1][col1-1];
        }
        else if(row1 >= 1) {
            result = sumMatrix[row2][col2] - sumMatrix[row1-1][col2];
        }
        else if(col1 >= 1) {
            result = sumMatrix[row2][col2] - sumMatrix[row2][col1-1];
        }
        else {
            result = sumMatrix[row2][col2];
        }
        return result;
    }

private:
    vector<vector<int>> sumMatrix;
};
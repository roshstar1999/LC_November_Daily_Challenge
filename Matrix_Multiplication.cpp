void multiplication(int arr1[][2], int row1, int col1, int arr2[][2], int row2, int col2 , int result[][2]) {
    // Write your code here
    if (col1!=row2)
    for (int i=0;i<row1;i++)
        for (int j=0;j<col2;j++)
        result[i][j]=-1;
    else {
    
int r;

    for (int i=0;i<row1;i++)
        for (int j=0;j<col1;j++){
            r=0;
            for(int k=0;k<col1;k++){
                r+=arr1[i][k]*arr2[k][j];
            
                }
            result[i][j]=r;
    }    
    }
}

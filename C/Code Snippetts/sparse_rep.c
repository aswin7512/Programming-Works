#include<stdio.h>


void read_mat(int m, int n, int mat[][n]){
    for(int i = 0; i < m; i++)
        for(int j = 0; j < n; j++){
            printf("ENTER ELEMENT A%d%d: ", i+1, j+1);
            scanf("%d", &mat[i][j]);
        }
}


void print_mat(int m, int n, int mat[][n]){
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++)
            printf("%3d", mat[i][j]);
        printf("\n");
    }
}


void sparse_rep(int m, int n, int mat[][n], int sp[][3]){
    int k = 0;
    for(int i = 0; i < m; i++)
        for(int j = 0; j < n; j++)
            if(mat[i][j] != 0){
                sp[++k][0] = i;
                sp[k][1] = j;
                sp[k][2] = mat[i][j];
            }
    sp[0][0] = m;
    sp[0][1] = n;
    sp[0][2] = k;
}


int main(){
    int mat[10][10], sp[20][3], m, n;
    printf("ENTER NO. OF ROWS AND COLUMNS: ");
    scanf("%d %d", &m, &n);
    printf("ENTER MATRIX\n");
    read_mat(m, n, mat);
    printf("MATRIX ENTERED:\n");
    print_mat(m, n, mat);
    printf("CONVERTING TO SPARSE...\n");
    sparse_rep(m, n, mat, sp);
    printf("CONVERTION SUCCESSFULL...\n");
    print_mat(sp[0][2] + 1, 3, sp);
    return 0;
}
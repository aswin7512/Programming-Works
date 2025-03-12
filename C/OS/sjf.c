#include<stdio.h>

void sort(int a[], int b[], int n) {
	int temp, i, j;
	for (i = 0; i < n-1; i++) {
		for (j = 0; j < n - i - 1; j++) {
			if (b[j] > b[j + 1]) {
				temp = b[j];
				b[j] = b[j+1];
				b[j+1] = temp;
				temp = a[j];
				a[j] = a[j+1];
				a[j+1] = temp;
			}
		}
	}
}

int main() {
	int n, i, j;
	printf("Enter No. of Processes: ");
	scanf("%d", &n);
	int p[10], bt[10], wt[10], tat[10];
	float twt = 0, ttat = 0;
	for (i = 0; i < n; i++) {
		printf("Enter BT of P%d: ", i+1);
		scanf("%d", &bt[i]);
		p[i] = i;
	}
	sort(p, bt, n);
	wt[0] = 0;
	tat[0] = bt[0];
	ttat += tat[0];
	for (i = 1; i < n; i++) {
		wt[i] = wt[i - 1] + bt[i - 1];
		tat[i] = wt[i] + bt[i];
		twt += wt[i];
		ttat += tat[i];
	}
	float awt = twt / n, atat = ttat / n;
	printf("%8s%5s%5s%5s\n", "Pno.", "BT", "WT", "TAT");
	for(i = 0; i < n; i++) 
		printf("%8d%5d%5d%5d\n", p[i] + 1, bt[i], wt[i], tat[i]);
	printf("Average Waiting Time: %.2f\n", awt);
	printf("Average Turn Around Time: %.2f\n", atat);
	return 0;
}
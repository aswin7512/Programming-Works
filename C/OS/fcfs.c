#include<stdio.h>
int main() {
	int n, i;
	printf("Enter Number of Processes: ");
	scanf("%d", &n);
	int bt[10], wt[10], tat[10];
	float twt = 0, ttat = 0;
	for (i = 0; i < n; i++) {
		printf("Enter Burst time of process P%d: ", i+1);
		scanf("%d", &bt[i]);
	}
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
		printf("%8d%5d%5d%5d\n", i, bt[i], wt[i], tat[i]);
	printf("Average Waiting Time: %.2f\n", awt);
	printf("Average Turn Around Time: %.2f\n", atat);
	return 0;
}
#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

struct process {
	int pid;
	int at;	
	int bt;
	int wt;
	int tat;
	int ct;
	int btl;
} process[10];


int main() {
	int n, sht, pos, cmp;
	printf("Enter no. of processes: ");
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		printf("Enter at, bt of P%d: ", i+1);
		scanf("%d %d", &process[i].at, &process[i].bt);
		process[i].pid = i+1;
		process[i].btl = process[i].bt;
		process[i].wt = process[i].tat = 0;
	}

	for (int time = 0; 1; time++) {
		sht = INT_MAX;
		cmp = 1;
		pos = 0;
		for (int i = 0; i < n; i++){
			if (process[i].btl != 0)
				cmp = 0;
			if (process[i].at <= time && process[i].btl < sht && process[i].btl != 0) {
				sht = process[i].btl;
				pos = i;
			}
		}
		if (cmp)
			break;
		for (int i = 0; i < n; i++) {
			if (process[i].at <= time && process[i].btl > 0) {
				process[i].tat++;
				if (pos == i) {
					process[i].btl--;
					process[i].ct = time+1;
				} else
					process[i].wt++;
			}
		}
	}

	float tat = 0, wt = 0, avg_tat, avg_wt;
	printf("%5s%4s%4s%4s%5s%4s\n", "Pno", "AT", "BT", "CT", "TAT", "WT");
	for (int i = 0; i < n; i++) {
		printf("%5d%4d%4d%4d%5d%4d\n", process[i].pid, process[i].at, process[i].bt, process[i].ct, process[i].tat, process[i].wt);
		tat += process[i].tat;
		wt += process[i].wt;
	}
	
	avg_tat = tat/n;
	avg_wt = wt/n;
	printf("Avg WT: %.2f\n", avg_wt);
	printf("Avg TAT: %.2f\n", avg_tat);
	return 0;
}
#include<stdio.h>
#include<stdlib.h>

struct process {
	int pid;
	int bt;
	int wt;
	int tat;
	int ct;
	int btl;
} process[10];


int main() {
	int n, tq;
	printf("Enter no. of processes: ");
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		printf("Enter bt of P%d: ", i+1);
		scanf("%d", &process[i].bt);
		process[i].pid = i+1;
		process[i].btl = process[i].bt;
		process[i].wt = process[i].tat = 0;
	}
	printf("Enter Time Quantum: ");
	scanf("%d", &tq);

	int time = 0, pos = 0, cmp, adv;
	while(1){
		cmp = 1;
		for (int i = 0; i < n; i++){
			if (process[i].btl != 0)
				cmp = 0;
		}
		if (cmp)
			break;
		for (int i = 0; i < n; i++) {
			if (process[i].btl > 0) {
				adv = process[i].btl < tq ? process[i].btl : tq;
				process[i].btl -= adv;
                if (process[i].btl == 0) {
				    process[i].ct = process[i].tat = time + adv;
                    process[i].wt = process[i].tat - process[i].bt;
                }
			}
            time += adv;
		}
	}

	float tat = 0, wt = 0, avg_tat, avg_wt;
	printf("%5s%4s%4s%5s%4s\n", "Pno", "BT", "CT", "TAT", "WT");
	for (int i = 0; i < n; i++) {
		printf("%5d%4d%4d%5d%4d\n", process[i].pid, process[i].bt, process[i].ct, process[i].tat, process[i].wt);
		tat += process[i].tat;
		wt += process[i].wt;
	}
	
	avg_tat = tat/n;
	avg_wt = wt/n;
	printf("Avg WT: %.2f\n", avg_wt);
	printf("Avg TAT: %.2f\n", avg_tat);
	return 0;
}
#include<stdio.h>
int main(){
    struct employee{
        int emp_id;
        char emp_name[20];
        float basic;
        float da;
        float tax;
        float nsalary;
    }emp;
    printf("ENTER EMPLOYEE ID: ");
    scanf("%d",&emp.emp_id);
    printf("ENTER EMPLOYEE NAME: ");
    scanf("%s",&emp.emp_name);
    printf("ENTER BASIC PAY: ");
    scanf("%f",&emp.basic);
    printf("ENTER DA: ");
    scanf("%f",&emp.da);
    printf("ENTER TAX: ");
    scanf("%f",&emp.tax);
    emp.nsalary=emp.basic+emp.da-emp.tax;
    printf("%10s %20s %10s %10s %10s %10s\n","EMP_ID","EMP_NAME","BASIC","DA","TAX","NETSALARY");
    printf("%10d %20s %10.2f %10.2f %10.2f %10.2f\n",emp.emp_id,emp.emp_name,emp.basic,emp.da,emp.tax,emp.nsalary);
    return 0;
}
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <math.h>

const char *admin_panel_variables[][2] = {
    {"Variable Name", "type"}
    {"data_count", "int"},
    {"course_code_length", "int"},
    {"check_settings_result", "bool"}
};

int data_count = 0;
int course_code_length = 0;

bool check_settings_result = ((data_count!=0) && (course_code_length!=0));

typedef struct{

    char course_code[course_code_length]

}couese_details;

void main(){

    bool exit_choice = false;

    do{

        print_main_menu();
        int menu_choice = choice();
        check_settings();

        switch(menu_choice){

            case 1:
                break;
            case 2:
                break;
            case 3:
                analysis_gpa();
                break;
            case 4:
                admin_panel();
                break;
            case 5:
                documentation();
                break;
            case 9:
                exit_choice = exit();
                break;
            default:
                printf("Wrong Choice!");
                break;

        }

    } while(exit_choice==true);

}

bool choice(){

    char choice;
    scanf("%c", &choice);
    
    do{
        switch(choice){
        
            case 'Y':
                return true;
                break;
            case 'y':
                return true;
                break;
            case 'N':  
                return false;
                break;
            case 'n':
                return false;
                break;
            default:
                printf("Wrong choice!\n");
                continue;

        }
    } while(true);

}

int choice(){

    int choice;
    printf("Enter Your Choice: ");
    scanf("%d", &choice);
    return choice;

}

float calculate_gpa(float gpa[data_count], int credit[data_count]){

    float sumProduct_gpa_credit = 0.00;
    int sum_credit = 0;

    for(int i=0; i<data_count; i++){
        sumProduct_gpa_credit += ( (float) gpa[i] * credit[i]);
        sum_credit += credit[i];
    }

    float calculated_gpa = (float) sumProduct_gpa_credit/ sum_credit;
    return calculated_gpa;

}

int get_course_details(){



}

void print_main_menu(){

    printf("********************************************************************************\n\n");
    printf("1.Register Course Details\n");
    printf("2.Print Registered Course Details\n");
    printf("3.Calculate & Analysis of GPA\n");
    printf("4.Admin Panel\n");
    printf("5.Documentation\n");
    printf("9.Exit\n\n");

}

bool exit(){

    char exit_choice;
    printf("Do you want to exit? (Y/n): ");
    bool exit_choice = choice();

    if(exit_choice==true){
        printf("Exited!.\n");
        return true;
    } else {
        printf("Returned to main menu!.\n\n");
        return false;
    }


}

void check_Settings(){

    if(check_settings_result==false){
        printf("Admin Panel Setting(s) are not Initialized correctly!.\n");
        printf("Do you want to check/ modify? (Y/n): ");
        bool Yn_choice = choice();
        if(Yn_choice==true){
            admin_panel();
        } else {
            printf("Can\'t Run the programe without initializing/ modify Admin Panel\n\n");
            continue;
        }

    }

}

int admin_panel_int(){

}

float admin_panel_float(){

}

char admin_panel_char(){

}

bool admin_panel_bool(){

}

void admin_panel(){

    printf("%-5s %-20s Values\n", admin_panel_variables[0][1], admin_panel_variables[0][0]);
    printf("%-5s %-20s %-5d\n", admin_panel_variables[1][1], admin_panel_variables[1][0], data_count);
    printf("%-5s %-20s %-5d\n", admin_panel_variables[2][1], admin_panel_variables[2][0], course_code_length);
    printf("%-5s %-20s %-5d\n", admin_panel_variables[3][1], admin_panel_variables[3][0], check_settings_result);

}

void typeof_var(){

}

void documentation(){

}

void analysis_gpa(){

}

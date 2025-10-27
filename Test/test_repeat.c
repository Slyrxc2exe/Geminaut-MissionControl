#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char *argv[]){
    int opt;
    int repeat = 1, print_newline = 1;

    extern char *optarg;
    extern int optind;

    char *message = NULL;
    int message_len = 0;

    while((opt = getopt(argc, argv, "r:n")) != -1){
        switch(opt){
            case 'r':
                repeat = atoi(optarg);

                if(repeat < 0){
                    printf(stderr, "Error: The number of repeats cannot be negative\n");
                    //perror("Error: The number of repeats cannot be negative")
                    return 1;
                }
                break;

            case 'n':
                print_newline = 0;

                break;

            default:
                printf(stderr, "Error: Usage should be like this:...\n");
                return 1;
        }
    }

    if(optind < argc){
        for(int i = optind; i < argc; i++){
            message_len += strlen(argv[i]) + 1;
        }

        message = malloc(message_len);
        if(message == NULL){
            printf(stderr, "Memory allocation failed\n");
            return 1;
        }

        message[0] = '\0';

        for(int i = optind, i < argc; i++){
            if(i > optind){
                strcat(message, " ");
            }
            strcat(message, argv[i]);
        }
    }
}